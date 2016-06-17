outputs = []
crontable = []
'''crontable.append([10, "say_hello"])'''
import simplejson as json
import requests

exchange = {}

def process_message(data):
    global exchange
    channel = data["channel"]
    text = data["text"]
    if channel.startswith("C04JUEPP0"):
         if text.startswith("exchange"):
              outputs.append([channel, "Searching...:thinking_face:"])
              exchange[channel].append(text[9:])
              url = "http://api.fixer.io/latest?symbols=MXN&base=USD"
              resp = requests.get(url=url)
              data = json.loads(resp.text)
    outputs.append(["D0JJGQRJ9", data])
