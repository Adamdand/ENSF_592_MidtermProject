# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:16:40 2020

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

cluster = MongoClient("mongodb+srv://adamdand:Family590274003?@cluster0.okwdo.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["592_Project_1"] #<--- data base name in mongodb

collection = db["Traffic_Incidents_Archive_2016"]
#results = list(collection.find({}))


#print(results)

    
Lat = list(collection.find({}, {"Latitude":1,"_id":0}))
Long = list(collection.find({}, {"Longitude":1,"_id":0}))
Count = list(collection.find({}, {"Count":1,"_id":0}))

list_lat = []
for result in Lat:
    list_lat.append(result["Latitude"])
    
    
list_long = []
for result in Long:
    list_long.append(result["Longitude"])  
    
    
list_count = []
for result in Count:
    list_count.append(result["Count"])

df=pd.DataFrame({'Latitude':list_lat,'Longitude' : list_long, 'Count' : list_count})

#print(df)

map_osm = folium.Map(location=[51.0673798693422,-114.028551292521], tiles='Stamen Toner', zoom_start=13)
#df = pd.read_excel("C:/Users/adamd/Desktop/ENSF592/Project2/Test.csv")
#df = pd.read_csv('C:/Users/adamd/Desktop/ENSF592/Project2/Traffic_Incidents_Archive_2016.csv')
#print(df)


for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=str(row['Count']),icon=folium.Icon(color='red',icon='location', prefix='ion-ios')).add_to(map_osm)
    #folium.CircleMarker(location=[ , ], redius=50, popup=' ', colour='red', fill = True, fill_colour='red').add_to(map_osm)
    

map_osm

map_osm.save('C:/Users/adamd/Desktop/ENSF592/Project2/map2.html')
