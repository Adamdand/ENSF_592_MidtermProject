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


collection1 = db["Traffic_Incidents_Archive_2016_sorted_freq"]
collection2 = db["Traffic_Incidents_Archive_2017_sorted_freq"]
collection3 = db["Traffic_Incidents_Archive_2018_sorted_freq"]



#print(results)

volume2016 = list(collection1.find({}, {"freq":1,"_id":0}))

volume2017 = list(collection2.find({}, {"freq":1,"_id":0}))

volume2018 = list(collection3.find({}, {"freq":1,"_id":0}))

#~~~~~~~~~~~~2016~~~~~~~~~~~~~~~~~


list_vol2016= []
for result in volume2016:
    list_vol2016.append(result["freq"])
    
volSum2016 = 0;
for i in list_vol2016:
    if i>volSum2016:
        volSum2016=i
   
#~~~~~~~~~~~~2017~~~~~~~~~~~~~~~~~


list_vol2017= []
for result in volume2017:
    list_vol2017.append(result["freq"])
    
volSum2017 = 0;
for i in list_vol2017:
    if i>volSum2017:
        volSum2017=i
#~~~~~~~~~~~~2018~~~~~~~~~~~~~~~~~



list_vol2018= []
for result in volume2018:
    list_vol2018.append(result["freq"])

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
fig=Figure(figsize = (5,4),dpi=100)

a=fig.add_subplot(1,1,1).plot(df2.Year, df2.y)
fig.subplots_adjust(left=0.1, right=0.8, bottom=0.1) 

canvas = FigureCanvasTkAgg(fig, master=window)
#fig.set_xlabel('x')
#fig.set_ylabel('y')

canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
#figure tool bar, maybe not neccessary
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
"""
