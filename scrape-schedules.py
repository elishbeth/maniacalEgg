#!/usr/bin/env python
import requests
import bs4
import csv

def getDetails(url):
    page = requests.get(url,verify = False)
    #response = requests.get(url, verify=False
    GeneralEd = ""
    DistReq = ""
    courseMaterials = ""
    soup = bs4.BeautifulSoup(page.content,'lxml')

    allText = soup.get_text().strip()
    splitText = allText.split(":")
    if(len(splitText) >= 2):
        GeneralEd = splitText[1].strip("Distribution Requirements")
    GeneralEdList = GeneralEd.split("\n")
    while("" in GeneralEdList) :
        GeneralEdList.remove("")

    if(len(splitText) >= 3):
        DistReq = splitText[2].strip("Course Materials")
    DistReqList = DistReq.split("\n")
    while("" in DistReqList) :
        DistReqList.remove("")
    if(not isinstance(soup.a, type(None))):
        courseMaterials = soup.a.get('href')

    courseDesc = splitText[0].strip("General Education Requirements").strip()

    detailsList = [courseDesc,GeneralEdList,DistReqList,courseMaterials]

    return(detailsList)

url = "https://www.macalester.edu/registrar/schedules/2020spring/class-schedule/"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content,'lxml')


course = soup.find("tr")
list_dict = []

while(course != None):
    number = 0

    for child in course.children:
        if (number == 0):
            category = "Number"
        if (number == 1):
            category = "Name"
        if (number == 2):
            category = "Days"
        if (number == 3):
            category = "Time"
        if (number == 4):
            category = "Room"
        if (number == 5):
            category = "Instructor"
        if (number == 6):
            category = "Available"


        if (isinstance(child, bs4.element.NavigableString)):
            pass
        elif(child.a):
            url = child.a.get('href')
            detailsList = getDetails(url)
            if(len(detailsList) != 0):
                classDict["Description"] = detailsList[0]
                classDict["General Ed"] = detailsList[1]
                classDict["Distribution Req"] = detailsList[2]
                classDict["Course Materials"] = detailsList[3]
            classDict["Notes"] = child.text.replace("Details", "").strip()
            list_dict.append(classDict)
        else:
            if(number == 0):
                classDict = {}
            classDict[category] = child.text.strip()
            number += 1

    course = course.find_next("tr")

keys = list_dict[1].keys()


classes_csv = open("classes.csv", "w")

dict_writer = csv.DictWriter(classes_csv, keys)
dict_writer.writeheader()
dict_writer.writerows(list_dict)
classes_csv.close()
