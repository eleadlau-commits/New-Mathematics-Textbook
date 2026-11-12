"""Check and compile the books.  Usage:  python3 build.py [--no-pdf]   (run from textbook/)

Layout: one file per building (a book) and one file per part.
  building0-blur.tex   = preamble + contents + rules.tex + part1-numbers.tex + part2-systems.tex
  building1-moves.tex, building2-loops.tex  (stubs until their first chapter)
  rules.tex            = Chapter 0, shared by every building
To add a chapter: append it to the end of its part file, starting with a banner and \\section*.
Check scripts live in checks/, plans and designs in plans/.
"""
import re, sys, os, shutil, subprocess
here = os.path.dirname(os.path.abspath(__file__))
BUILDINGS = ['building0-blur', 'building1-moves', 'building2-loops']
PARTS = ['rules', 'part1-numbers', 'part2-systems', 'part3-regions', 'moves-part1', 'moves-part2', 'moves-part3', 'loops-part1', 'loops-part2']
rd = lambda f: open(os.path.join(here, f + '.tex')).read()
pre = rd('preamble')
bad = 0

def chapters(text):
    """Split a part file at each \\section* (one chunk per chapter)."""
    pieces = re.split(r'(?=^\\section\*\{)', text, flags=re.M)
    return [p for p in pieces if p.startswith('\\section*')]

def code_of(t):
    return "\n".join(l for l in t.split("\n") if not l.lstrip().startswith('%'))

for f in PARTS:
    t = rd(f)
    probs = []
    code = code_of(t)
    if code.count('{') != code.count('}'): probs.append("braces %+d" % (code.count('{') - code.count('}')))
    if len(re.findall(r'\\begin\{', code)) != len(re.findall(r'\\end\{', code)): probs.append("begin/end")
    for ch in chapters(code):
        name = re.match(r'\\section\*\{([^}]*)\}', ch).group(1)
        cp = []
        if ch.count('$') % 2: cp.append("odd number of $")
        if 'addcontentsline' not in ch: cp.append("no contents entry")
        labs = re.findall(r'\\item\[\\lab\{([^}]+)\}\]', ch)
        dup = sorted({x for x in labs if labs.count(x) > 1 and not re.fullmatch(r'[Aa]\d|d\d', x)})
        if dup: cp.append("duplicate labels " + ",".join(dup))
        # floor one never cites floor two outside Remarks (rule F7)
        if f == 'part1-numbers' and not name.startswith('The map'):
            for i, l in enumerate(ch.split("\n"), 1):
                if re.search(r'\bII\.\d', l) and not re.search(r'\\lab\{R\d', l):
                    cp.append("line %d cites Part II outside a Remark" % i)
        # Building 0 never relies on Buildings 1, 2 outside Remarks
        if f in ('part1-numbers', 'part2-systems'):
            for i, l in enumerate(ch.split("\n"), 1):
                if re.search(r'Building [12]', l) and not re.search(r'\\lab\{R\d', l):
                    cp.append("line %d cites Building 1/2 outside a Remark" % i)
        if cp: probs.append(name + ": " + "; ".join(cp))
    if probs: bad += 1
    print("%-18s %d chapters  %s" % (f, len(chapters(code)) or 1, "; ".join(probs) if probs else "ok"))

if shutil.which('pdflatex') and '--no-pdf' not in sys.argv:
    for b in BUILDINGS:
        for _ in range(2):
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', b + '.tex'],
                               cwd=here, capture_output=True, text=True)
        log = open(os.path.join(here, b + '.log'), errors='replace').read()
        errs = log.count('\n! ')
        over = [l for l in log.split('\n') if l.startswith('Overfull') and float(l.split('(')[1].split('pt')[0]) > 10]
        pages = re.search(r'Output written on .*?\((\d+) page', log)
        print("%-18s pdflatex %s, %d errors, %d lines >10pt too wide, %s pages -> %s.pdf" % (
            b, "ok" if r.returncode == 0 else "FAILED", errs, len(over), pages.group(1) if pages else "?", b))
        for l in over: print("   ", l)
        if r.returncode != 0 or errs: bad += 1
        for ext in ('aux', 'log', 'out', 'toc'):
            p = os.path.join(here, b + '.' + ext)
            if os.path.exists(p) and ext != 'log' or (ext == 'log' and r.returncode == 0 and not errs and os.path.exists(p)):
                os.remove(p)
else:
    print("No pdflatex here (or --no-pdf): NOT compiled.")
sys.exit(1 if bad else 0)
