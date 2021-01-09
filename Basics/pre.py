import PyPDF2

# creating a pdf file object
path = '/Users/ishwarjangid/Desktop/CA for 2021 /Test Series/Test 1.pdf'
path = path.encode('UTF-8')
pdfFileObj = open(path, 'r')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
a = pdfReader.numPages

# creating a page object

print(a)
# extracting text from page
for i in range(1):
    pageObj = pdfReader.getPage(22)
    try:
        text = pageObj.extractText()
        print(text[1:23])
        print("this is text of", pageObj)
        if "VISIONIAS" in text:
            print(text)

    except:
        continue


pdfFileObj.close()
