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
runtime = int(alarm_MM) + (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20)

#ALARM SOUND
def loopSound():
    while True:
         now = time.localtime()
         if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM) or int(alarm_MM) + runtime:
            playsound("C:/Users/Zack/Downloads/Siren_Noise.mp3", block=True)
            
#ACTUAL ALARM
def alarm_function():
     while True:
        now = time.localtime()
        if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM) or int(alarm_MM) + runtime:
             loopThread = threading.Thread(target=loopSound, name='Alarm Sound')
             loopThread.daemon = True
             loopThread.start()
             print("!!!WAKE UP!!!")
             print ("---------------")
             print ("Scan QR code to disable the alarm --> testing code: Type Goodmorning")
             print ("---------------")
             answer = input("Enter Answer: ")
             while answer != "Goodmorning":
                 answer = input("Enter Answer: ")
             if answer == "Goodmorning":
                print ("---------------")
                print ("Alarm Disabled")
                break
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




        
    

