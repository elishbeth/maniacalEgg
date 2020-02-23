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

allText = soup.get_text())
allText
