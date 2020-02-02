#!/usr/bin/env python
import requests
import bs4
import re
import csv

url = "https://webapps.macalester.edu/registrardata/classdata/spring2020/30268"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content,'lxml')

#print(soup.get_text())
