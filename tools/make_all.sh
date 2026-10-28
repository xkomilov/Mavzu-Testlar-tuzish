#!/bin/sh
cd /projects/sandbox/work
for f in savollar/pilot_001_003.txt savollar/b0*.txt; do cat $f; printf '\n\n'; done > savollar/_all.txt
python3 tools/build_tests.py check savollar/_all.txt | head -20 || exit 1
rm -rf out && python3 tools/build_tests.py build savollar/_all.txt src/shablon.xlsx out | tail -1
python3 tools/verify_xlsx.py out/*.xlsx | grep -vc OK
ls out | wc -l
