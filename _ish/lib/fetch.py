import sys,json,os,time,urllib.request
os.makedirs('cache',exist_ok=True)
for a in sys.argv[1:]:
    i=int(a); f=f'cache/{i}.json'
    if os.path.exists(f): continue
    for t in range(3):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(f"https://xayrullokomilov.uz/api/materiallar/{i}",headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
            json.dump(d,open(f,'w')); print(i,len(d.get('matn') or ''),d['nomi'][:70],flush=True); break
        except Exception as e:
            time.sleep(2)
    else: print(i,'FAILED',flush=True)
