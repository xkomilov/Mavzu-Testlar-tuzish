import sys,re
p=sys.argv[1]; s=open(p,encoding='utf8').read().split('\n')
out=[]
for l in s:
    m=re.match(r'^([+-]) (Faqat|Hech|Umuman|Barcha) (.*)$',l)
    if m and not (m.group(2)=='Hech' and False):
        rest=m.group(3); rest=rest[0].upper()+rest[1:]
        l='%s %s'%(m.group(1),rest)
    out.append(l)
open(p,'w',encoding='utf8').write('\n'.join(out))
