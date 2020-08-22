# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
class MainApplication(tk.Frame):
   def __init__(self, master):
       self.master = master
       tk.Frame.__init__(self, self.master)
       self.configure_gui()
       self.create_widgets()

   def configure_gui(self):
       self.master.title('Calgary Traffic Program') #title at top of main window
       self.master.geometry('800x500')  #size of main window
       self.master.expand=True   #expandable = TRUE

   def create_widgets(self):
       self.create_frames()    #using frames
       self.create_buttons()    #using buttons


   def create_frames(self):
       self.left_frame = tk.Frame(width=100, height=500, background='#808080')
       self.left_frame.grid_propagate(0)
       self.left_frame.grid(row=0, column=0)


       self.right_frame = tk.Frame(width=700, height=500, background='#C0C0C0')
       self.right_frame.grid_propagate(0)
       self.right_frame.grid(row=0, column=1)
       

   def create_buttons(self):
       self.create_left_frame_buttons()
       self.create_right_frame_buttons()       

   def create_left_frame_buttons(self):
       self.button1 = tk.Button(self.left_frame, text='Type')  
       #                 (ROW  , COLOUMN,   horr screen dist ,cert.space between)
       self.button1.grid(row=0, column=0, padx=30, pady=20)

       self.button2 = tk.Button(self.left_frame, text='Year')       
       self.button2.grid(row=1, column=0, padx=30, pady=20) 
       
       self.button3 = tk.Button(self.left_frame, text='Read')       
       self.button3.grid(row=2, column=0, padx=30, pady=20) 
       
       self.button4 = tk.Button(self.left_frame, text='Sort')       
       self.button4.grid(row=3, column=0, padx=30, pady=20) 
       
       self.button5 = tk.Button(self.left_frame, text='Analysis')       
       self.button5.grid(row=4, column=0, padx=30, pady=20) 
       
       self.button6 = tk.Button(self.left_frame, text='Map')       
       self.button6.grid(row=5, column=0, padx=30, pady=20) 
       


   def create_right_frame_buttons(self):
      
       """
       self.button1 = tk.Button(self.right_frame, text='Button3')       
       self.button1.grid(row=0, column=0, padx=20, pady=50)

       self.button2 = tk.Button(self.right_frame, text='Button4')       
       self.button2.grid(row=0, column=1, padx=70)
       """


if __name__ == '__main__':
   window = tk.Tk()
   main_app =  MainApplication(window)
   window.mainloop()

"""
border_effects = {
    "flat" : tk.FLAT,
    "sunkn" : tk.SUNKEN,
    "raised" : tk.RAISED,
    "groove" : tk.GROOVE,
    "ridge" : tk.RIDGE,
    }

window = tk.Tk()


frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="Im in Frame A")
label_a.pack()
label_b = tk.Label(master=frame_b, text="Im in Frame B")
label_b.pack()


frame_a.pack()
frame_b.pack()

window.mainloop()
"""
"""
label = tk.Label(text = "hello,Tkinter",
                 fg = "white",
                 bg = "black",
                 width = 10,
                 height = 5)
label.pack()

entry = tk.Entry()
entry = tk.Entry(fg = "yellow", bg = "blue", width = 50)
entry.pack()


name = entry.get()
"""

"""
button = tk.Button(
    text = "Click me!",
    width = 25,
    height = 5,
    bg = "blue",
    fg = "yellow",)
"""
"""

label2 = tk.Label(text = name,
                 fg = "white",
                 bg = "black",
                 width = 10,
                 height = 5)
label2.pack()

window.mainloop()
"""


"""
window = tk.Tk()
greeting = tk.Label(text = "hello Tkinter")
greeting.pack()

window.mainloop()
"""


"""
class ExampleView(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        l = tk.Label(self, text="your widgets go here...", anchor="c")
        l.pack(side="top", fill="both", expand=True)

if __name__=='__main__':
    root = tk.Tk()
    view = ExampleView(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
"""

        

