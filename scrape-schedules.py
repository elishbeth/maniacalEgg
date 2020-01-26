#!/usr/bin/env python
import requests
import bs4
import re

url = "https://www.macalester.edu/registrar/schedules/2020spring/class-schedule/"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content,'lxml')


something = soup.find("tr")
firstname = something.name


while(something != None):

    for child in something.children:
        if (isinstance(child, bs4.element.NavigableString)):
            print(child)
        elif(child.text == Details):
             href = child.find(href)
             print("******")

        else:
            print(child.text)
    something = something.find_next("tr")

print(firstname)
