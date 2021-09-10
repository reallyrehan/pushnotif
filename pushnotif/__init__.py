from  urllib import request
import json

class PushNotif():
    key, event = "",""

    def __init__(self,key,event):
            self.key = key
            self.event = event
        
        
    def send(self,value1 = "",value2="",value3=""):
        values = {
            "value1": value1,
            "value2": value2,
            "value3": value3
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        data = json.dumps(values).encode("utf-8")
        try:
            url = "https://maker.ifttt.com/trigger/"+self.event+"/with/key/"+self.key
            req = request.Request(url, data, headers)
            with request.urlopen(req) as f:
                res = f.read()
        except Exception as e:
            print(e)