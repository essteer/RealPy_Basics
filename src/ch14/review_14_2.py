from pypdf import PdfReader, PdfWriter
from pathlib import Path

pdf_path = (
    Path.cwd() /
    "python-basics-exercises" /
    "ch14-interact-with-pdf-files" /
    "practice_files" /
    "Pride_and_Prejudice.pdf"
)

input_pdf = PdfReader(str(pdf_path))

# 1
last_page = input_pdf.pages[-1]
pdf_writer = PdfWriter()
pdf_writer.add_page(last_page)

with Path("src/ch14/last_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# 2
pdf_writer = PdfWriter()
for page in input_pdf.pages[::2]:
    pdf_writer.add_page(page)

with Path("src/ch14/every_other_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# 3
pdf_writer = PdfWriter()
for page in input_pdf.pages[:150]:
    pdf_writer.add_page(page)

with Path("src/ch14/part_1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

pdf_writer = PdfWriter()
for page in input_pdf.pages[150:]:
    pdf_writer.add_page(page)

with Path("src/ch14/part_2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
