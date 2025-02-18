from PyPDF2 import PdfReader as PdfR, PdfWriter as PdfW

in_path, out_path = './1.pdf', '1_r.pdf'

# Read and Rotate a file
reader = PdfR(in_path)
reader.getPage(0).rotateClockwise(90)

# Write the file
with open(out_path, mode='wb') as f:
    writer = PdfW()
    writer.addPage(reader.getPage(0))
    writer.write(f)
