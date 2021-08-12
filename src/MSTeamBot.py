import schedule 
import time 
import webbrowser
import json
import datetime 
import sys
import os
from colorama import init
from colorama import Fore, Back, Style
init()
from os import path  








bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
data_path = os.path.abspath(path.join(bundle_dir, 'data.json'))

f=open(data_path)
data = json.load(f)
f.close()

size = os.get_terminal_size().columns
 


day_name= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
day = datetime.datetime.now().weekday()



print(Style.RESET_ALL)



print(f"{Fore.GREEN}Today is Time Table : {day_name[day]}".center(size))


for i in data[day_name[day]]:
    print(" ")
    print(f"{Fore.MAGENTA}*"*size)
    print(f" {Fore.RED} {i['Name']} {Fore.WHITE} -- {Fore.YELLOW} {i['time']}".center(size))


print(f"{Fore.RED}*"*size)


print(f"{Fore.YELLOW}Hi, I am MSTeamBot, I will nofity you to join the class when time start!".center(size))
print(f"{Fore.YELLOW}you just tap join without looking table time and opening Ms teams".center(size))
print(f"{Fore.YELLOW} Nofitier and Join Meeting MS Teams..".center(size))
print(f"{Fore.YELLOW} Made By Aman Tiwari..".center(size))

print(" ")
print(f"{Fore.RED}*"*size)
print(f"{Fore.YELLOW} Note: Do Not Close this Program, Otherwise I will not nofity you to join the class and you will get low attendence")


def OpenApp(url):
    webbrowser.open(url)



for i in data["monday"]:
    schedule.every().monday.at(i["time"]).do(OpenApp, i["url"])


for i in data["tuesday"]:
    schedule.every().tuesday.at(i["time"]).do(OpenApp, i["url"])


for i in data["wednesday"]:
    schedule.every().wednesday.at(i["time"]).do(OpenApp, i["url"])

for i in data["thursday"]:
    schedule.every().thursday.at(i["time"]).do(OpenApp, i["url"])

for i in data["friday"]:
    schedule.every().friday.at(i["time"]).do(OpenApp, i["url"])

for i in data["sunday"]:
    schedule.every().sunday.at(i["time"]).do(OpenApp, i["url"])




while True: 
    schedule.run_pending() 
    print(f"{Fore.RED}Running.".center(size), end="\r")
    time.sleep(0.05)
    print(f"{Fore.RED}Running....".center(size), end="\r")
    time.sleep(1)




