import sys
# usage: setopts.py file < spec
# spec: lines "? <question prefix>" followed by "+ ..." and 4x "- ..." (new options). Optional "! new note" line.
tgt=sys.argv[1]
L=open(tgt,encoding='utf8').read().split('\n')
spec=sys.stdin.read().split('\n')
blocks=[];cur=None
for ln in spec:
    if ln.startswith('? '):
        cur={'q':ln[2:].strip(),'opts':[],'note':None};blocks.append(cur)
    elif cur is not None and (ln.startswith('+ ') or ln.startswith('- ')):
        cur['opts'].append(ln)
    elif cur is not None and ln.startswith('! '):
        cur['note']=ln
for b in blocks:
    idx=[i for i,x in enumerate(L) if x.startswith('? '+b['q'])]
    if len(idx)!=1: print('XATO',len(idx),b['q']);continue
    i=idx[0]
    j=i+1
    while not L[j].startswith('!'): j+=1
    if len(b['opts'])!=5 or not b['opts'][0].startswith('+ '): print('XATO format',b['q']);continue
    L[i+1:j]=b['opts']
    if b['note']:
        k=i+1
        while not L[k].startswith('!'): k+=1
        L[k]=b['note']
open(tgt,'w',encoding='utf8').write('\n'.join(L))
