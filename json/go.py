import json

with open("a.json", 'r') as f:
    temp = json.loads(f.read())
    print(temp)
