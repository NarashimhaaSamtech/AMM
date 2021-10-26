import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

def step3():
    master.destroy()
    import Recipe_selection
    
master = tk.Tk()
master.geometry('720x480')
master.title('Select process !!!')
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
            
btn1=ttk.Button(master,text='Manual',width=26,style='my.TButton')
btn1.place(relx=0.285, rely=0.4, anchor='center',height=125)

btn1=ttk.Button(master,text='Automated',width=26,command=step3,style='my.TButton')
btn1.place(relx=0.715, rely=0.4, anchor='center',height=125)

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