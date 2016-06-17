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
    if text.startswith("exchange"):
          exchange[channel] = []
          outputs.append([channel, "Searching...:thinking_face:"])
          exchange[channel].append(text[9:])
          url = "http://api.fixer.io/latest?symbols=MXN&base=USD"
          resp = requests.get(url=url)
          data = json.loads(resp.text)
          outputs.append([channel, data])
