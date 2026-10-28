import json,re,sys
i,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
t=re.sub(r'\s+',' ',json.load(open(f'cache/{i}.json'))['matn'])
print(t[a:b])
