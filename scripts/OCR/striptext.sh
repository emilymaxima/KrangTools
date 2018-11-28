#!/bin/sh

#This one-liner will rip raw text files from PDFs producing a text file with the same name in the same directory
for file in *.pdf; do pdftotext "$file" "$file.txt"; done
