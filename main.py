import datetime
from playsound import playsound
print("It is "+datetime.datetime.today().strftime("%H")+":"+datetime.datetime.today().strftime("%M"))
hour = int(input("What hour should your alarm be raised (Enter military time): "))
minute = int(input("What minute should your alarm be raised: "))
x = False
while x == False:
    if hour == int(datetime.datetime.today().strftime("%H")) and minute == int(datetime.datetime.today().strftime("%M")):
        print("Alarm Raised")
        playsound(r"C:/Users/Zack/Downloads/Siren_Noise.mp3")
        x = True
        