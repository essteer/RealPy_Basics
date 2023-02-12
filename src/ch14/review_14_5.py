from pathlib import Path
from pypdf import PdfReader, PdfWriter
import copy

# 1
pdf_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "split_and_rotate.pdf"
cwd_path = Path.cwd()

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for page in pdf_reader.pages:
    page.rotate(-90)
    pdf_writer.add_page(page)

with Path(cwd_path / "rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# 2
pdf_path = Path.cwd() / "rotated.pdf"
pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for page in pdf_reader.pages:
    left_side = copy.deepcopy(page)
    current_coords = left_side.mediabox.upper_right
    new_coords = (current_coords[0] / 2, current_coords[1])
    left_side.mediabox.upper_right = new_coords
    right_side = copy.deepcopy(page)
    right_side.mediabox.upper_left = new_coords
    pdf_writer.add_page(left_side)
    pdf_writer.add_page(right_side)

with Path("split.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
