import csv
from os import listdir

listOfFiles = []

for each in listdir("aastx"):
    header = "aastx/"+each+"/"
    for file in listdir(header):
        fullPath = header+file
        # read tab-delimited file (from https://stackoverflow.com/questions/29759305/how-do-i-convert-a-tsv-to-csv)
        with open(fullPath,'r') as fin:
            cr = csv.reader(fin, delimiter='`')
            filecontents = [line for line in cr]

        # write comma-delimited file (comma is the default delimiter) (from https://stackoverflow.com/questions/29759305/how-do-i-convert-a-tsv-to-csv)
        with open(fullPath,'w') as fou:
            cw = csv.writer(fou)
            cw.writerows(filecontents)
