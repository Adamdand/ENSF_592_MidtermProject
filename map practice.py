# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:55:38 2020

@author: adamd
"""
import folium
from folium.plugins import MarkerCluster
import xlrd
import pandas as pd
import folium
map_osm = folium.Map(location=[51.0673798693422,-114.028551292521], tiles='Stamen Toner', zoom_start=13)
#df = pd.read_excel("C:/Users/adamd/Desktop/ENSF592/Project2/Test.csv")
df = pd.read_csv('C:/Users/adamd/Desktop/ENSF592/Project2/Traffic_Incidents_Archive_2016.csv')
for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=str(row['Count']),icon=folium.Icon(color='red',icon='location', prefix='ion-ios')).add_to(map_osm)
#folium.CircleMarker(location=[ , ], redius=50, popup=' ', colour='red', fill = True, fill_colour='red').add_to(map_osm)
map_osm

map_osm.save('C:/Users/adamd/Desktop/ENSF592/Project2/map_1.html')