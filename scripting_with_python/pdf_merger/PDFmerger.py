# Program that merges PDF files into an output file
# Terminal arguments: python PDFmerger.py [input_file_1] [input_file_2] ... [input_file_n]
import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)
