from PyPDF2 import PdfWriter

# Instantiate a Writer
writer = PdfWriter()

# Add Blank page and set dims
writer.addBlankPage(width=72, height=72)

# Write output to a file
file = open('write.pdf', mode='wb')
writer.write(file)
file.close()

# Adding Pages
from PyPDF2 import PdfReader
pride = PdfReader('./Pride_and_Prejudice.pdf')
with open('write.pdf', mode='wb') as f:
    page = pride.getPage(0)
    writer.addPage(page)

    # Make sure you write the page
    writer.write(f)

print(f'Total No. of Pages: {writer.getNumPages()}')
