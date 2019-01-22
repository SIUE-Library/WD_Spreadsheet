import sys
import csv
import json
import re
import string
import copy

if len(sys.argv) < 3:
    print("Usage:\npython3 exclude.py <csv file of records to delieneate> <csv file of records to delieneate>")
    sys.exit(1)

csvfile = open(sys.argv[1], 'r')

reader = csv.DictReader( csvfile, delimiter="`", quoting=csv.QUOTE_NONE)

PAS =  open(sys.argv[1][:-4]+"_PAS.tsv", 'w')

PAS_count = 0
PAS_00X =  open(sys.argv[1][:-4]+"_PAS_"+f'{PAS_count:03}'+".tsv", 'w')
n = 0
for line in reader:

    out = str(line["ITEM_BARCODE"])
    PAS.write(out+"\t\n")
    PAS_00X.write(out+"\t\n")
    n += 1
    if n % 500 == 0:
        n = 0
        PAS_00X.close()
        PAS_count += 1
        PAS_00X = open(sys.argv[1][:-4]+"_PAS_"+f'{PAS_count:03}'+".tsv", 'w')


csvfile = open(sys.argv[2], 'r')

reader = csv.DictReader( csvfile, delimiter="`", quoting=csv.QUOTE_NONE)


PAS = open(sys.argv[2][:-4]+"_PAS.tsv", 'w')

PAS_count = 0
PAS_00X =  open(sys.argv[2][:-4]+"_PAS_"+f'{PAS_count:03}'+".tsv", 'w')

MFHD_count = 0
MFHD = open(sys.argv[2][:-4]+"_MFHD.tsv", 'w')
MFHD_00X =  open(sys.argv[2][:-4]+"_MFHD_"+f'{PAS_count:03}'+".tsv", 'w')
MFHD_list = []

BIB_count = 0
BIB = open(sys.argv[2][:-4]+"_BIB.tsv", 'w')
BIB_00X =  open(sys.argv[2][:-4]+"_BIB_"+f'{PAS_count:03}'+".tsv", 'w')
BIB_list = []
n0 = 0
n1 = 0
n2 = 0
for line in reader:

    out = str(line["ITEM_BARCODE"])
    PAS.write(out+"\n")
    PAS_00X.write(out+"\n")
    n0 += 1

    out = str(line["MFHD_ID"])
    if out not in MFHD_list:
        MFHD.write(out+"\n")
        MFHD_00X.write(out+"\n")
        MFHD_list.append(out)
        n1 += 1
        if n1 % 500 == 0:
            n1 = 0
            MFHD_00X.close()

            MFHD_count += 1

            MFHD_00X = open(sys.argv[2][:-4]+"_MFHD_"+f'{MFHD_count:03}'+".tsv", 'w')

    out = str(line["BIB_ID"])
    if out not in BIB_list:
        BIB.write(out+"\n")
        BIB_00X.write(out+"\n")
        BIB_list.append(out)
        n2 += 1
        if n2 % 500 == 0:
            n2 = 0
            BIB_00X.close()

            BIB_count += 1

            BIB_00X = open(sys.argv[2][:-4]+"_BIB_"+f'{BIB_count:03}'+".tsv", 'w')

    if n0 % 500 == 0:
        n0 = 0
        PAS_00X.close()

        PAS_count += 1

        PAS_00X = open(sys.argv[2][:-4]+"_PAS_"+f'{PAS_count:03}'+".tsv", 'w')
