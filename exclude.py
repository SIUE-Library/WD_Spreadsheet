import sys
import csv
import json
import re
import string

#takes a record and returns whether that record should be kept (if parameters are appropriate)
def shouldKeep(dict):
    #overloading is used, if string is empty cast will fail so skip that check
    if (line['CREATE_DATE'] != "" and int(line['CREATE_DATE'][-2:]) > 12 and int(line['CREATE_DATE'][-2:]) < 20):
        return True
    if (line['MaxOfCHARGE_DATE\n'] != "" and int(line['MaxOfCHARGE_DATE\n'][-2:]) > 12 and int(line['MaxOfCHARGE_DATE\n'][-2:]) < 20):
        return True
    if (line['UPDATE_DATE'] != "" and int(line['UPDATE_DATE'][-2:]) > 17 and int(line['UPDATE_DATE'][-2:]) < 20):
        return True
    #BEGIN_PUB_DATE may have corrupted format so regex to only match ints so casting doesn't fail
    bpd = re.match(r'[d.]*', line['BEGIN_PUB_DATE']).group()
    if (bpd != "" and int(bpd) > 12 and int(bpd) < 20):
        return True


if len(sys.argv) < 2:
    print("Usage:\npython3 exclude.py <csv file>")


csvfile = open(sys.argv[1], 'r')

fieldnames = (csvfile.readline().split(','))
reader = csv.DictReader( csvfile, fieldnames)
keep = open(sys.argv[1][:-4]+"_keep.csv", 'w')
keep.write(",".join(fieldnames))
wd =  open(sys.argv[1][:-4]+"_wd.csv", 'w')
for line in reader:
    if shouldKeep(line):
    #    line = dict(line)
        out = ""
        for key in line.keys():
            out += str(line[key]) + ","
        keep.write(out[:-1]+"\n")

    else:
        out = ""
        for key in line.keys():
            out += str(line[key]) + ","
        wd.write(out[:-1]+"\n")
