# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:45:52 2020

@author: adamd
"""

from pymongo import MongoClient
from random import randint
#pprint library is used to make the output look better
from pprint import pprint
#connect to MongoDB, change the <<MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.admin
"""
#issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
"""

#creating sample data

names = ["kitchen" , "animals" , "state" , "big" , "fish"]
company_type = ["LLC","Inc","Company","Corporation"]
company_cuisine = ["pizza","Bar Food","Fast Food","Italiant","Mexican","American","Sushi"]

for x in range (1,501):
    business = {
        'name' : banes[randint(0,(len(names)-1))] + ' ' + names[radint(0,(len(names)-1))] + 
        'rating': randint(1,5) ,
        'cuisine' : company_cuisine[randint(0,(len(company_cuisine)-1))]
        }
    
# insert business object directly into MongoDB via isnert_one
    result=db.reviews.insert_one(business)
    #print to consol the ObjectID of the new document
    print('Created [0] of 500 as [1]'.format(x,result.inserted_id))

#tell us that you are done
print('finished creating 500 business reviews')