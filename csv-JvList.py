import csv


def reformatTime(time):
    """converts the time format from the csv to a 2 element array of start-time and end-time in 24hr double format"""
    if not len(time) == 23:
        return("[]")
    Shour = int(time[6:8])
    Smin = int(time[9:11])
    Sampm = time[12:14]
    Ehour = int(time[15:17])
    Emin = int(time[18:20])
    Eampm = time[21:23]
    if Sampm == "am":
        STime = Shour
    else:
        STime = 12 + Shour
    if Eampm == "am":
        ETime = Ehour
    else:
        ETime = Ehour + 12
    STime = STime + round(Smin/90., 2)
    ETime = ETime + round(Emin/90., 2)
    return("["+str(STime)+","+str(ETime)+"]")


def reformatAvailable(avail):
    """converts the availability format from the csv to a 2 element array of available-seats and max-size"""
    avail = avail[13:]
    available = ""
    maximum = ""
    for i in range(len(avail)):
        if avail[i] == "/":
            available = avail[0:i-1]
            maximum = avail[i+2:]
    return("[" + available + "," + maximum + "]")


def cleanUpText(text):
    out = ""
    for i in text:
        if i in ['"', "'"]:
            out += "\\"
        out += i
    return out



with open('classesFall.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    out = '{\n'
    iternum = 0
    for row in readCSV:
        if(iternum > 0):
            out += '\t"' + row[0] + '"' + ": {\n"
            out += '\t\t"Title" : "' + row[1] + '",\n'
            out += '\t\t"Day" : ' + '"' + row[2][6:].strip() + '",\n'
            out += '\t\t"Time" : ' + reformatTime(row[3]) + ',\n'
            out += '\t\t"Room" : "' + row[4][6:] + '",\n'
            out += '\t\t"Instructor" : "' + row[5][12:] + '",\n'
            out += '\t\t"Availability" : ' + reformatAvailable(row[6]) + ',\n'
            out += '\t\t"Description" : "' + cleanUpText(row[7]) + '",\n'
            out += '\t\t"GeneralEd" : ' + row[8] + ',\n'
            out += '\t\t"DistributionReq" : "' + row[9][1:-1] + '",\n'
            out += '\t\t"CourseMaterials" : "' + row[10] + '",\n'
            out += '\t\t"Notes" : "' + row[11] + '",\n'
            out += "\t},\n"
        iternum += 1
    out += '};'

file1 = open("jv2.txt", "w")
file1.write(out)
file1.close()
