from PyPDF2 import PdfReader, PdfWriter

in_path, out_path = './1.pdf', './1_c.pdf'


# Read the pdf
reader = PdfReader(in_path)

# Crop
print('OG Shape: ', reader.getPage(0).mediaBox.upperRight)

# New Shape
shape = reader.getPage(0).mediaBox.upperRight[0]//2, reader.getPage(0).mediaBox.upperRight[1]//2

reader.getPage(0).mediaBox.upperRight = shape
print('New Shape: ', reader.getPage(0).mediaBox.upperRight)

# Write to new filw
with open(out_path, mode='wb') as f:
    writer = PdfWriter()
    writer.addPage(reader.getPage(0))
    writer.write(f)
