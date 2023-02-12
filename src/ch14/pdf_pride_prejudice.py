from pypdf import PdfReader
from pathlib import Path

pdf_path = (Path.home() /
            "code" /
            "projects" /
            "realpy_basics" /
            "python-basics-exercises" /
            "ch14-interact-with-pdf-files" /
            "practice_files" /
            "Pride_and_Prejudice.pdf"
            )

# 1
pdf_reader = PdfReader(str(pdf_path))
output_file_path = Path.cwd() / "Pride_and_Prejudice.txt"

# 2
with output_file_path.open(mode="w") as output_file:
    # 3
    title = pdf_reader.metadata.title
    num_pages = len(pdf_reader.pages)
    output_file.write(f"{title}\nNumber of pages: {num_pages}\n\n")

    # 4
    for page in pdf_reader.pages:
        text = page.extract_text()
        output_file.write(text)

