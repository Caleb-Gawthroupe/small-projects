import psutil
import requests

#Everyday at 10pm -> Auto Task (Windows Built-in)


#Check if laptop is charging ->
def charging():
    return psutil.sensors_battery().power_plugged


#Send a notification to my phone saying it is/isn't ->
def notification():
    message = ""
    desc = ""
    if charging():
        message = "Laptop is charging"
        desc = "Your all good to go"
    else:
        message = "Laptop is not charging"
        desc = "Go plug it in"
        
    requests.post('https://api.mynotifier.app', {
    "apiKey": '36867e8c-320c-47cd-9eae-7f9e1f368cce',
    "message": message,
    "description": desc,
    "type": "info", # info, error, warning or success
    })
    
notification()