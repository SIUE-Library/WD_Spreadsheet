# WD_Spreadsheet
Withdrawal Project spreadsheet processing

Roadmap:
//part 1
convert xls to csv
for each line in csv:
if 2013 < createDate < 2019 OR 2013 < maxOfCharge < 2019 OR 2013 < beginPubDate < 2019 OR 2018 < updateDate < 2019:
add line to _keep.csv
else:
add line to _wd.csv
//part 2
sort _wd.csv file by BIB_ID
for each line in csv:
if csvLine has PO_ID:
add that line to _PO.csv file
else if BIB_ID is equal to the previous BIB_ID or the next BIB_ID
add the line to the _multi.csv file
else:
add the line to _1to1.csv
