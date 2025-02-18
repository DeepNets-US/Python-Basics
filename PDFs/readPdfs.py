import os
from PyPDF2 import PdfReader

# Ensure that path exists
pdf_file_path = "Pride_and_Prejudice.pdf"
if os.path.exists(pdf_file_path):
    print('PDF File Exists\n')

# Specify the path
pdf = PdfReader(pdf_file_path)

print(f'Number of Pages: {pdf.getNumPages()}')

# Extracting Document Information
print(f"Doc Info:")
for key, info in pdf.documentInfo.items():
    print(f'\t{key:20} : {info}')

# Extracting a page's text
page_num = int(input('Enter page number: '))
page = pdf.getPage(page_num)
page_text = page.extractText()
print(f'Text on Page.{page_num}')
print(page_text)


# Loop over Pages
term = 1
for page in pdf.pages:
    print(f'Page.{term}:\n{page}')
    if term>=10:
        break
    term+=1


