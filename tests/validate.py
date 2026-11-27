from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'data/policies.json').read_text())
p=d['policies']; ids={x['id'] for x in p}; assert len(ids)==len(p)==23
html=(R/'index.html').read_text()
guide=(R/'README.md').read_text()
for x in p:
 for k in ['title','region','kind','priority','amount','window','conditions','steps','materials','risks','sources','entry','verified']: assert x[k], (x['id'],k)
 assert x['verified']==d['as_of']; assert all(s['url'].startswith('https://') for s in x['sources'])
 assert f'id="{x["id"]}"' in html
 assert f'### {x["id"]}｜' in guide
for fn in ['data/policies.csv','templates/ledger.csv']:
 with (R/fn).open(encoding='utf-8-sig') as f: assert {r['ID'] for r in csv.DictReader(f)}==ids
for fn in ['templates/contact.md','templates/project-evidence.md','templates/profile.local.example.json','LICENSE','docs/PUBLISH.md']: assert (R/fn).is_file()
assert 'data-print-guide' in html
print(f'Validated {len(p)} policies; all files consistent')
