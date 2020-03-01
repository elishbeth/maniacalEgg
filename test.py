# !/usr/bin/env python
import requests
import bs4
import re
import csv
import time

import time

url = "https://webapps.macalester.edu/registrardata/classdata/spring2020/30535"
page = requests.get(url, verify=False)
# response = requests.get(url, verify=False)
soup = bs4.BeautifulSoup(page.content,'lxml')

allText = soup.get_text()

L = []
if "\n" in allText:
    L = allText.strip().split("\n")
    L.remove("")

count = 1
ClassDict = {}
for l in L:
    if count == 1 and l!="":
        ClassDict["Description"] = l
        count = 5

    if "General Education" in l:
        count = 2
        ClassDict["General Education"] = []

    elif count == 2 and l!="" and "Distribution" not in l:
        ClassDict["General Education"].append(l)

    if "Distribution" in l:
        count = 3
        ClassDict["Distribution"] = []

    elif count == 3 and l!="" and "Course Materials" not in l:
        ClassDict["Distribution"].append(l)

    if "Course Materials" in l:
        ClassDict["Course Materials"] = soup.a.get("href")



print(ClassDict)
