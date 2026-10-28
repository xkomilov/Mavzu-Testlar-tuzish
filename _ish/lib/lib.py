import sys,json,os,re,urllib.request,urllib.parse
UA={"User-Agent":"Mozilla/5.0"}
CACHE='cache'; os.makedirs(CACHE,exist_ok=True)
def api(path,timeout=40):
    return json.load(urllib.request.urlopen(urllib.request.Request("https://xayrullokomilov.uz"+path,headers=UA),timeout=timeout))
def search(q,pages=1):
    out=[]
    for p in range(1,pages+1):
        r=api("/api/materiallar?"+urllib.parse.urlencode({"q":q,"sahifa":p}))
        out+=r['materiallar']
        if len(out)>=r['jami']: break
    return out
def doc(i):
    f=f'{CACHE}/{i}.json'
    if not os.path.exists(f):
        d=api(f"/api/materiallar/{i}",timeout=60)
        json.dump(d,open(f,'w'))
    return json.load(open(f))
def show(q,pages=1):
    r=search(q,pages)
    print(f"## {q}")
    for m in r:
        print(f"  {m['id']:>5} | {m['hujjatTuri']:<17} | {m.get('raqami')} | kuchda={m.get('kuchda')} ai={m.get('ai')} | {m['nomi'][:120]}")
def grep(i,pat,w=250,n=6):
    d=doc(i); t=d['matn']; ms=list(re.finditer(pat,t,flags=re.I))
    print(f"--- [{i}] {d['nomi'][:80]} | {len(ms)} matches")
    for m in ms[:n]:
        print('   …',t[max(0,m.start()-w):m.end()+w].replace('\n',' '),'…\n')
if __name__=='__main__':
    for q in sys.argv[1:]: show(q)
