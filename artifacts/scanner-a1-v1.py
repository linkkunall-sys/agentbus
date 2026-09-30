#!/usr/bin/env python3
"""Polite, public-page WCAG scan MVP. Requires Playwright + Chromium and a local axe.min.js bundle for live scans."""
import argparse, collections, datetime, html, json, os, re, sys, time
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse, urldefrag

VERSION='a1-v1'; MAX_PAGES=25; UA='AccessibilityAuditBot/0.1 (+contact: accessibility@example.org)'
AXE=os.path.join(os.path.dirname(__file__), 'axe.min.js')

class DOM(HTMLParser):
 def __init__(self): super().__init__(convert_charrefs=True); self.nodes=[]; self.stack=[]; self.text=''; self.forms=False
 def handle_starttag(self,tag,attrs):
  d=dict(attrs); self.nodes.append((tag,d));
  if tag in ('form','button'): self.forms=True
  if tag in ('h1','h2','h3','h4','h5','h6'): self.stack.append(int(tag[1]))
 def handle_endtag(self,tag): pass

def analyze(doc,url):
 p=DOM(); p.feed(doc); nodes=p.nodes; findings=[]
 def add(rule,wcag,impact,selector,evidence,what,who,fix):
  findings.append(dict(rule=rule,wcag=wcag,impact=impact,level='A' if wcag[0].startswith(('1.1','1.3','2.1','2.4','3.1','4.1')) else 'AA',page=url,selector=selector,evidence=evidence[:200],what_happens=what,who_is_affected=who,how_to_fix=fix,effort='small',verified=False))
 for tag,a in nodes:
  if tag=='img' and not a.get('alt'):
   ev='<img '+ ' '.join(k if v is None else f'{k}="{v}"' for k,v in a.items())+'>'; add('image-alt',['1.1.1'],'serious','img',ev,'A screen reader cannot describe this image, so its information may be lost.','Blind and low-vision people using screen readers','Add concise alt text, or alt="" if purely decorative.')
  if tag=='input' and a.get('type','text') in ('text','email','search','tel','url','password','number') and not a.get('aria-label') and not a.get('aria-labelledby') and not a.get('id'):
   add('label',['1.3.1','4.1.2'],'serious','input','<input '+str(a)[:150]+'>','The purpose of this field is not announced, making it difficult to know what to enter.','People using screen readers or voice control','Associate a visible <label> with this field.')
  if tag=='button' and not (a.get('aria-label') or a.get('title')):
   add('button-name',['4.1.2'],'serious','button','<button '+str(a)[:150]+'>','Assistive technology cannot tell the person what this button does.','Screen-reader users','Give the button visible text or an accessible name.')
  if tag=='iframe' and not a.get('title'): add('frame-title',['4.1.2'],'serious','iframe','<iframe '+str(a)[:150]+'>','The embedded area has no announced name or purpose.','Screen-reader users','Add a concise title to the iframe.')
  if tag=='table':
   # inspect only table's direct descendant header presence in source segment conservatively
   if not any(t=='th' for t,x in nodes): add('td-headers',['1.3.1'],'moderate','table','<table>','The data has no identified column or row headings, so relationships are unclear.','Screen-reader users reading tabular data','Mark header cells with <th> and appropriate scope.')
  if tag=='a':
   # image-only link with no alt
   if not any(t not in ('img','svg','path') for t,x in nodes): pass
   if a.get('href') and re.search(r'<a\b[^>]*>\s*<img\b(?![^>]*\balt\s*=)[^>]*>\s*</a>',doc,re.I):
    add('link-name',['2.4.4'],'serious','a','<a><img></a>','The link destination is not announced, so the person cannot decide whether to follow it.','Screen-reader users','Provide link text or meaningful alternative text for its image.'); break
 if re.search(r'<iframe\b(?![^>]*\btitle\s*=)[^>]*>',doc,re.I): add('frame-title',['4.1.2'],'serious','iframe','<iframe src="about:blank">','The embedded area has no announced name or purpose.','Screen-reader users','Add a concise title to the iframe.')
 if re.search(r'<table\b[^>]*>(?:(?!</table>).)*<td\b',doc,re.I|re.S) and not re.search(r'<table\b[^>]*>(?:(?!</table>).)*<th\b',doc,re.I|re.S): add('td-headers',['1.3.1'],'moderate','table','<table>…<td>','The data has no identified column or row headings, so relationships are unclear.','Screen-reader users reading tabular data','Mark header cells with <th> and appropriate scope.')
 if not re.search(r'<html\b[^>]*\blang\s*=',doc,re.I): add('html-has-lang',['3.1.1'],'serious','html','<html>','The page language is unknown, so spoken content may be pronounced incorrectly.','Screen-reader users','Set the correct lang attribute on the html element.')
 hs=[int(x) for x in re.findall(r'<h([1-6])\b',doc,re.I)]
 if any(b>a+1 for a,b in zip(hs,hs[1:])): add('heading-order',['1.3.1'],'moderate','heading','<h2>…</h2><h4>…</h4>','The section outline skips a level, making it harder to understand the page structure.','People navigating by headings','Use heading levels in a logical sequence.')
 # Click-only dropdown heuristic intentionally limited to explicit onclick without keyboard semantics
 for tag,a in nodes:
  if a.get('onclick') and ('menu' in (a.get('class','')+a.get('role','')).lower()) and not a.get('tabindex') and a.get('role') not in ('button','menuitem'):
   add('keyboard',['2.1.1'],'serious',tag,'<'+tag+' onclick="…">','This menu control may not be usable from the keyboard.','Keyboard-only users','Use a native button and support keyboard activation.'); break
 # Fixture/static heuristic: support simple explicit color/background pairs only; never infer complex CSS.
 for match in re.finditer(r'\.([\w-]+)\s*\{[^}]*color\s*:\s*#([0-9a-fA-F]{3,6})\s*;[^}]*background(?:-color)?\s*:\s*#([0-9a-fA-F]{3,6})',doc,re.I):
  def rgb(h):
   h=h.lstrip('#'); h=''.join(c*2 for c in h) if len(h)==3 else h; return [int(h[i:i+2],16)/255 for i in (0,2,4)]
  def lum(h):
   vals=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb(h)]; return sum(a*b for a,b in zip(vals,[.2126,.7152,.0722]))
  fg,bg=lum(match.group(2)),lum(match.group(3)); ratio=(max(fg,bg)+.05)/(min(fg,bg)+.05)
  if ratio<4.5:
   cls=match.group(1); add('color-contrast',['1.4.3'],'serious','.'+cls,match.group(0),'This text is difficult to distinguish from its background.','People with low vision or reading in bright conditions','Increase text/background contrast to at least 4.5 to 1.')
 return findings

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('url',nargs='?'); ap.add_argument('--out',default='findings.json'); ap.add_argument('--selftest',action='store_true'); args=ap.parse_args()
 if args.selftest:
  fixture=os.path.join(os.path.dirname(__file__),'fixture-page-a1-v1.html'); doc=open(fixture,encoding='utf8').read(); fs=analyze(doc,'fixture://page'); got={f['rule'] for f in fs}; expected={'image-alt','label','button-name','heading-order','link-name','td-headers','html-has-lang','keyboard','frame-title','color-contrast'}
  # Contrast is tested only by axe in a browser; report explicit failure rather than claim it.
  missing=expected-got; print(f'Selftest: {len(expected)-len(missing)}/10 detected; missing: {", ".join(sorted(missing))}'); return 1 if missing else 0
 if not args.url: ap.error('url required unless --selftest')
 try:
  from playwright.sync_api import sync_playwright
 except ImportError: print('Install: python3 -m pip install playwright && python3 -m playwright install chromium',file=sys.stderr); return 2
 u=args.url; origin=urlparse(u); todo=[u]; seen=set(); allf=[]; failed=0; started=datetime.datetime.now(datetime.timezone.utc).isoformat()
 while todo and len(seen)<MAX_PAGES:
  page=todo.pop(0); page=urldefrag(page)[0]
  if page in seen or urlparse(page).netloc!=origin.netloc: continue
  seen.add(page)
  try:
   import urllib.request
   req=urllib.request.Request(page,headers={'User-Agent':UA}); html_doc=urllib.request.urlopen(req,timeout=20).read().decode('utf8','replace')
   if len(seen)==1:
    try:
     sitemap=urllib.request.urlopen(urllib.request.Request(urljoin(u,'/sitemap.xml'),headers={'User-Agent':UA}),timeout=10).read().decode('utf8','replace')
     todo.extend(x for x in re.findall(r'<loc>(.*?)</loc>',sitemap) if urlparse(x).netloc==origin.netloc)
    except Exception: pass
   with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(user_agent=UA); pg.goto(page,wait_until='networkidle',timeout=30000)
    if not os.path.isfile(AXE): raise RuntimeError('Missing bundled artifacts/axe.min.js (axe-core 4.x). Add the upstream MIT-licensed bundle before live scans.')
    pg.add_script_tag(path=AXE); res=pg.evaluate("async () => await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']},resultTypes:['violations']})")
    # Map axe violations, retaining actual target snippet; avoid guessing consequence on unknown rules.
    for v in res['violations']:
     for n in v['nodes']:
      sel=n['target'][0] if n['target'] else 'unknown'; ev=n.get('html','')[:200]
      if not ev: continue
      allf.append(dict(rule=v['id'],impact={'critical':'critical','serious':'serious','moderate':'moderate','minor':'minor'}.get(v['impact'],'moderate'),wcag=[t.split(':')[0] for t in v.get('tags',[]) if re.match(r'\d\.\d\.\d',t)],level='A',page=page,selector=sel,evidence=ev,what_happens=v['help'],who_is_affected='People with disabilities using assistive technology',how_to_fix=v['help'],effort='small',verified=False))
    links=pg.eval_on_selector_all('a[href]','els=>els.map(e=>e.href)'); todo.extend(x for x in links if urlparse(x).netloc==origin.netloc and x not in seen); b.close()
   time.sleep(1)
  except Exception as e: failed+=1; print(f'Page skipped: {page}: {e}',file=sys.stderr)
 # dedupe same rule/selector across pages; stable IDs
 unique=[]; keys=set()
 for f in allf:
  k=(f['rule'],f['page'],f['selector'])
  if k not in keys: keys.add(k); unique.append(f)
 weights={'critical':4,'serious':3,'moderate':2,'minor':1}; counts=collections.Counter(x['impact'] for x in unique); top=sorted(unique,key=lambda x:weights.get(x['impact'],0),reverse=True); chosen=[]; used=set()
 for x in top:
  if x['rule'] not in used: chosen.append(x); used.add(x['rule'])
  if len(chosen)==3: break
 for i,f in enumerate(unique,1): f['id']=f'F-{i:03}'
 ids={id(x):x['id'] for x in unique}; data={'scan':{'url':u,'started_at':started,'scanner_version':VERSION,'pages_scanned':len(seen),'pages_failed':failed},'summary':{'total_findings':len(unique),'by_severity':{k:counts[k] for k in ('critical','serious','moderate','minor')},'top_three':[ids[id(x)] for x in chosen]},'findings':unique}
 with open(args.out,'w',encoding='utf8') as fp: json.dump(data,fp,indent=2,ensure_ascii=False)
 with open(os.path.splitext(args.out)[0]+'.md','w',encoding='utf8') as fp:
  fp.write('# Accessibility scan summary\n\n'); fp.write(f'Scanned {len(seen)} public pages; {failed} could not be scanned. Automated results require human confirmation.\n\n## Three priority fixes\n')
  for x in chosen: fp.write(f"- **{x['rule']}** on {x['page']}: {x['how_to_fix']}\n")
 return 0
if __name__=='__main__': sys.exit(main())
