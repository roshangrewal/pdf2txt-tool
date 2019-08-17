import PyPDF2
import os
def convertMultiple(pdfdir, txtdir):
    if pdfdir == "": pdfdir = os.getcwd() + "\\" 
    for pdf in os.listdir(pdfdir): 
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfdir + pdf
            PDFFile = PyPDF2.PdfFileReader(pdfFilename)
            for page in range(PDFFile.getNumPages()):
                text = PDFFile.getPage(page).extractText()
                text = text.encode("utf-8")
                print(text)
                textFilename = txtdir + pdf + ".txt"
                textFile = open(textFilename, "wb") 
                textFile.write(text) 
pdfdir = "D:/GitHub/pdf2txt-tool/pdf/"
txtdir = "D:/GitHub/pdf2txt-tool/txt/"
convertMultiple(pdfdir, txtdir)