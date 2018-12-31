# OCR Scripts

These scripts are for OCR activation and a little bulk file management.

It may seem silly to have scripts that do simple things like moving a certain number of files from one directory to another, but with the volume of files you may be dealing with, your arguments list may be too long for processing.

In order to install system requirements, use the following command:
xargs -rxa requirements.txt -- sudo apt-get install --

In order to use this script, you will need to install the programs inside of requirements.txt

The file structure this works around is as follows:
```
|/root/
-|OCRd
-|foo/
--|OCR.sh
--|<.PDF files to be OCR'd>
```

## OCR.sh
Recommend you use this with tmux, especially if you're processing through a high volume of files, most especially if your files have a high number of pages in them.

## striptext.sh
This script will help rip raw text out of your PDFs. It will dump raw text files out with the same name as the original file.

## OCR_Drive.py
This script supports the Google docs upload method. It's much less resource intensive and much faster per document, but there are things you should take note of before using it:

THIS SCRIPT WILL REPLACE THE ORIGINAL PDF FILE! Make sure you have copies if you want to keep the originals intact!
Be aware that this will only work for documents under 5mb in size and you will need an active network connection to upload and download the pdf files you wish to process.

You will also need to have a google drive api key in order to make this work.

Credit for the singule document processing script goes out to https://tanaikech.github.io/2017/05/02/ocr-using-google-drive-api/
Great thanks to @glitchliz for helping with the failover protections!
