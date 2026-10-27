#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Savollar (oddiy matn) -> shablon.xlsx asosidagi .xlsx yig'uvchi va sifat tekshiruvchi.

Matn formati (savollar/*.txt):
  # 001                 - mavzu raqami (yangi mavzu boshlanadi)
  ? Savol matni
  + To'g'ri javob       (oxirida nuqta qo'yilmaydi)
  - Noto'g'ri javob     (aynan 4 ta)
  ! Qisqa ilmiy izoh    (oxirida nuqta qo'yilmaydi)
  @ M JAW BROCK         (manba kalitlari, SOURCES lug'atidan)

Ishlatilishi:
  python3 build_tests.py check  savollar/batch01.txt
  python3 build_tests.py build  savollar/batch01.txt  shablon.xlsx  Тест2
Aralashtirish: random.Random(mavzu_raqami) - natija qayta qurilganda o'zgarmaydi.
"""
import sys, re, random, zipfile, os, collections
from xml.sax.saxutils import escape

LETTERS = "ABCDE"
MAX_RATIO_WARN = 1.10   # to'g'ri javob eng uzun noto'g'ri javobdan 10 % dan ko'p uzun bo'lmasin
MAX_RATIO_FAIL = 1.30
BAD_START = ("faqat", "hech", "umuman", "barcha")

SOURCES = {
    "M": "Mavzu materiali ({id}.docx)",
    "JAW": "Riedel S. va boshq. Jawetz, Melnick & Adelberg's Medical Microbiology, 28-nashr (2019)",
    "BROCK": "Madigan M.T. va boshq. Brock Biology of Microorganisms, 16-nashr (2021)",
    "WHOLBM": "WHO. Laboratory biosafety manual, 4th ed. (2020)",
    "WOESE": "Woese C.R., Kandler O., Wheelis M.L. (PNAS, 1990)",
    "FLEM": "Fleming A. (Br J Exp Pathol, 1929)",
    "GRAM": "Gram C. (Fortschr Med, 1884)",
    "PETRI": "Petri R.J. (Zentralbl Bakteriol, 1887)",
    "KOCH": "Koch R. (Mitt Kaiserl Gesundheitsamte, 1881)",
    "DOBELL": "Dobell C. Antony van Leeuwenhoek and his 'Little Animals' (1932)",
    "LENS": "Lens on Leeuwenhoek (lensonleeuwenhoek.net) — Visibility",
}


def parse(path):
    topics = collections.OrderedDict()
    cur = None
    q = None
    for ln, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.rstrip("\n").strip()
        if not line:
            continue
        if line.startswith("#"):
            cur = line[1:].strip()
            topics.setdefault(cur, [])
            continue
        tag, _, val = line.partition(" ")
        val = val.strip()
        if tag == "?":
            q = {"q": val, "wrong": [], "line": ln, "src": []}
            topics[cur].append(q)
        elif tag == "+":
            q["correct"] = val
        elif tag == "-":
            q["wrong"].append(val)
        elif tag == "!":
            q["note"] = val
        elif tag == "@":
            q["src"] = val.split()
        else:
            raise SystemExit("%s:%d: noma'lum qator: %r" % (path, ln, line))
    return topics


def letter_sequence(n, rng):
    """Har harf deyarli teng, ketma-ket 3 ta bir xil harf bo'lmaydi."""
    base = []
    order = list(LETTERS)
    rng.shuffle(order)
    while len(base) < n:
        base.extend(order)
        order = list(LETTERS)
        rng.shuffle(order)
    base = base[:n]
    for _ in range(10000):
        rng.shuffle(base)
        if all(not (base[i] == base[i + 1] == base[i + 2]) for i in range(n - 2)):
            return base
    raise RuntimeError("ketma-ketlik topilmadi")


def arrange(tid, items):
    rng = random.Random(int(tid))
    seq = letter_sequence(len(items), rng)
    out = []
    for it, L in zip(items, seq):
        wrong = it["wrong"][:]
        rng.shuffle(wrong)
        opts = []
        wi = 0
        for l in LETTERS:
            if l == L:
                opts.append(it["correct"])
            else:
                opts.append(wrong[wi]); wi += 1
        out.append((it, opts, L))
    return out


def comment(tid, it):
    srcs = "; ".join(SOURCES[k].format(id=tid) for k in it["src"])
    return "To'g'ri javob: %s. %s. Manba: %s." % (it["correct"], it["note"], srcs)


def check(topics, verbose=True):
    problems = []
    tot = collections.Counter()
    over10 = 0
    nq = 0
    for tid, items in topics.items():
        if len(items) < 10:
            problems.append("%s: savollar soni %d < 10" % (tid, len(items)))
        for it in items:
            nq += 1
            w = "%s:%d" % (tid, it["line"])
            if "correct" not in it or len(it["wrong"]) != 4 or "note" not in it or not it["src"]:
                problems.append("%s: to'liq emas (correct/4 wrong/note/src)" % w); continue
            for k in it["src"]:
                if k not in SOURCES: problems.append("%s: noma'lum manba %s" % (w, k))
            if it["correct"].endswith(".") or it["note"].endswith("."):
                problems.append("%s: javob/izoh oxirida nuqta bor (builder o'zi qo'shadi)" % w)
            allopts = [it["correct"]] + it["wrong"]
            if len(set(a.lower() for a in allopts)) != 5:
                problems.append("%s: takroriy javob" % w)
            mx = max(len(x) for x in it["wrong"])
            r = len(it["correct"]) / mx
            if r > MAX_RATIO_FAIL: problems.append("%s: FAIL uzunlik nisbati %.2f" % (w, r))
            elif r > MAX_RATIO_WARN: problems.append("%s: uzunlik nisbati %.2f (>1.10)" % (w, r))
            if r > 1.10: over10 += 1
            nbad = sum(1 for x in it["wrong"] if x.split()[0].lower().strip(",") in BAD_START)
            if nbad > 1: problems.append("%s: %d ta Faqat/Hech/Umuman/Barcha bilan boshlanadi" % (w, nbad))
            fw = collections.Counter(x.split()[0].lower() for x in it["wrong"])
            for word, c in fw.items():
                if c >= 3 and it["correct"].split()[0].lower() != word:
                    problems.append("%s: %d ta noto'g'ri javob '%s' bilan boshlanadi" % (w, c, word))
            if it["correct"].split()[0].lower() in BAD_START:
                problems.append("%s: to'g'ri javob '%s' bilan boshlanadi (ajralib qoladi)" % (w, it["correct"].split()[0]))
        if items and all("correct" in i and len(i["wrong"]) == 4 for i in items):
            arr = arrange(tid, items)
            seq = [L for _, _, L in arr]
            c = collections.Counter(seq); tot.update(c)
            if max(c.values()) - min(c.get(l, 0) for l in LETTERS) > 1:
                problems.append("%s: harf muvozanati buzilgan %s" % (tid, dict(c)))
            for i in range(len(seq) - 2):
                if seq[i] == seq[i + 1] == seq[i + 2]:
                    problems.append("%s: %s harfi 3 marta ketma-ket" % (tid, seq[i]))
    if verbose:
        print("Savollar: %d, mavzular: %d" % (nq, len(topics)))
        print("Harf taqsimoti:", {l: tot.get(l, 0) for l in LETTERS})
        print(">10%% uzun: %d (%.1f%%)" % (over10, 100.0 * over10 / max(nq, 1)))
        print("Muammolar: %d" % len(problems))
        for p in problems: print("  -", p)
    return problems


# ---------------- XLSX ----------------

def build(topics, template, outdir):
    os.makedirs(outdir, exist_ok=True)
    zin = zipfile.ZipFile(template)
    sheet0 = zin.read("xl/worksheets/sheet1.xml").decode("utf-8")
    sst0 = zin.read("xl/sharedStrings.xml").decode("utf-8")
    base_strings = re.findall(r"<si><t[^>]*>(.*?)</t></si>", sst0, flags=re.S)
    for tid, items in topics.items():
        strings = list(base_strings)       # 0..7 shablon sarlavhalari saqlanadi
        index = {s: i for i, s in enumerate(strings)}
        refs = [0]

        def sid(text):
            e = escape(text)
            refs[0] += 1
            if e not in index:
                index[e] = len(strings); strings.append(e)
            return index[e]
        rows = []
        for n, (it, opts, L) in enumerate(arrange(tid, items), start=2):
            vals = [it["q"]] + opts + [L, comment(tid, it)]
            cells = "".join(
                '<c r="%s%d" s="1" t="s"><v>%d</v></c>' % ("ABCDEFGH"[c], n, sid(v)) for c, v in enumerate(vals))
            # ustunlar tartibi shablonda: A Question, B..E variantlar A-D, F variant E, G Correct, H Comment
            rows.append('<row r="%d" spans="1:8">%s</row>' % (n, cells))
        last = len(items) + 1
        sheet = sheet0.replace("</sheetData>", "".join(rows) + "</sheetData>")
        sheet = sheet.replace('<dimension ref="A1:H1"/>', '<dimension ref="A1:H%d"/>' % last)
        total_refs = 8 + refs[0]
        sst = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
               '<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="%d" uniqueCount="%d">%s</sst>'
               % (total_refs, len(strings), "".join('<si><t xml:space="preserve">%s</t></si>' % s for s in strings)))
        outp = os.path.join(outdir, "%s.xlsx" % tid)
        with zipfile.ZipFile(outp, "w", zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = zin.read(info.filename)
                if info.filename == "xl/worksheets/sheet1.xml": data = sheet.encode("utf-8")
                elif info.filename == "xl/sharedStrings.xml": data = sst.encode("utf-8")
                zout.writestr(info.filename, data)
        print("yozildi:", outp, len(items), "savol")


if __name__ == "__main__":
    mode = sys.argv[1]
    topics = parse(sys.argv[2])
    if mode == "check":
        sys.exit(1 if check(topics) else 0)
    elif mode == "build":
        if check(topics): print("Muammolar bor, build to'xtatildi"); sys.exit(1)
        build(topics, sys.argv[3], sys.argv[4])
