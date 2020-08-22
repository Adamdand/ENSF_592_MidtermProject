# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:12:54 2020

@author: adamd
"""

import pymongo
from pymongo import MongoClient

import pymongo
import tkinter as tk
from tkinter import ttk

import pandas as pd
import csv
import numpy as np

import folium
from folium.plugins import MarkerCluster
import os


import folium
from folium.plugins import MarkerCluster
import xlrd
import tkinterhtml
from tkinterhtml import HtmlFrame


from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import style

cluster = MongoClient("mongodb+srv://adamdand:Family590274003?@cluster0.okwdo.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["592_Project_1"] #<--- data base name in mongodb

collection1 = db["TrafficFlow2016_OpenData"]
collection2 = db["2017_Traffic_Volume_Flow"]
collection3 = db["Traffic_Volumes_for_2018"]



#print(results)

year2016 = list(collection1.find({}, {"year_vol":1,"_id":0}))
volume2016 = list(collection1.find({}, {"volume":1,"_id":0}))

year2017 = list(collection2.find({}, {"year":1,"_id":0}))
volume2017 = list(collection2.find({}, {"volume":1,"_id":0}))

year2018 = list(collection3.find({}, {"YEAR":1,"_id":0}))
volume2018 = list(collection3.find({}, {"VOLUME":1,"_id":0}))

#~~~~~~~~~~~~2016~~~~~~~~~~~~~~~~~


list_vol2016= []
for result in volume2016:
    list_vol2016.append(result["volume"])
    
volSum2016 = 0;
for i in list_vol2016:
    if i>volSum2016:
        volSum2016=i
   
#~~~~~~~~~~~~2017~~~~~~~~~~~~~~~~~


list_vol2017= []
for result in volume2017:
    list_vol2017.append(result["volume"])
    
volSum2017 = 0;
for i in list_vol2017:
    if i>volSum2017:
        volSum2017=i
#~~~~~~~~~~~~2018~~~~~~~~~~~~~~~~~



list_vol2018= []
for result in volume2018:
    list_vol2018.append(result["VOLUME"])

volSum2018 = 0;
for i in list_vol2018:
    if i>volSum2018:
        volSum2018=i



print(volSum2016)
print(volSum2017)
print(volSum2018)



table = {'Year': ['2016','2017','2018'],
         'Volume' : [volSum2016, volSum2017, volSum2018]}



df=pd.DataFrame(data=table)

print(df)



"""
df2=df['Year'].value_counts().to_frame('y').rename_axis('Year').reset_index()
df2=df2.sort_values("Year",axis=0, ascending = True)

print(df2)
"""









