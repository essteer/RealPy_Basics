from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf_path = Path.cwd() / "newsletter_protected.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_reader.decrypt(password="SuperSecret")  # Use print() to return 0 / 1 / 2

print(pdf_reader.pages[0])
