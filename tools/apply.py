import sys
tgt=sys.argv[1]; s=open(tgt,encoding='utf8').read()
for ln in sys.stdin.read().splitlines():
    if ' ==> ' not in ln: continue
    a,b=ln.split(' ==> ',1)
    n=s.count('\n'+a+'\n')
    if n!=1: print('XATO (%d marta):'%n,a); continue
    s=s.replace('\n'+a+'\n','\n'+b+'\n',1)
open(tgt,'w',encoding='utf8').write(s)
