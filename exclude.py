import sys
import csv
import json
import re
import string

#takes a record and returns whether that record should be kept (if parameters are appropriate)
def shouldKeep(dict):
    #overloading is used, if string is empty cast will fail so skip that check
    if (dict['CREATE_DATE'] != "" and int(dict['CREATE_DATE'][-2:]) > 12 and int(dict['CREATE_DATE'][-2:]) < 20):
        return True
    if (dict['MaxOfCHARGE_DATE\n'] != "" and int(dict['MaxOfCHARGE_DATE\n'][-2:]) > 12 and int(dict['MaxOfCHARGE_DATE\n'][-2:]) < 20):
        return True
    if (dict['UPDATE_DATE'] != "" and int(dict['UPDATE_DATE'][-2:]) > 17 and int(dict['UPDATE_DATE'][-2:]) < 20):
        return True
    #BEGIN_PUB_DATE may have corrupted format so regex to only match ints so casting doesn't fail
    bpd = re.match(r'[d.]*', dict['BEGIN_PUB_DATE']).group()
    if (bpd != "" and int(bpd) > 12 and int(bpd) < 20):
        return True


if len(sys.argv) < 2:
    print("Usage:\npython3 exclude.py <csv file>")


csvfile = open(sys.argv[1], 'r')

fieldnames = (csvfile.readline().split(','))
reader = csv.DictReader( csvfile, fieldnames)
keep = open(sys.argv[1][:-4]+"_keep.csv", 'w')
keep.write("`".join(fieldnames))
wd =  open(sys.argv[1][:-4]+"_wd.csv", 'w')
wd.write("`".join(fieldnames))

for line in reader:
    if shouldKeep(line):
    #    dict = dict(dict)
        out = ""
        for key in line.keys():
            if key == "ITEM_BARCODE":
                out += '="'+line[key]+'"' + "`"
            else:
                out += str(line[key]) + "`"
        keep.write(out[:-1]+"\n")

    else:
        out = ""
        for key in line.keys():
            if key == "ITEM_BARCODE":
                out += '="'+line[key]+'"' + "`"
            else:
                out += str(line[key]) + "`"
        wd.write(out[:-1]+"\n")
