---
name: pdf-to-markdown
description: Use this skill whenever the user asks to convert PDF files to markdown format.
---

# PDF to Markdown

This skill converts PDF files into Markdown format using the `pymupdf4llm` library.

## How to use

Run the bundled `scripts/convert.py` script to convert a PDF file to markdown.

### Usage
```bash
python scripts/convert.py "<absolute_path_to_pdf>" ["<absolute_path_to_output_md>"]
```

If you do not provide an output markdown path, the script will create a markdown file in the same directory as the input PDF, with the same base name.

### Dependencies

The script automatically attempts to install `pymupdf4llm` if it is not already installed using `pip`. If it fails, please install it manually via `pip install pymupdf4llm`.
