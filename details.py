#!/usr/bin/env python
import requests
import bs4
import re
import csv
import time

import time

def getDetails(url):
    page = requests.get(url,verify = False)
    #response = requests.get(url, verify=False)
    soup = bs4.BeautifulSoup(page.content,'lxml')

    allText = soup.get_text().strip()
    splitText = allText.split(":")
    GeneralEd = splitText[1].strip("Distribution Requirements")
    GeneralEdList = GeneralEd.split("\n")
    while("" in GeneralEdList) :
        GeneralEdList.remove("")


    DistReq = splitText[2].strip("Course Materials")
    DistReqList = DistReq.split("\n")
    while("" in DistReqList) :
        DistReqList.remove("")

    courseMaterials = soup.a.get('href')

    courseDesc = splitText[0].strip("General Education Requirements").strip()

    detailsList = [courseDesc,GeneralEdList,DistReqList,courseMaterials]

    return(detailsList)
    # print(splitText[0].strip("General Education Requirements").strip())
    # print(GeneralEdList)
    # print(DistReqList)
    # print(courseMaterials)
#link("https://webapps.macalester.edu/registrardata/classdata/spring2020/30805")
