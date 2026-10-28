import zipfile,sys,re,collections
from xml.etree import ElementTree as ET
N={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def read(path):
    z=zipfile.ZipFile(path)
    sst=[''.join(t.text or '' for t in si.iter('{%s}t'%N['m'])) for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',N)]
    sh=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    rows=[]
    for r in sh.find('m:sheetData',N):
        d={}
        for c in r:
            col=re.match(r'[A-Z]+',c.get('r')).group(0)
            v=c.find('m:v',N); d[col]=(sst[int(v.text)],c.get('s'))
        rows.append(d)
    return sh,rows,z
if __name__=='__main__':
    for p in sys.argv[1:]:
        sh,rows,z=read(p)
        dim=sh.find('m:dimension',N).get('ref'); dv=sh.find('m:dataValidations/m:dataValidation',N)
        hdr=[rows[0][c][0] for c in 'ABCDEFGH']
        assert hdr==['Question','A','B','C','D','E','Correct',"Comment (Faqat to'g'ri javob uchun)"],hdr
        assert dim=='A1:H%d'%len(rows),dim
        assert dv.get('sqref')=='G2:G1048576' and dv.find('m:formula1',N).text=='$B$1:$F$1'
        cnt=collections.Counter()
        for i,r in enumerate(rows[1:],2):
            L=r['G'][0]; assert L in 'ABCDE'; cnt[L]+=1
            ans=r['BCDEF'['ABCDE'.index(L)]][0]
            assert r['H'][0].startswith("To'g'ri javob: %s. "%ans) and "Manba: " in r['H'][0],i
            assert len({r[c][0] for c in 'BCDEF'})==5
            assert all(r[c][1]=='1' for c in 'ABCDEFGH')
        print(p,dim,dict(cnt),'dv:',dv.get('sqref'),dv.find('m:formula1',N).text,'OK')
