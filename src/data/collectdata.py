# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:37:43 2016

@author: vleung
"""

import requests

import json 
from xml.etree import ElementTree

from datetime import datetime
import time


if __name__=="__main__":
# Authentication parameters
 headers = { 'AccountKey' : 'uGRbgLzXR3ukHemzQGhomg==',
            'UniqueUserID' : '85f31f16-c935-471d-a599-e0e93e6a1070',
            'accept' : 'application/json'}

    
# Traffic Speed Bands
uri = 'http://datamall2.mytransport.sg/'
path_TSB = 'ltaodataservice/TrafficSpeedBands'
path_TI = 'ltaodataservice/TrafficIncidents'
path_FTL = 'ltaodataservice/FaultyTrafficLights'
path_ERP = 'ltaodataservice/ERPRates'

count = 12

while (((datetime.now().month == 10) and (datetime.now().day > 24)) or ((datetime.now().month == 11) and (datetime.now().day < 5))):
    # collect Traffic Speed Band data
    with open('../../data/raw/TSB.txt', 'w') as outfile:
        try:
            r = requests.get(uri + path_TSB, headers=headers)
            data = json.loads(r.text)
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M")
            data["timestamp"] = timestamp
            json.dump(data, outfile)
        except:
            pass
    
    # collect Traffic Incidents data    
    with open('../../data/raw/TI.txt', 'w') as outfile:
        try:
            r = requests.get(uri + path_TI, headers=headers)
            data = json.loads(r.text)
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M")
            data["timestamp"] = timestamp
            json.dump(data, outfile)
        except:
            pass
    # collect Faulty Traffic Light data    
    with open('../../data/raw/FTL.txt', 'w') as outfile:
        try:
            r = requests.get(uri + path_TI, headers=headers)
            data = json.loads(r.text)
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M")
            data["timestamp"] = timestamp
            json.dump(data, outfile)
        except:
            pass
    
    # collect ERP Rates Data
    with open('../../data/raw/ERP.txt', 'w') as outfile:
        try:
            r = requests.get(uri + path_TI, headers=headers)
            data = json.loads(r.text)
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M")
            data["timestamp"] = timestamp
            json.dump(data, outfile)
        except:
            pass
    
    # collect 2 hour forecast
    if (count > 11):
        count = 0
        try:
            url = 'http://api.nea.gov.sg/api/WebAPI/?dataset=2hr_nowcast&keyref=781CF461BB6606ADC767F3B357E848ED455313756293E581'
            r = requests.get(url)
            weather = ElementTree.fromstring(r.content)
            weather.write(open('weather.xml', 'w'), encoding='unicode')
        except:
            pass

    # wait 5 minutes
    time.sleep(300)
    #print datetime.now()    
    count += 1
