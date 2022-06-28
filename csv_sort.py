import os
import csv

dir = r"C:\Users\guardant\Documents\ENC_Sirius_Variables.csv"
titles = ""
content = ""

with open(dir) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')    
    for x,line in enumerate(csv_reader):
        if x ==0:
            titles = line
        if x ==1:
            content= line
    
print(titles)
print(content)