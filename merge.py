import PyPDF2
import sys
import os

mergeIT = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print("Merging " + file)
        mergeIT.append(file)
    mergeIT.write("merged.pdf")
