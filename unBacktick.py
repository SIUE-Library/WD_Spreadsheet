import csv
import sys
from os import listdir

listOfFiles = []

if len(sys.argv) < 2:
    print("Usage:\npython3 exclude.py <file>")

fullPath = sys.argv[1]
# read tab-delimited file (from https://stackoverflow.com/questions/29759305/how-do-i-convert-a-tsv-to-csv)
with open(fullPath,'r') as fin:
    cr = csv.reader(fin, delimiter='`')
    filecontents = [line for line in cr]

# write comma-delimited file (comma is the default delimiter) (from https://stackoverflow.com/questions/29759305/how-do-i-convert-a-tsv-to-csv)
with open(fullPath,'w') as fou:
    cw = csv.writer(fou)
    cw.writerows(filecontents)
