# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:18:51 2021

@author: Samtech
"""

import tkinter as tk
import time 

def step4():
    for i in range(3):
        root.update_idletasks()
        root.configure(bg='#40d0e3')
        time.sleep(1)
        if i==0:
            label = tk.Label(root,text='RAKAKA', bg='#40d0e3',fg='#ab070f', font=('Times New Roman', 50, 'bold'))
            label.place(relx=0.5, rely=0.45, anchor='center')
        if i==1:
            label = tk.Label(root,text='RAKAKA', bg='#40d0e3',fg='#ab070f', font=('Times New Roman', 50, 'bold'))
            label.place(relx=0.5, rely=0.45, anchor='center')
        if i==2:
            root.destroy()
            import AMM_Splash
               
root=tk.Tk()
root.geometry('720x480')
root.configure(bg='#40d0e3')

step4()
root.mainloop()