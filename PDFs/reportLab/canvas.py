from reportlab.pdfgen.canvas import Canvas

canvas = Canvas('learn.pdf')

# Add data
canvas.drawString(72, 72, 'Hello World!')

# Save the File
canvas.save()
