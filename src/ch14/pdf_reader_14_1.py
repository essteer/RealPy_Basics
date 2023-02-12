from pypdf import PdfReader  # with 3.0 (pypdf), several changes made since PyPDF2
from pathlib import Path

pdf_path = (Path.cwd() /
            "python-basics-exercises" /
            "ch14-interact-with-pdf-files" /
            "practice_files" /
            "Pride_and_Prejudice.pdf"
            )

pdf = PdfReader(str(pdf_path))

# pdf.getNumPages() was replaced with len(reader.pages)
len(pdf.pages)

# pdf.documentInfo was replaced with reader.metadata
# pdf.metadata
# pdf.metadata.title

# pdf.getPage() was replaced with pdf.pages[page_number]
first_page = pdf.pages[0]
# pdf.extractText() was replaced with extract_text
first_page.extract_text()

# to print the text from all pages:
# for page in pdf.pages:
#     print(page.extract_text)
