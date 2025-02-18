from pathlib import Path
from PyPDF2 import PdfMerger

# Initialize merger
merger = PdfMerger()

# File Paths of the file to add
paths = list(Path.cwd().glob('?.pdf'))
for path in paths:
    merger.append(path)

# Merge at page num 1
merger.merge(1, paths[-1])

# Write the file
file = open('Merged.pdf', mode='wb')
merger.write(file)
file.close()

