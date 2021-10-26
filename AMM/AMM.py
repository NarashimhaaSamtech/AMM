# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:15:33 2021

@author: Samtech
"""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Progressbar
import time
import serial
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

ser=serial.Serial('COM17',115200) 
def serial():
    while True:
        #i=1
        s2=ser.readline(10).hex()
        return( s2 )

def increment():
    progress_bar.step()  # increment progressbar 
    seconds_label.configure( text=' {} sec'.format(Variable.get()))  # update label
#Main function 

def step7():
    for i in range(9):
        
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
     
        if i==0: 
            progress_bar['maximum']=5  
            
            j=0
            while j<5:
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                progress_bar['value'] += 1
                increment()
                time.sleep(1)
                if j==0:
                    process1['text']='Scanning QR Code'
                if j==4:
                    process1['text']='Scanning Completed'                                      
                j+=1
                error['text']="                                  no error                                  "
            
        elif i==1: 
            progress_bar['maximum']=60
            label_1['bg']='#c71e1e'   
            k=0
            while k<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print(s2[2:4], s2[4:6])
                    progress_bar['value'] += 1                      
                    increment()
                    time.sleep(1)
                    if k==0:
                     ser.write(b'\xfa\x1b\x2b\x00\x00\xfb')
                     process1['text']='Induction Power ON'
                        
                     ser.write(b'\xfa\x0f\x1f\x00\x00\xfb')
                     process2['text']='Stirrer Rotates Fwd'  
                    k+=1
                    error['text']="                                  no error                                  "   
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1)         
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1) 
            label_1['bg']='#36cf4f' 
        elif i==2:           
            progress_bar['maximum']=60
            label_2['bg']='#c71e1e'  
            data1['bg']='#36cf4f'
            l=0
            while l<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print('clear')
                    progress_bar['value'] += 1
                    increment()
                    time.sleep(1)
                    if l==0:
                        ser.write(b'\xfa\x0e\x2e\x00\x00\xfb')
                        process3['text']='Tray Rotates Forward'
                    if l==5:
                        ser.write(b'\xfa\x0c\x1c\x00\x00\xfb')
                        process3['text']='Trap Door Opens'
                    if l==10:
                        ser.write(b'\xfa\x0b\x1b\x00\x00\xfb')
                        process3['text']='Rack 1 Launch'
                    if l==15:
                        ser.write(b'\xfa\x0b\x2b\x00\x00\xfb')
                        process3['text']='Rack 1 Retract'
                    if l==20:
                        ser.write(b'\xfa\x0c\x2c\x00\x00\xfb')
                        process3['text']='Trap Door Close'
                    l+=1
                    error['text']="                                  no error                                  "   
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1) 
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1)
            label_2['bg']='#36cf4f'  
        elif i==3:
            progress_bar['maximum']=60
            label_3['bg']='#c71e1e'  
            data2['bg']='#36cf4f'
            m=0
            while m<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print('clear')
                    progress_bar['value'] += 1
                    increment()
                    time.sleep(1)
                    if m==0:
                        ser.write(b'\xfa\x0e\x2e\x00\x00\xfb')
                        process3['text']='Tray Rotates Forward'
                    if m==5:
                        ser.write(b'\xfa\x0c\x1c\x00\x00\xfb')
                        process3['text']='Trap Door Opens'
                    if m==10:
                        ser.write(b'\xfa\x0b\x1b\x00\x00\xfb')
                        process3['text']='Rack 2 Launch'
                    if m==15:
                        ser.write(b'\xfa\x0b\x2b\x00\x00\xfb')
                        process3['text']='Rack 2 Retract'
                    if m==20:
                        ser.write(b'\xfa\x0c\x2c\x00\x00\xfb')
                        process3['text']='Trap Door Close'
                    m+=1
                    error['text']="                                  no error                                  "   
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1) 
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1)
            label_3['bg']='#36cf4f' 
        elif i==4:           
            progress_bar['maximum']=60
            label_4['bg']='#c71e1e'           
            n=0
            while n<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print('clear')
                    progress_bar['value'] += 1
                    increment()
                    time.sleep(1)
                    if n==0:
                        ser.write(b'\xfa\x1a\x2a\x00\x00\xfb')
                        process3['text']='Water Pump ON'
                    if n==30:
                        ser.write(b'\xfa\x1a\x3a\x00\x00\xfb')
                        process3['text']='Water Pump OFF'
                    n+=1
                    error['text']="                                  no error                                  "      
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1) 
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1)
            label_4['bg']='#36cf4f'  
        elif i==5:            
            progress_bar['maximum']=60
            label_5['bg']='#c71e1e'   
            data3['bg']='#36cf4f'
            j=0
            while j<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print('clear')
                    progress_bar['value'] += 1
                    increment()
                    time.sleep(1)
                    if j==0:
                        ser.write(b'\xfa\x0e\x2e\x00\x00\xfb')
                        process3['text']='Tray Rotates Forward'
                    if j==5:
                        ser.write(b'\xfa\x0c\x1c\x00\x00\xfb')
                        process3['text']='Trap Door Opens'
                    if j==10:
                        ser.write(b'\xfa\x0b\x1b\x00\x00\xfb')
                        process3['text']='Rack 3 Launch'
                    if j==15:
                        ser.write(b'\xfa\x0b\x2b\x00\x00\xfb')
                        process3['text']='Rack 3 Retract'
                    if j==20:
                        ser.write(b'\xfa\x0c\x2c\x00\x00\xfb')
                        process3['text']='Trap Door Close'        
                    j+=1
                    error['text']="                                  no error                                  "   
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1) 
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1)
            label_5['bg']='#36cf4f'  
        elif i==6:
            progress_bar['maximum']=60
            label_6['bg']='#c71e1e'   
            data4['bg']='#36cf4f'
            j=0
            while j<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print('clear')
                    progress_bar['value'] += 1
                    increment()
                    time.sleep(1)
                    if j==0:
                        ser.write(b'\xfa\x0e\x2e\x00\x00\xfb')
                        process3['text']='Tray Rotates Forward'
                    if j==5:
                        ser.write(b'\xfa\x0c\x1c\x00\x00\xfb')
                        process3['text']='Trap Door Opens'
                    if j==10:
                        ser.write(b'\xfa\x0b\x1b\x00\x00\xfb')
                        process3['text']='Rack 4 Launch'
                    if j==15:
                        ser.write(b'\xfa\x0b\x2b\x00\x00\xfb')
                        process3['text']='Rack 4 Retract'
                    if j==20:
                        ser.write(b'\xfa\x0c\x2c\x00\x00\xfb')
                        process3['text']='Trap Door Close'
                    if j==25:
                        ser.write(b'\xfa\x0e\x1e\x00\x00\xfb')
                        process3['text']='Tray to Home Position'
                    j+=1
                    error['text']="                                  no error                                  "    
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1) 
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1)
            label_6['bg']='#36cf4f'  
        elif i==7:
            progress_bar['maximum']=60
            label_7['bg']='#c71e1e'  
            data5['bg']='#36cf4f'
            j=0
            while j<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print('clear')
                    progress_bar['value'] += 1
                    increment()
                    time.sleep(1)
                    if j==0:
                        ser.write(b'\xfa\x0e\x2e\x00\x00\xfb')
                        process3['text']='Tray Rotates Forward'
                    if j==5:
                        ser.write(b'\xfa\x0c\x1c\x00\x00\xfb')
                        process3['text']='Trap Door Opens'
                    if j==10:
                        ser.write(b'\xfa\x0b\x1b\x00\x00\xfb')
                        process3['text']='Rack 5 Launch'
                    if j==15:
                        ser.write(b'\xfa\x0b\x2b\x00\x00\xfb')
                        process3['text']='Rack 5 Retract'
                    if j==20:
                        ser.write(b'\xfa\x0c\x2c\x00\x00\xfb')
                        process3['text']='Trap Door Close'
                    if j==25:
                        ser.write(b'\xfa\x0e\x1e\x00\x00\xfb')
                        process3['text']='Tray to Home Position'
                    j+=1
                    error['text']="                                  no error                                  "    
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1) 
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1)
            label_7['bg']='#36cf4f'   
        elif i==8:
            progress_bar['maximum']=60
            label_8['bg']='#c71e1e'  
            data6['bg']='#36cf4f'
            j=0
            while j<60:
                s2=serial()
                master.update_idletasks()
                master.configure(bg='#40d0e3')
                if s2[2:4]=='00' and s2[4:6]=='00':
                    print('clear')
                    progress_bar['value'] += 1
                    increment()
                    time.sleep(1)
                    if j==0:
                        ser.write(b'\xfa\x0e\x2e\x00\x00\xfb')
                        process3['text']='Tray Rotates Forward'
                    if j==5:
                        ser.write(b'\xfa\x0c\x1c\x00\x00\xfb')
                        process3['text']='Trap Door Opens'
                    if j==10:
                        ser.write(b'\xfa\x0b\x1b\x00\x00\xfb')
                        process3['text']='Rack 6 Launch'
                    if j==15:
                        ser.write(b'\xfa\x0b\x2b\x00\x00\xfb')
                        process3['text']='Rack 6 Retract'
                    if j==20:
                        ser.write(b'\xfa\x0c\x2c\x00\x00\xfb')
                        process3['text']='Trap Door Close'
                    if j==25:
                        ser.write(b'\xfa\x0e\x1e\x00\x00\xfb')
                        process3['text']='Tray to Home Position'
                    if j==58:
                        ser.write(b'\xfa\x0f\x3f\x00\x00\xfb')
                        process2['text']='Stirrer Motor OFF'
                    if j==59:
                        ser.write(b'\xfa\x1b\x3b\x00\x00\xfb')
                        process1['text']='Induction Power OFF'
                    j+=1
                    error['text']="                                  no error                                  "    
                    error['bg']='#ed7464'
                elif s2[2:4]=='09' and s2[8:10]=='04':  #Power Loss
                    p=0
                    while True:
                        master.update_idletasks()
                        master.configure(bg='#40d0e3')
                        time.sleep(1)
                        
                        error['text']="Power Loss, Using Battery Supply"
                        print("Power Loss") 
                        error['bg']='#ba001c'
                        p+=1
                        if p==5:
                            error['text']='Cooking Process Terminated'
                            print('Cooking Process Terminated') 
                            time.sleep(1)
                            master.destroy()
                            break
                        else:
                            continue       
                    time.sleep(1)
                elif s2[2:4]=='09' and s2[8:10]=='00': #Power ON
                    error['text']='               Power Turned ON               '
                    error['bg']='#36cf4f' 
                    print('Power Turned ON') 
                    time.sleep(1) 
                elif s2[2:4]=='01' and s2[4:6]=='04':
                    print("Induction_IGPT_Temp _Error") 
                    error['text']="Induction_IGPT_Temp _Error"                        
                    time.sleep(1)
                elif s2[2:4]=='01' and s2[4:6]=='08':
                    print("INDUCTION_Voltage_Error Occured")	
                    error['text']="INDUCTION_Voltage_Error Occured"                  
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='00':
                    print("Water_top_sensor_Read_Full_Water")
                    error['text']="Water_top_sensor_Read_Full_Water"                
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='10':
                    print("Water_top_senor_Read_No_Water")    
                    error['text']="Water_top_senor_Read_No_Water"              
                    time.sleep(1)
                elif s2[2:4]=='02' and s2[4:6]=='20':
                    print("Water_Bottom_senor_Read_NO_Water")	
                    error['text']="Water_Bottom_senor_Read_NO_Water"                  
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='00':
                    print("Touch_Bottom_ON/OFF_Key_no_press key")  
                    error['text']="Touch_Bottom_ON/OFF_Key_no_press key"                
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='40':
                    print("Touch_Bottom_ON/OFF_Key_pressed key")   
                    error['text']="Touch_Bottom_ON/OFF_Key_pressed key"               
                    time.sleep(1)
                elif s2[2:4]=='03' and s2[4:6]=='80':
                    print("Touch_Bottom_INC/DEC_Key_pressed key")   
                    error['text']="Touch_Bottom_INC/DEC_Key_pressed key"               
                    time.sleep(1)	
                elif s2[2:4]=='04' and s2[6:8]=='00':
                    print("Lid_Open_Position_Sensor_Status is Low")   
                    error['text']="Lid_Open_Position_Sensor_Status is Low"               
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='01':
                    print("Lid_Open_Position_Sensor_Status is High")  
                    error['text']="Lid_Open_Position_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='04' and s2[6:8]=='02':
                    print("Lid_Close_Position_Sensor_Status is High") 
                    error['text']="Lid_Close_Position_Sensor_Status is High"                 
                    time.sleep(1)	
                elif s2[2:4]=='05' and s2[6:8]=='00':
                    print("Packet_lanuch_Position_Sensor_status is Low") 
                    error['text']="Packet_lanuch_Position_Sensor_status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='04':
                    print("Packet_lanuch_Position_Sensor_status is HIGH") 
                    error['text']="Packet_lanuch_Position_Sensor_status is HIGH"                 
                    time.sleep(1)
                elif s2[2:4]=='05' and s2[6:8]=='08':
                    print("Packet_Retract_Position_Sensor_status is HIGH") 
                    error['text']="Packet_Retract_Position_Sensor_status is HIGH"                 
                    time.sleep(1)	
                elif s2[2:4]=='06' and s2[6:8]=='00':
                    print("Trap_Door_Open_Positon_Sensor_Status is low") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is low"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='10':
                    print("Trap_Door_Open_Positon_Sensor_Status is High") 
                    error['text']= "Trap_Door_Open_Positon_Sensor_Status is High"                
                    time.sleep(1)
                elif s2[2:4]=='06' and s2[6:8]=='20':
                    print("Trap_Door_Close_Positon_Sensor_Status is High")
                    error['text']="Trap_Door_Close_Positon_Sensor_Status is High"	                  
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='00':
                    print("Piercing_Home_position_Sensor_Status is Low") 
                    error['text']="Piercing_Home_position_Sensor_Status is Low"                 
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='40':
                    print("Piercing_Home_position_Sensor_Status is High")   
                    error['text']="Piercing_Home_position_Sensor_Status is High"              
                    time.sleep(1)
                elif s2[2:4]=='07' and s2[6:8]=='80':
                    print("piercing_Sensor_Status is High")      
                    error['text']="piercing_Sensor_Status is High"            
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='00':
                    print("Tray_Index_Position_Sensor_Status_LOW")  
                    error['text']="Tray_Index_Position_Sensor_Status_LOW"                
                    time.sleep(1)
                elif s2[2:4]=='08' and s2[8:10]=='01':
                    print("Tray_Index_Position_Sensor_Status_HIGH")  
                    error['text']="Tray_Index_Position_Sensor_Status_HIGH"                
                    time.sleep(1)
            label_8['bg']='#36cf4f'  
            process3['text']='Cooking Completed'
        
master = tk.Tk()
master.geometry('720x480')
master.title('Cooking_Process')
master.configure(bg='#40d0e3')

Variable = tk.DoubleVar(master)

label = tk.Label(master,text='Mirchi Ka Salan', bg='#40d0e3',fg='#ab070f', font=('Times New Roman', 20, 'bold'))
label.place(relx=0.5, rely=0.05, anchor='center')

# label for boxes
label_1=tk.Label(master, text='Heat pan',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_1.place(relx = 0.08, rely = 0.2, anchor = 'center', height=70)

label_2=tk.Label(master, text='Rack 1',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_2.place(relx = 0.20, rely = 0.2, anchor = 'center', height=70)

label_3=tk.Label(master, text='Rack 2',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_3.place(relx = 0.32, rely = 0.2, anchor = 'center', height=70)

label_4=tk.Label(master, text='Water',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_4.place(relx = 0.44, rely = 0.2, anchor = 'center', height=70)

label_5=tk.Label(master, text='Rack 3',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_5.place(relx = 0.56, rely = 0.2, anchor = 'center', height=70)

label_6=tk.Label(master, text='Rack 4',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_6.place(relx = 0.68, rely = 0.2, anchor = 'center', height=70)

label_7=tk.Label(master, text='Rack 5',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_7.place(relx = 0.80, rely = 0.2, anchor = 'center', height=70)

label_8=tk.Label(master, text='Rack 6',borderwidth = 1,relief='raised', width= 8, bg='#8a8888', fg='#fafafa', font=('Helvetica', 10, 'bold'))
label_8.place(relx = 0.92, rely = 0.2, anchor = 'center', height=70)

#label for time
time_1=tk.Label(master, text='60sec', bg='#40d0e3')
time_1.place(relx = 0.08, rely = 0.35, anchor = 'center')

time_2=tk.Label(master, text='60sec', bg='#40d0e3')
time_2.place(relx = 0.20, rely = 0.35, anchor = 'center')

time_3=tk.Label(master, text='60sec', bg='#40d0e3')
time_3.place(relx = 0.32, rely = 0.35, anchor = 'center')

time_4=tk.Label(master, text='60sec', bg='#40d0e3')
time_4.place(relx = 0.44, rely = 0.35, anchor = 'center')

time_5=tk.Label(master, text='60sec', bg='#40d0e3')
time_5.place(relx = 0.56, rely = 0.35, anchor = 'center')

time_6=tk.Label(master, text='60sec', bg='#40d0e3')
time_6.place(relx = 0.68, rely = 0.35, anchor = 'center')

time_7=tk.Label(master, text='60sec', bg='#40d0e3')
time_7.place(relx = 0.80, rely = 0.35, anchor = 'center')

time_8=tk.Label(master, text='60sec', bg='#40d0e3')
time_8.place(relx = 0.92, rely = 0.35, anchor = 'center')

seconds_label = tk.Label(master, text='0 sec', bg='#40d0e3')
seconds_label.place(relx = 0.9, rely=0.466, anchor = 'center')

progress_bar = ttk.Progressbar(master, orient="horizontal",mode="determinate",maximum=100, length=500, variable=Variable)
progress_bar.place(relx = 0.5, rely = 0.47, anchor = 'center')

# process bar
process1 = tk.Label(master,borderwidth = 1,width = 20,bg='#beeddf',relief="ridge",text="")
process1.place(relx=0.1, rely=0.7, anchor='center',height=100)

process2 = tk.Label(master,borderwidth = 1,width = 20,bg='#beeddf',relief="ridge",text="")
process2.place(relx=0.3, rely=0.7, anchor='center',height=100)

process3 = tk.Label(master,borderwidth = 1,width = 20,bg='#beeddf',relief="ridge",text="")
process3.place(relx=0.5, rely=0.7, anchor='center',height=100)

process4 = tk.Label(master,borderwidth = 1,width = 40,bg='#ed7464',relief="ridge",text="")
process4.place(relx=0.8, rely=0.7, anchor='center',height=100)

error = tk.Label(master,text="",bg='#ed7464')
error.place(relx=0.8, rely=0.69, anchor='center')


#bottom display bar
bar1 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Water Level =")
bar1.place(relx=0.125, rely=0.965, anchor='center',height=35)

bar2 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Induction Temperature =")
bar2.place(relx=0.375, rely=0.965, anchor='center',height=35)

bar3 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Tray Position =")
bar3.place(relx=0.625, rely=0.965, anchor='center',height=35)

bar4 = tk.Label(master,borderwidth = 2,width = 25,relief="ridge",text="Battery =")
bar4.place(relx=0.875, rely=0.965, anchor='center',height=35)

A=['A','B','C','D','E','F']
#Tray data
data1 = tk.Label(master,borderwidth = 2,width = 12,relief="sunken",text="")
data1.place(relx=0.09, rely=0.865, anchor='center',height=30)

data2 = tk.Label(master,borderwidth = 2,width = 12,relief="sunken",text="")
data2.place(relx=0.255, rely=0.865, anchor='center',height=30)

data3 = tk.Label(master,borderwidth = 2,width = 12,relief="sunken",text="")
data3.place(relx=0.42, rely=0.865, anchor='center',height=30)

data4 = tk.Label(master,borderwidth = 2,width = 12,relief="sunken",text="")
data4.place(relx=0.585, rely=0.865, anchor='center',height=30)

data5 = tk.Label(master,borderwidth = 2,width = 12,relief="sunken",text="")
data5.place(relx=0.75, rely=0.865, anchor='center',height=30)

data6 = tk.Label(master,borderwidth = 2,width = 12,relief="sunken",text="")
data6.place(relx=0.915, rely=0.865, anchor='center',height=30)

step7()

master.mainloop()