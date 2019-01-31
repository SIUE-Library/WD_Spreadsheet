import sys
import csv
import json
import re
import string

#takes a record and returns whether that record should be kept (if parameters are appropriate)
def shouldKeep(dict):
    #overloading is used, if string is empty cast will fail so skip that check
    cd = re.match(r'(\d+/\d+/\d+)', dict['CREATE_DATE'])
    mocd = re.match(r'(\d+\/\d+\/\d+)', dict['MaxOfCHARGE_DATE\n'])
    ud = re.match(r'(\d+\/\d+\/\d+)', dict['UPDATE_DATE'])

    if cd != None:
        cd = cd.group()[-4:]

    if mocd != None:
        mocd = mocd.group()[-4:]

    if ud != None:
        ud = ud.group()[-4:]

    if (cd != None and int(cd) > 2012 and int(cd) < 2020):
        return True

    if (mocd != None and int(mocd) > 2012 and int(mocd) < 2020):
        return True

    if (ud != None and int(ud) > 2017 and int(ud) < 2020):
        return True

    #BEGIN_PUB_DATE may have corrupted format so regex to only match ints so casting doesn't fail
    #I've only seen this in the form YYYY or garbled
    bpd = re.match(r'[d.]*', dict['BEGIN_PUB_DATE']).group()
    if (bpd != "" and int(bpd) > 2012 and int(bpd) < 2020):
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
