# Looking Away — the books

One file per building (a book), one file per part.

| File | What it is |
|---|---|
| `building0-blur.tex` → `.pdf` | **Building 0: Blur.** Contents, rules, Part I (Chapters 1–37), Part II (II.1–II.6). |
| `building1-moves.tex` → `.pdf` | **Building 1: Moves.** The algebra path and elliptic curves. Part I (Rearrangements, Words), Part II (move systems, Smith form, actions, Sylow, divisibility, linear maps, similarity, forms, extensions, finite fields, Galois, radicals), Part III (the group law of a cubic, the torus, counts over ℤ/p). |
| `building2-loops.tex` → `.pdf` | **Building 2: Loops.** Part I (Proofs, Equally provable); planned: loops, Amplify, the edge. |
| `rules.tex` | Chapter 0, the rules. Shared by every building. |
| `part1-numbers.tex` | Building 0, Part I: the first floor (map + Chapters 1–37). |
| `part2-systems.tex` | Building 0, Part II: the second floor (map + II.1–II.6). |
| `moves-part1.tex` | Building 1, Part I: moves on things. |
| `moves-part2.tex` | Building 1, Part II: move systems as rows. |
| `moves-part3.tex` | Building 1, Part III: a cubic and its moves. |
| `loops-part1.tex` | Building 2, Part I: words about words. |
| `preamble.tex` | Macros. Use only these. |
| `build.py` | Checks every part and compiles every building: `python3 build.py`. |
| `checks/` | One machine-check script per chapter (`chN-check.py`). |
| `plans/` | `TERRITORIES.md` (current build order), `WORKPLAN.md` (hard rules), `WORKPLAN-2.md` (analysis + complex sketches), `ALGEBRA-PATH.md`; `designs/` chapter designs. |
| `archive/` (shared folder only) | Old one-file-per-chapter sources and retired chapters; not in this repo. |

Adding a chapter: append it to the end of its part file (banner comment, then `\section*`), add its row and tree arrow to the map at the top of that part, add `checks/chN-check.py`, run `python3 build.py`. Never renumber.

New container: `apt-get install -y --no-install-recommends texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended`.

The whole project in a few pages: [PROJECT-SUMMARY.md](PROJECT-SUMMARY.md).
