# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:56:39 2021

@author: Samtech
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


def step4():
    master.destroy()
    import Recipe_Initialize

master = tk.Tk()
master.geometry('720x480')
master.title('Select your Recipe !!!')
master.configure(bg='#40d0e3')

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 12, 'bold'))

#s1=ser.read(10)
#if s1==command for Water Level High:
    #bar1['text']='Water Level = High' 
#elif s1==command for Water Level Low:
    #bar1['text']='Water Level = Low'
#else:
    #continue
#if s1==command for Induction Temperature High:
    #bar2['text']='Induction Temperature = High' 
#elif s1==command for Induction Temperature Low:
    #bar2['text']='Induction Temperature = Low'
#else:
    #continue
#if s1==command for Tray in Rack 1 Position:
    #bar3['text']='Tray Position = Rack 1' 
#elif s1==command for Tray in Rack 2 Position:
    #bar3['text']='Tray Position = Rack 2' 
#elif s1==command for Tray in Rack 3 Position:
    #bar3['text']='Tray Position = Rack 3' 
#elif s1==command for Tray in Rack 4 Position:
    #bar3['text']='Tray Position = Rack 4' 
#else:
    #continue
#if s1==command for Battery Level 100%:
    #bar4['text']='Battery Level 100%' 
#elif s1==command for Battery Level 75%:
    #bar4['text']='Battery Level 75%'
#elif s1==command for Battery Level 50%:
    #bar4['text']='Battery Level 50%'  
            
btn1=ttk.Button(master,text='Mirchi Ka Salan',width=18, command=step4,style='my.TButton')
btn1.place(relx=0.25, rely=0.225, anchor='center',height=150)

label1 = tk.Label(master,text="i) A popular and spicy curry base recipe   ii) Made with peanuts, sesame and long slit green chillies", wraplength=225, bg='#40d0e3')
label1.place(relx=0.55, rely=0.225, anchor='center')

btn2=ttk.Button(master,text='',width=18,style='my.TButton')
btn2.place(relx=0.25, rely=0.65, anchor='center',height=150)

label2 = tk.Label(master,text="", wraplength=225, bg='#40d0e3')
label2.place(relx=0.55, rely=0.725, anchor='center')

#bottom display bar
bar1 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Water Level =")
bar1.place(relx=0.125, rely=0.965, anchor='center',height=35)

bar2 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Induction =")
bar2.place(relx=0.375, rely=0.965, anchor='center',height=35)

bar3 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Tray Position =")
bar3.place(relx=0.625, rely=0.965, anchor='center',height=35)

bar4 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Battery =")
bar4.place(relx=0.875, rely=0.965, anchor='center',height=35)

master.mainloop()