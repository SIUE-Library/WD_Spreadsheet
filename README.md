# WD_Spreadsheet
Withdrawal Project spreadsheet processing

## IO
Input must be in csv format.  On Linux with LibreOffice Headless xlsx files can be converted to csv by running:<br>
libreoffice --headless --invisible --convert-to csv <input.xlsx> --outdir <place to put xlsx>
<br><br>
Similarly, output will be in csv that can be converted back to xlsx with:<br>
libreoffice --headless --invisible --convert-to xlsx <input.csv> --outdir <place to put xlsx>
<br><br>
Alternatively, you can open the csv in excel, libreoffice, google sheets, or other spreadsheet software and export/save as a .csv to convert, and then open the open a csv file in excel and save as xlsx to convert back.
<br>
Its important the the csv file put into the software is encoded in UTF-8, not ISO-8859-14 or any other ISO.  Csv files exported from excel should be in UTF-8 as long as you open the file in UTF-8 mode, but if you used the libreoffice headless method you should be able to convert to UTF-8 with the command:<br>
iconv -f <current encoding, usually ISO-8859-14> -t UTF-8 <input file> -o <output file, must be different from input file name>
<br>
You can find the encoding of a file with the command:
file <filename>
<br><br>

# Quick Start
To process to just the withdraw and keep list, run exclude.py, passing as input the csv file to check.  This will output two intermediate backtick-delineated text files.  Convert these files to csv one at a time by running unBacktick.py, passing the files as an argument.  These files can be loaded in as additional sheets of the original master.xlsx manually.


## Execution
There are four python files that perform the data transformations.  All are made for python3<br><br>
exclude.py should be passed as a command line argument the aastx_?\_master.csv file where ? is the letter you want processed.  The required headers in this csv file are: CREATE_DATE, MaxOfCHARGE_DATE, UPDATE_DATE, BEGIN_PUB_DATE, and ITEM_BARCODE.  The order of these does not matter, nor does it matter if there are any other columns.  The output of this will be two backtick (\`) delineated text files, one containing all of the withdraw items (\_wd) and one containing all keep files (\_keep).
<br><br>

withdraw.py takes as command line input a list of withdraw items delineated by backticks, such as the \_wd file output by exclude.py.  Required headers in this file are PO_ID and BIB_ID.  This program will sort the data into three additional file (\_PO, \_1to1, and \_multi) based on the following conditions:
\_PO will contain all of the records/rows from the \_wd spreadsheet that have values in PO_ID column<br>
\_1to1 will contain all of the records/rows from the \_wd spreadsheet that meet the following criteria:
    • Does not have a value in PO_ID
    • Does not have a BIB_ID that has a duplicate value within their column. This means that there will be no duplicate values in the BIB_ID, MFHD_ID, or ITEM_ID columns.
\_multi will contain all of the records/rows from the \_wd spreadsheet that meet the following criteria:
    • Does not have a value in PO_ID
    • Contains a duplicate value in BIB_ID
Like exclude.py, the output of this will be backtick delineated text files.
<br><br>

tabDelineate.py takes two files and input, the \_1to1 list and the \_multi list.  From the 1to1 it puts all of the ITEM_BARCODEs in a single text file list.  It will also output a set of text files with the barcodes split into sections of 500.  ITEM_BARCODE is the only required header in this input file.
<br><br>

As you may have noticed, all of these files output backtick (\`) delineated files rather than csv.  The unBacktick.py file may be used to convert these to csv.  This file takes no arguments but looks at all files in all subfolders in the aastx/ folder.  All such files are parsed in and converted to proper csv.  This overwrites the original files.  This script may fail if there are any files in the aastx/ folder, and may also fail if any of the files in the subfolders don't match the correct format.
