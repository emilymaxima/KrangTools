#!/bin/sh

for f in *.pdf;
do
  echo "Running OCR on "$f""
  ocrmypdf -v --deskew --clean --clean-final "$f" "$f";

  echo "moving ocr'd file"
#  Make sure this value is changed to fit your destination!
  mv "$f" /root/OCRd

  echo "finished"
done
