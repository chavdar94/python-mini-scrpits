from pdf2docx import parse


# path to pdf file
pdf_file = ''
# path to word file
docx_file = ''

try:
    parse(pdf_file, docx_file)
except:
    print('Conversion failed')
