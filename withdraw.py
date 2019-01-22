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
    #    print(line)
        if word["BIB_ID"] == line["BIB_ID"]:
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
reader = csv.reader( csvfile, fieldnames, delimiter="`", quoting=csv.QUOTE_NONE)

records = []


po =  open(sys.argv[1][:-4]+"_PO.csv", 'w')
po.write("`".join(fieldnames))

to1 =  open(sys.argv[1][:-4]+"_1to1.csv", 'w')
to1.write("`".join(fieldnames))

mult =  open(sys.argv[1][:-4]+"_multi.csv", 'w')
mult.write("`".join(fieldnames))


for new in reader:
    records.append(dict(zip(fieldnames, new)))

for n, line in enumerate(records):
    if line["PO_ID"] != "":
        out = ""
        for key in line.keys():
            out += str(line[key]) + "`"
        po.write(out[:-1]+"\n")
    elif isNotUnique(line, records):
        out = ""
        for key in line.keys():
            out += str(line[key]) + "`"
        to1.write(out[:-1]+"\n")
    else:
        out = ""
        for key in line.keys():
            out += str(line[key]) + "`"
        mult.write(out[:-1]+"\n")

print("Finished")
