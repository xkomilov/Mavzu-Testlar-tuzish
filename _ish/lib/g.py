import json,re,sys
i=sys.argv[1]; pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 600; mx=int(sys.argv[4]) if len(sys.argv)>4 else 3
t=json.load(open(f'cache/{i}.json'))['matn']
t=re.sub(r'\s+',' ',t)
n=0
for m in re.finditer(pat,t,re.I):
    print(f'--[{m.start()}]--',t[max(0,m.start()-100):m.start()+w]); n+=1
    if n>=mx: break
print('total hits',len(re.findall(pat,t,re.I)),'len',len(t))
