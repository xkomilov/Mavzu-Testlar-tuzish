#!/usr/bin/env python3
"""Mavzu .docx fayllaridan oddiy matn ajratadi: extract_docx.py <docx_papka> <chiqish_papka>"""
import sys, glob, os, zipfile
from xml.etree import ElementTree as ET
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for f in sorted(glob.glob(os.path.join(src, '*.docx'))):
    root = ET.fromstring(zipfile.ZipFile(f).read('word/document.xml'))
    paras = []
    for p in root.iter(W + 'p'):
        t = ''.join(n.text or '' for n in p.iter(W + 't'))
        if t.strip():
            paras.append(t.strip())
    open(os.path.join(out, os.path.basename(f)[:-5] + '.txt'), 'w', encoding='utf8').write('\n'.join(paras))
