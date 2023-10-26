import PyPDF2   # library to merge multiple PDF files into single file

pdfiles = ["sample.pdf","example.pdf"]
Merger = PyPDF2.PdfMerger()   #object is used to combine the individual PDF files into a single merged PDF.

for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        Merger.append(pdfReader)

pdfFile.close()
Merger.write('merged.pdf')
