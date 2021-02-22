import schedule 
import time 
import webbrowser
import json


f = open('data.json') 
data = json.load(f)
f.close()

import datetime 

day_name= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
day = datetime.datetime.now().weekday()


print("This is Schedule Join Automatic MS Teams by Aman Tiwari..")
print("Today is Time Table")
for i in data[day_name[day]]:

    print("______________________________________")
    print(" ")
    print(f" {i['Name']}      | {i['time']}    ")


print("")
print("************")

print("HI, I am Micrsoft Bot, I wil take care of your College attendence! you just tap join without needing table time and opening Ms teams")

print("************")


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





while True: 
    schedule.run_pending() 
    time.sleep(1)



