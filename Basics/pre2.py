
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
path = '/Users/ishwarjangid/Desktop/CA for 2021 /Test Series/Test 1.pdf'

# output_string = StringIO()
# with open(path, 'rb') as in_file:
#     parser = PDFParser(in_file)
#     doc = PDFDocument(parser)
#     rsrcmgr = PDFResourceManager()
#     device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
#     interpreter = PDFPageInterpreter(rsrcmgr, device)

#     for page in PDFPage.create_pages(doc):
#         # print(page.__dict__)
#         interpreter.process_page(page)

# print(output_string.getvalue())
# A list for all each page's text
pages_text = []

# for page in PDFPage.get_pages(pdf):
#     # Get (and store) the "cursor" position of stream before reading from PDF
#     # On the first page, this will be zero
#     read_position = retstr.tell()

#     # Read PDF page, write text into stream
#     interpreter.process_page(page)

#     # Move the "cursor" to the position stored
#     retstr.seek(read_position, 0)

#     # Read the text (from the "cursor" to the end)
#     page_text = retstr.read()

#     # Add this page's text to a convenient list
#     pages_text.append(page_text)


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    with open(path, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            # print(page)
            interpreter.process_page(page)
            break
    fp.close()
    device.close()

    str = retstr.getvalue()
    retstr.close()
    return str


a = convert_pdf_to_txt(path)

print(len(a))
