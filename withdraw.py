import sys
import csv
import json
import re
import string
import copy



def isNotUnique(word, master):
    n = 0
    #count how many records have that BIB_ID
    for line in master:
        if word["BIB_ID"] is line["BIB_ID"]:
            n += 1
    #if more than one record does, Item is not Unique
    if n > 1:
        return True
    else:
        return False

if len(sys.argv) < 2:
    print("Usage:\npython3 exclude.py <csv file of records to withdraw>")


csvfile = open(sys.argv[1], 'r')

fieldnames = (csvfile.readline().split('`'))
reader = csv.DictReader( csvfile, fieldnames, delimiter="`", quoting=csv.QUOTE_NONE)
n = 0
print(n)
for line in reader:
    n += 1
    print(n)
    if line["PO_ID"] != "":
        print("po")  #add to _PO.csvfile
    elif isNotUnique(line, reader):
        print("multi")
    else:
        print("1to1")
