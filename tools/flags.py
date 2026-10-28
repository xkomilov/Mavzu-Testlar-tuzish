import sys; sys.path.insert(0,'/projects/sandbox/work/tools')
import build_tests as b
t=b.parse(sys.argv[1])
for tid,items in t.items():
    for it in items:
        mx=max(len(x) for x in it['wrong']); r=len(it['correct'])/mx
        if r>1.10:
            print(tid,it['line'],'|',it['q'][:70]); print('  C',len(it['correct']),it['correct'])
            for w in it['wrong']: print('  W',len(w),w)
