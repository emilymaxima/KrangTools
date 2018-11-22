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

## movestuff.sh
This script is helpful for moving large volumes of files from one place to another.

## striptext.sh
This script will help rip raw text out of your PDFs. It will dump raw text files out with the same name as the original file.
