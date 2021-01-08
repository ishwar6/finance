import PyPDF2

# creating a pdf file object
path = '/Users/ishwarjangid/Desktop/CA for 2021 /Test Series/Test 1.pdf'
pdfFileObj = open(path, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
a = pdfReader.numPages

# creating a page object
pageObj = pdfReader.getPage(0)
print(type(pageObj))

# extracting text from page
for i in range(a):
    pageObj = pdfReader.getPage(0)


# print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
