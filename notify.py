import requests
import pynotify
from time import sleep
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
r = requests.get('http://api.theysaidso.com/qod.json')
Quote=r.json()

text=Quote["contents"]["quote"]
while True:
    sendmessage("Quote of The Day",text)
    sleep(3600*24)
