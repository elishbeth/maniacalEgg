#!/usr/bin/env python
import requests
import bs4
import csv

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
            classDict["Link"] = child.a.get('href')
            classDict["Notes"] = child.text.replace("Details", "").strip()
            list_dict.append(classDict)
        else:
            if(number == 0):
                classDict = {}
            classDict[category] = child.text.strip()
            number += 1

    course = course.find_next("tr")


keys = list_dict[1].keys()

link= "https://webapps.macalester.edu/registrardata/classdata/spring2020/30040"
newPage = requests.get(link)
miniSoup = bs4.BeautifulSoup(newPage.content,'lxml')
print(miniSoup.get_text())

classes_csv = open("classes.csv", "w")

dict_writer = csv.DictWriter(classes_csv, keys)
dict_writer.writeheader()
dict_writer.writerows(list_dict)
classes_csv.close()

def getDetails(url):
    page = requests.get(url, verify=False)
    soup = bs4.BeautifulSoup(page.content, 'lxml')

    allText = soup.get_text()

    L = []
    if "\n" in allText:
        L = allText.strip().split("\n")
        L.remove("")

    count = 1
    ClassDict = {}
    for l in L:
        if count == 1 and l != "":
            ClassDict["Description"] = l
            count = 5

        if "General Education" in l:
            count = 2
            ClassDict["General Education"] = []

        elif count == 2 and l != "" and "Distribution" not in l:
            ClassDict["General Education"].append(l)

        if "Distribution" in l:
            count = 3
            ClassDict["Distribution"] = []

        elif count == 3 and l != "" and "Course Materials" not in l:
            ClassDict["Distribution"].append(l)

        if "Course Materials" in l:
            ClassDict["Course Materials"] = soup.a.get("href")

    return ClassDict
