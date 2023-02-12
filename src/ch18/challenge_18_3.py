import easygui as gui
from pypdf import PdfReader, PdfWriter

# 1 Ask the user to select a PDF file to open.
input_path = gui.fileopenbox(
    title="Select a PDF file to extract pages from",
    default="*.pdf"  # prevents non-PDF files from displaying in the GUI
)
# 2 If no PDF file is chosen, then exit the program.
if input_path is None:
    exit()
# 3 Ask for a starting page number.
start_page = int(gui.enterbox(
    msg="Enter a starting page number:",
    title="Select Start Page"
)) - 1
# 4 If the user doesn't enter a starting page number, then exit the program.
if start_page is None:
    exit()
# 5 Valid page numbers are positive integers. If the user enters an invalid page number:
while start_page < 0:
    # Warn the user that the entry is invalid.
    gui.msgbox(msg="Please enter a valid page number!")
    # Return to step 3.
    start_page = int(gui.enterbox(
        msg="Enter a starting page number:",
        title="Select Start Page"
    )) - 1
    if start_page is None:
        exit()
# 6 Ask for an ending page number.
end_page = int(gui.enterbox(
    msg="Enter an ending page number:",
    title="Select End Page"
))
# 7 If the user doesn't enter an ending page number, then exit the program.
if end_page is None:
    exit()
# 8 If the user enters an invalid page number:
while end_page < start_page:
    # Warn the user that the entry is invalid.
    gui.msgbox(msg="Please enter a valid page number!")
    # Return to step 6.
    end_page = int(gui.enterbox(
        msg="Enter an ending page number:",
        title="Select End Page"
    ))
    if end_page is None:
        exit()
# 9 Ask for the location to save the extracted pages.
save_title = "Save the PDF extract as..."
file_type = "*.pdf"
output_path = gui.filesavebox(title=save_title, default=file_type)
# 10 If the user doesn't select a save location, then exit the program.
if output_path is None:
    exit()
# 11 If the chosen save location is the same as the input file path:
while input_path == output_path:
    # Warn the user that they can't overwrite the input file.
    gui.msgbox(msg="Cannot overwrite original file!")
    # Return to step 9.
    output_path = gui.filesavebox(title=save_title, default=file_type)
    if output_path is None:
        exit()
# 12 Perform the page extraction:
# Open the input PDF file.
input_file = PdfReader(input_path)
output_pdf = PdfWriter()
# Write a new PDF file containing only the pages in the selected page range.
for page in input_file.pages[start_page:end_page]:
    output_pdf.add_page(page)
with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)
