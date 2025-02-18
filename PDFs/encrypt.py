from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('./1.pdf')
writer = PdfWriter()
writer.appendPagesFromReader(reader)
writer.encrypt(user_pwd='secret')
writer.write(open('./1_encrypted.pdf', mode='wb'))

