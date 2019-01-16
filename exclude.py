import sys
import csv
import re
import json


if len(sys.argv) < 2:
    print("Usage:\npython3 exclude.py <csv file>")


csvfile = open(sys.argv[1], 'r')


fieldnames = (csvfile.readline().split(','))
reader = csv.DictReader( csvfile, fieldnames)

print(type(reader))

for line in reader:
    print(line['CREATE_DATE'])
