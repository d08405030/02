import requests

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-from-urlencoded"
    }

    payload = {'message':msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

message = 'Notify from LINE, HELLO WORLD'
token = 'J3l2kY9Ydc1GLXvxL38dN9xnZyyCAuuuuUNQL71myNn'

lineNotifyMessage(token, message)