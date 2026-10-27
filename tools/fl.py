import sys
sys.path.insert(0,'/projects/sandbox/work/tools')
import build_tests as b
t=b.parse(sys.argv[1]); lo=int(sys.argv[2]); hi=int(sys.argv[3])
for tid,items in t.items():
    if not (lo<=int(tid)<=hi): continue
    for it in items:
        mx=max(len(x) for x in it['wrong']); r=len(it['correct'])/mx
        firsts=[w.split()[0].lower() for w in it['wrong']]
        rep=max(firsts.count(f) for f in set(firsts))
        bad=sum(1 for w in it['wrong'] if w.lower().startswith(b.BAD_START))
        flag=[]
        if r>1.10: flag.append('LEN %d/%d'%(len(it['correct']),mx))
        if rep>=3: flag.append('SAME%d'%rep)
        if bad>=2 or it['correct'].lower().startswith(b.BAD_START): flag.append('FAQAT')
        if flag: print(tid,'|',it['q'][:62],'|',' '.join(flag))
