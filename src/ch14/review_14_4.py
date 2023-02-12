from pathlib import Path
from pypdf import PdfMerger

files_dir = Path.cwd() / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files"

pdf_merger = PdfMerger()
pdf_merger.append(str(files_dir / "merge1.pdf"))
pdf_merger.append(str(files_dir / "merge2.pdf"))

with Path("src/ch14/concatenated.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)

concat_path = Path.cwd() / "src" / "ch14" / "concatenated.pdf"
merge3_path = files_dir / "merge3.pdf"

pdf_merger = PdfMerger()
pdf_merger.append(str(concat_path))
pdf_merger.merge(1, str(merge3_path))

with Path("src/ch14/merged.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
