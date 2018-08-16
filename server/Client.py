# -*- coding: utf-8 -*-

import socket
import json

ip_port = ('192.168.1.146', 8080)
s = socket.socket()
s.connect(ip_port)
while True:
    filePath = raw_input('FilePath : ')
    file = open(filePath, 'rb')
    js = json.dumps({"action": "upload-img", "img": bytes(file)})
    s.send(bytes(js))
s.close()
