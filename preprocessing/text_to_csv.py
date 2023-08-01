import csv
import os

FilePath = "C:/ITStudy/3/data/INSTAGRAM"

file_list = os.listdir(FilePath)
#normal data
f = open('C:/ITStudy/3/data/instagram.csv','a', newline='')

for file in file_list:
    open_file = open(FilePath+'/'+file, "r",encoding='utf-8')

    while True:
        try:
            line = open_file.readline()
            line = line[4:]
            wr = csv.writer(f)
            wr.writerow([file,line.strip(), 1])
            if not line:
                break
        except:
            continue

    open_file.close()
f.close()

# unnormal data
f = open('C:/ITStudy/3/data/unnormal.csv','a', newline='')
FilePath = "C:/ITStudy/3/data"
open_file = open(FilePath+'/'+'voicephising.txt', "r",encoding='utf-8')
idx = 0
while True:
    try:
        line = open_file.readline()
        line = line[6:]
        wr = csv.writer(f)
        wr.writerow([idx,line.strip(), 0])
        if not line:
            break
        idx+=1
    except:
        continue

open_file.close()
f.close()
