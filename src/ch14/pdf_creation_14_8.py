from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import blue

canvas = Canvas("hello.pdf")
canvas.drawString("Hello, World")
canvas.save()  # saves to the CWD, RealPy_Basics

# canvas = Canvas("hello.pdf", pagesize=(612.0, 792.0))

# canvas = Canvas("hello.pdf", pagesize=(8.5 * inch, 11 * inch))

# canvas = Canvas("font-example.pdf", pagesize=LETTER)
# canvas.setFont("Times-Roman", 18)
# canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18pt)")
# canvas.save()

canvas = Canvas("font-colors.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 12)
canvas.setFillColor("blue")
canvas.drawString(1*inch, 10*inch, "Blue text")
canvas.save()
