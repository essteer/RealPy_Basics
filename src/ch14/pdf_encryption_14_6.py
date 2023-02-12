from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "newsletter.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

pdf_writer.append_pages_from_reader(pdf_reader)

user_pwd = "SuperSecret"
owner_pwd = "ReallySuperSecret"
pdf_writer.encrypt(user_password=user_pwd, owner_password=owner_pwd)

output_path = Path.cwd() / "newsletter_protected.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)

