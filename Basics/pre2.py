
from io import StringIO
import re
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


def convert_pdf_to_txt(path, page_no):
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

        for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
           # print(pageNumber)
            if pageNumber == page_no:
                interpreter.process_page(page)
                data = retstr.getvalue()
                # print(data)
        #data = ""
        retstr.truncate(0)
        retstr.seek(0)
    fp.close()
    device.close()

    str = retstr.getvalue()
    retstr.close()
    return data


a = convert_pdf_to_txt(path, 0)

ANSWER = 24
TOTAL = 56
list_of_answers = []
# for a in range(ANSWER - 1, 53):
#     a = convert_pdf_to_txt(path, a)
#     b = a.split("Q ")
#     list_of_answers.append(b[1][2])
#     c = b[2].split(".Q")

#     list_of_answers.append(c[0][2])
#     print(list_of_answers)

for a in range(ANSWER - 1, 28):
    a = convert_pdf_to_txt(path, a)
    a = re.split('Q [0-9].', a)

    for i in a:
        print("---------------------")
        list_of_answers.append(i[0:3])

    print(list_of_answers)

   # print(len(b))
   # print(a)
