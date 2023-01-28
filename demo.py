from PyPDF2 import PdfMerger

l = ['sample.pdf', 'free.pdf']

merger = PdfMerger()


for i in l:
    merger.append(i)

merger.write("result.pdf")
merger.close()

