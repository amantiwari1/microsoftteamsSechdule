import schedule 
import time 
import webbrowser
import json


data = {
  "monday": [
    {
      "Name": "Data Analytics",
      "time": "09:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3a10e7d72ff9f14c4285fe977d0770ecbb%40thread.tacv2/1613322209259?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%22e23c6d7f-490a-4e4e-beff-f05d1be5a33d%22%7d"
    },
    {
      "Name": "Web Programming",
      "time": "10:00",
      "url": "https://teams.microsoft.com/l/team/19%3a67d8ada616c94432967961ba22abff9e%40thread.tacv2/conversations?groupId=f6542471-e59e-439d-946b-8d5f32ed0f41&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    },
    {
      "Name": "Software Engineering",
      "time": "11:00",
      "url": "https://teams.microsoft.com/l/team/19%3a272afc27f43a408099b8a642f57972ac%40thread.tacv2/conversations?groupId=a9925e0c-2774-4ef6-ae80-66097c8982df&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    },
    {
      "Name": "Computer Algorithms",
      "time": "12:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3aad57cd5df45646ac8c37bd49a3555c53%40thread.tacv2/1610344619144?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%2213843375-6b35-4265-8115-69fa8708bbb8%22%7d"
    },
    {
      "Name": "Data Analytics lab",
      "time": "14:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3a32e407dccdd84a4a92395e2b988141c5%40thread.tacv2/1613378165090?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%22e23c6d7f-490a-4e4e-beff-f05d1be5a33d%22%7d"
    }
  ],

  "tuesday": [
    {
      "Name": "Web Programming",
      "time": "10:00",
      "url": "https://teams.microsoft.com/l/team/19%3a67d8ada616c94432967961ba22abff9e%40thread.tacv2/conversations?groupId=f6542471-e59e-439d-946b-8d5f32ed0f41&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    },
    {
      "Name": "Software Engineeering",
      "time": "11:00",
      "url": "https://teams.microsoft.com/l/team/19%3a272afc27f43a408099b8a642f57972ac%40thread.tacv2/conversations?groupId=a9925e0c-2774-4ef6-ae80-66097c8982df&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    },
    {
      "Name": "Data Analytics",
      "time": "12:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3a10e7d72ff9f14c4285fe977d0770ecbb%40thread.tacv2/1610372928683?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%22e23c6d7f-490a-4e4e-beff-f05d1be5a33d%22%7d"
    },
    {
      "Name": "Data Analytics Lab",
      "time": "14:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3a32e407dccdd84a4a92395e2b988141c5%40thread.tacv2/1613635904451?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%22e23c6d7f-490a-4e4e-beff-f05d1be5a33d%22%7d"
    }
  ],

  "wednesday": [
    {
      "Name": "FCA Class",
      "time": "10:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3aad57cd5df45646ac8c37bd49a3555c53%40thread.tacv2/1613542040283?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%2213843375-6b35-4265-8115-69fa8708bbb8%22%7d"
    },
    {
      "Name": "Software Engineeering",
      "time": "11:00",
      "url": "https://teams.microsoft.com/l/team/19%3a67d8ada616c94432967961ba22abff9e%40thread.tacv2/conversations?groupId=f6542471-e59e-439d-946b-8d5f32ed0f41&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    },
    {
      "Name": "Data Analytics",
      "time": "13:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3a10e7d72ff9f14c4285fe977d0770ecbb%40thread.tacv2/1610373543483?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%22e23c6d7f-490a-4e4e-beff-f05d1be5a33d%22%7d"
    },
    {
      "Name": "Web Programming Lab",
      "time": "14:00",
      "url": "https://teams.microsoft.com/l/channel/19%3a1aaf31a42d454ef08ddc2671cbce88dc%40thread.tacv2/CA257%2520Web%2520Programming%2520lab?groupId=f6542471-e59e-439d-946b-8d5f32ed0f41&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    }
  ],

  "thursday": [
    {
      "Name": "Web Programmming",
      "time": "12:00",
      "url": "https://teams.microsoft.com/l/team/19%3a67d8ada616c94432967961ba22abff9e%40thread.tacv2/conversations?groupId=f6542471-e59e-439d-946b-8d5f32ed0f41&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    },
    {
      "Name": "Computer Algorithms",
      "time": "13:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3aad57cd5df45646ac8c37bd49a3555c53%40thread.tacv2/1613453719812?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%2213843375-6b35-4265-8115-69fa8708bbb8%22%7d"
    },
    {
      "Name": "Software Engineering Lab",
      "time": "14:00",
      "url": "https://teams.microsoft.com/l/team/19%3a272afc27f43a408099b8a642f57972ac%40thread.tacv2/conversations?groupId=a9925e0c-2774-4ef6-ae80-66097c8982df&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    }
  ],
  "friday": [
    {
      "Name": "Computer Algorithms",
      "time": "10:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3aad57cd5df45646ac8c37bd49a3555c53%40thread.tacv2/1613542040283?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%2213843375-6b35-4265-8115-69fa8708bbb8%22%7d"
    },
    {
      "Name": "Data Analytics",
      "time": "11:00",
      "url": "https://teams.microsoft.com/l/meetup-join/19%3a10e7d72ff9f14c4285fe977d0770ecbb%40thread.tacv2/1610373848954?context=%7b%22Tid%22%3a%2212b4fbf9-dea8-4490-bede-9cc40309ad61%22%2c%22Oid%22%3a%22e23c6d7f-490a-4e4e-beff-f05d1be5a33d%22%7d"
    },
    {
      "Name": "Web Programming Lab",
      "time": "12:00",
      "url": "https://teams.microsoft.com/l/channel/19%3a1aaf31a42d454ef08ddc2671cbce88dc%40thread.tacv2/CA257%2520Web%2520Programming%2520lab?groupId=f6542471-e59e-439d-946b-8d5f32ed0f41&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    },
    {
      "Name": "Software Engineeering Lab",
      "time": "14:00",
      "url": "https://teams.microsoft.com/l/team/19%3a272afc27f43a408099b8a642f57972ac%40thread.tacv2/conversations?groupId=a9925e0c-2774-4ef6-ae80-66097c8982df&tenantId=12b4fbf9-dea8-4490-bede-9cc40309ad61"
    }
  ]
}
 

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



