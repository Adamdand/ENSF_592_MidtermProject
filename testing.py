# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:03:15 2020

@author: adamd
"""

from tkinter import*

root = Tk() #creating blank window
theLabel = Label(root, text="Calgary Traffic")
theLabel.pack() #pack = pack it in there where ever it fits

leftFrame = Frame(root)  #making invisible in main container (root)
leftFrame.pack(side=LEFT)   #place it now in main window

rightFrame = Frame(root) #blank rectangle in main window
rightFrame.pack(side=RIGHT)   #side=BOTTOM/LEFT/RIGHT/TOP

#create some labels
label1 = Label(leftFrame, text="Buttons", bg="black", fg="white")
label1.pack(fill=BOTH) #side of label will be as big as it needs to be

label2 = Label(rightFrame, text = "Data",  bg="black", fg="white")
label2.pack(fill=Y)

#make some buttons
button1 = Button(leftFrame, text="Type", )  #(which frame you want it in, text, colour)
button2 = Button(leftFrame, text="Year", )
button3 = Button(leftFrame, text="Read", )
button4 = Button(leftFrame, text="Sort", )
button5 = Button(leftFrame, text="Analysis",)
button6 = Button(leftFrame, text="Map", )

#display buttons on screen
button1.pack(side=TOP) #(side=LEFT)=pack button as far left as possible
button2.pack(side=TOP)
button3.pack(side=TOP)
button4.pack(side=TOP)
button5.pack(side=TOP)
button6.pack(side=TOP)

root.mainloop() #keep window continuously on screen until we close it - infinit loop

