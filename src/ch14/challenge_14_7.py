from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "scrambled.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

page_dict = {}

for page in pdf_reader.pages:
    if page["/Rotate"] != 0:
        page.rotate(360 - page["/Rotate"])
    page_num = page.extract_text()
    page_dict[int(page_num)] = page

for n in range(1, 8):
    pdf_writer.add_page(page_dict[n])

with Path("unscrambled.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
