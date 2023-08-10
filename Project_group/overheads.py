## Using the variable datafile, open the overheads csv from saved location

datafile = open('C:\Python Programming 1\project_group\csv_reports\Overheads.csv',"r")
datafile.readline()
cat = ''
highest = 0
for line in datafile:
    info = line.split(",")
    if float(info[1])> highest:
        highest = float(info[1])
        cat = info[0]
report = open('summary_report.txt',"w")
report.write("[HIGHEST OVERHEAD] "+cat+': '+str(highest)+"%")
report.close()