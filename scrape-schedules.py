#!/usr/bin/env python
import requests
import bs4
import re
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
            #print("*link", child.a.get('href'))
            classDict["link"] = child.a.get('href')
            #print("---what this", child.text.replace("Details", "").strip())
            classDict["notes"] = child.text.replace("Details", "").strip()
        else:
            if(number == 0 ):
                classDict = {}
            #print(")))))who this",number," ",child.text.strip())
            classDict[category] = child.text.strip()
            number += 1

    list_dict.append(classDict)
    course = course.find_next("tr")

keys = list_dict[1].keys()

classes_csv = open("classes.csv", "w")

dict_writer = csv.DictWriter(classes_csv, keys)
dict_writer.writeheader()
dict_writer.writerows(list_dict)
classes_csv.close()
