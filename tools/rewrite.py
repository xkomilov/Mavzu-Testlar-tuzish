import sys
# stdin: "@@<qator>" bilan boshlanuvchi bloklar; fayldagi shu qatordan boshlanadigan savol bloki almashtiriladi
tgt=sys.argv[1]
lines=open(tgt,encoding='utf8').read().split('\n')
new={}
cur=None
for ln in sys.stdin.read().split('\n'):
    if ln.startswith('@@'):
        cur=int(ln[2:].strip()); new[cur]=[]
    elif cur is not None:
        new[cur].append(ln)
out=[];i=0
while i<len(lines):
    n=i+1
    if n in new:
        assert lines[i].startswith('?'),(n,lines[i])
        j=i
        while j<len(lines) and lines[j].strip()!='': j+=1
        blk=[l for l in new[n] if l.strip()!='']
        out.extend(blk); i=j
    else:
        out.append(lines[i]); i+=1
open(tgt,'w',encoding='utf8').write('\n'.join(out))
