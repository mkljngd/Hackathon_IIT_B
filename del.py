import urllib.request, json
from lol import print_messages
import pandas as pd

updates = print_messages()
d=''
key = 'tweet'
for i in range(len(updates)):
    d += '{"' + key+str(i)+'" : "' + updates[i] + '"},'
d=d[:-1]
#print(d)
p = json.dumps(d)
print(p)
