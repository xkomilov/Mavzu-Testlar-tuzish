import sys
# usage: set4.py file ; stdin lines: "question-prefix ==> new 4th wrong"
tgt=sys.argv[1]
L=open(tgt,encoding='utf8').read().split('\n')
for ln in sys.stdin.read().splitlines():
    if ' ==> ' not in ln: continue
    q,w=ln.split(' ==> ',1)
    idx=[i for i,x in enumerate(L) if x.startswith('? '+q)]
    if len(idx)!=1: print('XATO',len(idx),q); continue
    j=idx[0]
    while not L[j].startswith('!'): j+=1
    L[j-1]='- '+w
open(tgt,'w',encoding='utf8').write('\n'.join(L))
