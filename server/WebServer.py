# _*_ coding: utf-8 _*_
import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)


def run(sock, add):
    print 'Accept new connection from %s:%s...' % add
    data = []
    length = 0
    while True:
        data.append(sock.recv(1024))
        if length == len(data):
            break
        length = len(data)
        print data[0]
    image = json.loads(bytes(data))
    sock.close()


while True:
    client, add = s.accept()
    print '地址: ', add
    run(client, add)
    client.close()


