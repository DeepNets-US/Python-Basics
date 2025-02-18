from pathlib import Path
from PyPDF2 import PdfMerger

# Initialize merger
merger = PdfMerger()

# File Paths of the file to add
paths = list(Path.cwd().glob('?.pdf'))

# Append these paths
for path in paths:
    merger.append(path)

# Write the file
file = open('merged.pdf', mode='wb')
merger.write(file)
file.close()

