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

    for child in course.children:
        if (isinstance(child, bs4.element.NavigableString)):
            print(child)
        elif(child.text.strip() == "Details"):
             #soup.select_one('a[href]')
             #href = child.find(href)
             print("******")
             print(child.text.strip())
             print(child)

        else:
            print(child.text.strip())
            print("ELSE")
    course = course.find_next("tr")

print(firstname)
