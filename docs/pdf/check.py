""" .md ファイルとこれを元に生成された .pdf ファイルのタイムスタンプを比較し、
必要に応じて .md ファイルをブラウザで表示する """

import os
import pathlib

md_dir = pathlib.Path(__file__).parent.parent.resolve()
pdf_dir = md_dir / 'pdf'

md_files = [f for f in os.listdir(md_dir) if f.endswith(".md")]
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

# add README.md file on top directory to the first of md_files
readme_file = 'README.md'
md_files.insert(0, 'README.md')

# Compare the timestamps of the .md files with the corresponding .pdf files
for md_file in md_files:
    if md_file == readme_file:
        md_path = md_dir.parent / readme_file
    else:
        md_path = pathlib.Path(md_dir, md_file)
    pdf_file = md_file[:-3] + ".pdf"  # Generate the corresponding .pdf file name
    if md_file == readme_file:
        pdf_file = "00_" + pdf_file
    pdf_path = pathlib.Path(pdf_dir, pdf_file)

    if not pdf_path.exists():
        print(f"{pdf_file} does not exist for {md_file}")
        os.system(f"start chrome {md_path}")
        continue

    md_timestamp = os.path.getmtime(md_path)
    pdf_timestamp = os.path.getmtime(pdf_path)

    if md_timestamp > pdf_timestamp:
        os.system(f"start chrome {md_path}")
        print(f"{md_file} is newer than {pdf_file}")
