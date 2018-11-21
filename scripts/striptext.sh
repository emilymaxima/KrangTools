#!bin/bash

for file in *.pdf; do pdftotext "$file" "$file.txt"; done
