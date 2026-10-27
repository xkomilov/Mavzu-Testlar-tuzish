import sys,re
# usage: autoshort.py file  -- if correct is >1.10x longest wrong, drop trailing ", ..." or " (...)" segments of the correct answer
p=sys.argv[1]
L=open(p,encoding='utf8').read().split('\n')
changed=0
i=0
while i<len(L):
    if L[i].startswith('? '):
        j=i+1
        while j<len(L) and not L[j].startswith('!'): j+=1
        block=L[i+1:j]
        cidx=[k for k,x in enumerate(block) if x.startswith('+ ')]
        w=[x[2:] for x in block if x.startswith('- ')]
        if len(cidx)==1 and w:
            c=block[cidx[0]][2:]
            mx=max(len(x) for x in w)
            orig=c
            while len(c)>1.10*mx:
                m=re.match(r'^(.*\S)\s*\([^()]*\)$',c)
                if m and len(m.group(1))>=8: c=m.group(1); continue
                if ',' in c:
                    c2=c.rsplit(',',1)[0].strip()
                    if len(c2)>=8: c=c2; continue
                break
            if c!=orig and len(c)<=1.10*mx:
                block[cidx[0]]='+ '+c; L[i+1:j]=block; changed+=1
        i=j
    else: i+=1
open(p,'w',encoding='utf8').write('\n'.join(L))
print('qisqartirildi:',changed)
