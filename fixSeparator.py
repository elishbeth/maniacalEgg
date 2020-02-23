#!/usr/bin/env python
import requests
import bs4
import re
import csv
import time

import time

url = "https://webapps.macalester.edu/registrardata/classdata/spring2020/30003"
page = requests.get(url,verify = False)
#response = requests.get(url, verify=False)
soup = bs4.BeautifulSoup(page.content,'lxml')

allText = soup.get_text()

L = []
if "\n" in allText:
    L = allText.strip().split("\n")
    L.remove("")

count = 1
ClassDict = {}
for l in L:
    if l!="" and count == 1:
        ClassDict["Description"] = l
        count = 4
    if "General Education" in l:
        count = 2
        ClassDict["General Education"] = []
    if "Fine Arts" in l:
        count = 3
    if count == 2 and l!="":
        ClassDict["General Education"].append(l)
    if count == 3 and l!="":
        ClassDict["Fine Arts"] = l
