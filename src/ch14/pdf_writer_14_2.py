from pypdf import PdfWriter, PdfReader
from pathlib import Path

# Writing a blank PDF page
pdf_writer = PdfWriter()
pdf_writer.add_blank_page(width=72, height=72)
with Path("src/ch14/blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# Extracting a single page from a PDF
pdf_path = (
    Path.cwd() /
    "python-basics-exercises" /
    "ch14-interact-with-pdf-files" /
    "practice_files" /
    "Pride_and_Prejudice.pdf"
)

input_pdf = PdfReader(str(pdf_path))
first_page = input_pdf.pages[0]

pdf_writer = PdfWriter()
pdf_writer.add_page(first_page)

with Path("src/ch14/first_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# Extracting multiple pages from a PDF
pdf_path = (
    Path.cwd() /
    "python-basics-exercises" /
    "ch14-interact-with-pdf-files" /
    "practice_files" /
    "Pride_and_Prejudice.pdf"
)

input_pdf = PdfReader(str(pdf_path))

# with loop
pdf_writer = PdfWriter()
for n in range(1, 4):
    page = input_pdf.pages[n]  # replaces "input_pdf.getPage(n)"
    pdf_writer.add_page(page)

len(pdf_writer.pages)  # replaces "pdf_writer.getNumPages()"

with Path("src/ch14/chapter1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# with slice
pdf_writer = PdfWriter()
for page in input_pdf.pages[1:4]:
    pdf_writer.add_page(page)

with Path("src/ch14/chapter1_slice.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
