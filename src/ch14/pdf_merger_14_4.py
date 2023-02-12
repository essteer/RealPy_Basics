from pathlib import Path
from pypdf import PdfMerger

# 1 - .append()
reports_dir = Path.cwd() / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "expense_reports"

# Print the names of the target PDF files
for path in reports_dir.glob("*.pdf"):
    print(path.name)
# This seems to now print them in name order - PyPDF2 did not
# the next lines of code may not be relevant to pypdf
expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()


pdf_merger = PdfMerger()
for path in expense_reports:
    pdf_merger.append(str(path))

with Path("src/ch14/expense_reports.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)

# 2 - .merge()
reports_dir = Path.cwd() / "python-basics-exercises" / "ch14-interact-with-pdf-files" / "practice_files" / "quarterly_report"

report_path = reports_dir / "report.pdf"
toc_path = reports_dir / "toc.pdf"

pdf_merger = PdfMerger()
pdf_merger.append(str(report_path))
pdf_merger.merge(1, str(toc_path))

with Path("src/ch14/full_report.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)



