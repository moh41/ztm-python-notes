import PyPDF2

with open('twopage.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    reader.getPage(0).rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilted.pdf', 'wb') as new_file:
        writer.write(new_file)