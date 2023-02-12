from pathlib import Path
from pypdf import PdfReader, PdfWriter
import copy

pdf_path = Path.cwd() / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "half_and_half.pdf"

# pdf_reader = PdfReader(str(pdf_path))
# first_page = pdf_reader.pages[0]
# # first_page.mediabox
# # first_page.mediabox.upper_right
# # first_page.mediabox.upper_left[1]
# first_page.mediabox.upper_left = (0, 480)
#
# pdf_writer = PdfWriter()
# pdf_writer.add_page(first_page)
# with Path("src/ch14/cropped_page.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

first_page = pdf_reader.pages[0]

left_side = copy.deepcopy(first_page)
current_coords = left_side.mediabox.upper_right
new_coords = (current_coords[0] / 2, current_coords[1])
left_side.mediabox.upper_right = new_coords

right_side = copy.deepcopy(first_page)
right_side.mediabox.upper_left = new_coords

pdf_writer.add_page(left_side)
pdf_writer.add_page(right_side)

with Path("src/ch14/cropped_pages.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

