from pypdf import PdfReader
from pathlib import Path

pdf_path = (Path.home() /
            "code" /
            "projects" /
            "realpy_basics" /
            "python-basics-exercises" /
            "ch14-interact-with-pdf-files" /
            "practice_files" /
            "zen.pdf"
            )
# 1
pdf_reader = PdfReader(str(pdf_path))

# 2
print(len(pdf_reader.pages))

# 3
first_page = pdf_reader.pages[0]
print(first_page.extract_text())
