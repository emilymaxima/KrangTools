#!/bin/sh

for f in *.pdf;
do

# ocrmypdf takes in a filename and can output to a different filename, but this will maintain the same filename through OCR.
# You can change this if you want to though!
  echo "Running OCR on "$f""
  ocrmypdf -v --deskew --clean --clean-final "$f" "$f";

  echo "moving ocr'd file"
#  Make sure this value is changed to fit your destination!
  mv "$f" /root/OCRd

#  echo "removing original file"
#  rm $f

  echo "finished"
done
