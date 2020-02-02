#!/usr/bin/env python
import requests
import bs4
import re

url = "https://www.macalester.edu/registrar/schedules/2020spring/class-schedule/"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content,'lxml')


course = soup.find("tr")
firstname = course.name


while(course != None):
    number = 0

    classDict = {}

    for child in course.children:
        if (number == 0):
            category = "number"
        if (number == 1):
            category = "name"
        if (number == 2):
            category = "days"
        if (number == 3):
            category = "time"
        if (number == 4):
            category = "room"
        if (number == 5):
            category = "instructor"
        if (number == 6):
            category = "available"

        if (isinstance(child, bs4.element.NavigableString)):
            pass
        elif(child.a):
            #print("*link", child.a.get('href'))
            classDict["link"] = child.a.get('href')
            #print("---what this", child.text.replace("Details", "").strip())
            classDict["notes"] = child.text.replace("Details", "").strip()
        else:
            #print(")))))who this",number," ",child.text.strip())
            classDict[category] = child.text.strip()
            number += 1
    print(classDict)
    print("\n\n")
    course = course.find_next("tr")


#print(firstname)
