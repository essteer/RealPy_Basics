from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf_path = Path.cwd() / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "ugly.pdf"

# 1 - with knowledge of which pages to rotate
pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for n in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[n]
    if n % 2 == 0:
        page.rotate(90)
    pdf_writer.add_page(page)

with Path("src/ch14/ugly_rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# 2 - without knowledge of which pages to rotate
pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for page in pdf_reader.pages:
    if page["/Rotate"] == -90:
        page.rotate(90)  # could use abs() to counter all rotations
    pdf_writer.add_page(page)

with Path("src/ch14/ugly_rotated2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)



