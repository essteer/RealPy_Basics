from pathlib import Path
from pypdf import PdfReader, PdfWriter

#1
pdf_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "top_secret.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

pdf_writer.append_pages_from_reader(pdf_reader)
pdf_writer.encrypt(user_password="Unguessable")

output_path = Path.cwd() / "top_secret_encrypted.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# 2
pdf_path = Path.cwd() / "top_secret_encrypted.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_reader.decrypt(password="Unguessable")

first_page = pdf_reader.pages[0]

print(first_page.extract_text())
