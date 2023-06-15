""" .md ファイルを元に生成された .pdf ファイルを結合し、 unittest_resume_all.pdf を生成する """

import os
import pathlib

from PyPDF2 import PdfMerger

# フォルダのパス
folder_path = pathlib.Path(__file__).parent.resolve()

# 結合後のPDFファイル名
merged_filename = 'unittest_resume_all.pdf'

# PDFファイルのリスト
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf') and f != merged_filename]

# PdfFileMergerオブジェクトを作成
merger = PdfMerger()

# すべてのPDFファイルを結合
for pdf_file in pdf_files:
    pdf_path = os.path.join(folder_path, pdf_file)
    merger.append(open(pdf_path, 'rb'))

# 新しいPDFファイルを保存
merged_path = folder_path / merged_filename
with open(merged_path, 'wb') as merged_file:
    merger.write(merged_file)
