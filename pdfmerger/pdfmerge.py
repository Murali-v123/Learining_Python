import os

from pypdf import PdfWriter

merger = PdfWriter()

list = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in list:
    merger.append(pdf)
# merger.append("1.pdf")
# merger.append("2.pdf")
merger.write("merged-pdf.pdf")

merger.close()
