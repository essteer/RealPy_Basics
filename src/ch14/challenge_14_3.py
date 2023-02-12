from pathlib import Path
from pypdf import PdfReader, PdfWriter

class PdfSplitter:
    """Receives an instance of a PDF file.
    Creates two PDF files separated at a predetermined page number."""
    def __init__(self, path_string):
        self.path_string = path_string
        self.pdf_path = Path.cwd() / self.path_string
        self.pdf_reader = PdfReader(str(self.pdf_path))
        self.writer1 = PdfWriter()
        self.writer2 = PdfWriter()

    def split(self, split_point):
        """Divides pages according to the split point and
        adds them to the writer1 and writer2 PdfWriter instances."""
        for page in self.pdf_reader.pages[:split_point]:
            self.writer1.add_page(page)
        for page in self.pdf_reader.pages[split_point:]:
            self.writer2.add_page(page)

    def write(self, filename="New_PDF"):
        """"""
        filename1 = filename + "_1.pdf"
        filename2 = filename + "_2.pdf"
        with Path(filename1).open(mode="wb") as output_file:
            self.writer1.write(output_file)
        with Path(filename2).open(mode="wb") as output_file:
            self.writer2.write(output_file)


pdf_splitter = PdfSplitter("The Emperor.pdf")
pdf_splitter.split(3)
pdf_splitter.write("The_Emperor_split")
