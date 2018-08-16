#!/usr/bin/python
import json

data = [{'a': open("C:\1.txt", "r"), 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

json = json.dumps(data)
print json