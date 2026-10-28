import json,urllib.request,urllib.parse,math,time,sys,os
UA={"User-Agent":"Mozilla/5.0"}
def page(mv,p):
    u="https://xayrullokomilov.uz/api/materiallar?"+urllib.parse.urlencode({"mavzu":mv,"sahifa":p})
    for a in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25))
        except Exception as e: time.sleep(2)
    raise RuntimeError(f"fail {mv} {p}")
idx=json.load(open('index.json')) if os.path.exists('index.json') else {}
for mv in map(int,sys.argv[1:]):
    if str(mv) in idx: continue
    r=page(mv,1); items=r['materiallar']; n=math.ceil(r['jami']/r['sahifaHajmi'])
    for p in range(2,n+1): items+=page(mv,p)['materiallar']
    idx[str(mv)]=[{k:m.get(k) for k in('id','nomi','hujjatTuri','raqami','qabulSanasi','kuchda','ai')} for m in items]
    json.dump(idx,open('index.json','w'),ensure_ascii=False); print(mv,len(items),flush=True)
