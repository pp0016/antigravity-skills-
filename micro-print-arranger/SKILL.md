---
name: micro-print-arranger
description: >-
  Arranges a PDF for duplex micro-printing (4-up) so cut-out pieces have correct
  front-back pairs. Triggers on /micro-print or /micro-print-arranger.
  MUST activate when the user mentions: micro print, micro printing, 4-up print,
  4-up duplex, arrange pages for printing, duplex cut print, front back page arrange,
  chote pages print, chhota print, micro me print, aage peeche page set karna,
  cut out print, print and cut, micro nikalwana, or provides PDF files and asks
  to arrange them for micro/duplex/4-up printing.
---

# Micro Print Arranger Skill

Rearranges pages in a PDF so it can be printed in **micro-print mode** (4 pages per A4 sheet, duplex). After cutting the printed sheet into 4 pieces, each piece has the correct front-back page pair (e.g., Page 1 front → Page 2 back). Leftover padding slots get an explicit **"ERROR (Extra Padding Page)"** so printers don't skip them.

## How It Works

For each group of 8 pages (long-edge flip):

| | TL | TR | BL | BR |
|---|---|---|---|---|
| **FRONT** | N | N+2 | N+4 | N+6 |
| **BACK** | N+3 | N+1 | N+7 | N+5 |

Supports any page count (auto-pads to multiples of 8) and both long-edge and short-edge duplex flip.

## Script Location

The Python script is at: `scripts/micro_print_arranger.py` (relative to this SKILL.md).

Absolute path: `C:\Users\renu5\.gemini\config\skills\micro-print-arranger\scripts\micro_print_arranger.py`

## Dependencies

The script requires `PyPDF2` and `reportlab`. A dedicated venv already exists at:
`C:\Users\renu5\.gemini\antigravity\scratch\micro-print-env`

If the venv doesn't exist or is broken, recreate it:
```powershell
python -m venv C:\Users\renu5\.gemini\antigravity\scratch\micro-print-env
C:\Users\renu5\.gemini\antigravity\scratch\micro-print-env\Scripts\python.exe -m pip install PyPDF2 reportlab
```

## Execution

> [!IMPORTANT]
> Always set `$env:PYTHONIOENCODING='utf-8'` on Windows to avoid Unicode errors.
> Always use the venv python, NOT the global python.

### Single PDF:
```powershell
$env:PYTHONIOENCODING='utf-8'; C:\Users\renu5\.gemini\antigravity\scratch\micro-print-env\Scripts\python.exe "C:\Users\renu5\.gemini\config\skills\micro-print-arranger\scripts\micro_print_arranger.py" "C:\path\to\input.pdf"
```

### Multiple PDFs:
Run the command once for **each** PDF file the user provides. Do NOT batch them — the script takes one input at a time.

### Options:
- `--flip short` — Use short-edge (notepad-style) duplex flip instead of default long-edge
- `--order-only N` — Just display the page order table for N pages (no PDF generated)

### Output:
The script creates `<original_name>_microprint.pdf` in the **same directory** as the input file.

## Post-Execution

After running, tell the user:
1. The output file path(s)
2. These printing instructions:
   - Open the `_microprint.pdf` file
   - Print → **Multiple pages per sheet / 4-up** (2×2 layout)
   - Page order: **Left to Right, Top to Bottom**
   - Duplex: **ON (Long Edge)** — or Short Edge if `--flip short` was used
   - Print ALL pages
   - Cut each sheet into 4 pieces
   - Each piece will have correct front-back pages
