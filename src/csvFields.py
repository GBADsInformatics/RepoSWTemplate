#
#   Extract unique values for a field in a CSV file and sort the list
#
#   Author: Deb Stacey
#   Usage: python3 csvFields.py <csv filename> <field number starting at 1>
#
#   Date of last update: October 28, 2024
#
# Libraries
import sys
import csv

file_name = sys.argv[1]
num = int(sys.argv[2]) - 1
if num < 0:
    print ( "Improper column number (",num+1,")" )
    exit ( -1 )

colfield = []
with open ( file_name, encoding='ISO-8859-1' ) as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        num_cols = len(row)
        if num >= num_cols:
            print ( "There are only ",num_cols," columns" )
            exit ( -1 )
        else:
            colfield.append(row[num])
    setA = set(colfield)
    uniqList = list(setA)
    uniqList.sort()
    total = len(uniqList)
    print ( "There are ",total," unique values in column ",num )
    i = 0
    while i < total:
        print ( uniqList[i] )
        i = i + 1
