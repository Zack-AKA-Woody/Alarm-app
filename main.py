#IMPORTS
import datetime
import time
import os
import sys
import threading
from playsound import playsound

#VARIABLES
alarm_HH = 00
alarm_MM = 00

#ALARM SOUND
def loopSound():
    while True:
         now = time.localtime()
         if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
            playsound("C:/Users/Zack/Downloads/Siren_Noise.mp3", block=True)

#KILL ALARM 
def stop_alarm():
        while True:
            loopThread = threading.Thread(target=loopSound, name='Alarm Sound')
            loopThread.daemon = False
            loopThread.start()
            
#ACTUAL ALARM
def alarm_function():
     #GLOBALS
     global alarm_HH
     global alarm_MM
     while True:
        now = time.localtime()
        if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
             loopThread = threading.Thread(target=loopSound, name='Alarm Sound')
             loopThread.daemon = True
             loopThread.start()
             print("!!!WAKE UP!!!")
             print ("---------------")
             print ("Scan QR code to disable the alarm --> testing code: Type Goodmorning")
             print ("---------------")
             answer = input("Enter Answer: ")
             if answer == "Goodmorning":
                 print ("---------------")
                 print ("Alarm Disabled")
                 break
             loopThread.join(stop_alarm)
        else:
            pass
             
#SET THE TIME FOR THE ALARM
def alarm_set():
    #GLOBALS
    global alarm_HH
    global alarm_MM
    print ("---------------")
    alarm_HH = input("What hour do you want to wake up? (24 hour format) ")
    print ("---------------")
    alarm_MM = input("How about the minute? ")
    print ("---------------")
    print ("Alarm Set")
    alarm_function()

#STARTING SEQUENCE
print ("----------------")
print ("QR CODE ALARM CLOCK")
print ("----------------")
answer = input("Type <<1>> to start ")
if answer == 1:
    alarm_set()
else:
    alarm_set()




        
    

