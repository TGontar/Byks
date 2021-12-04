import socket
import random
import byki
from _thread import *
sock = socket.socket()
sock.bind(('', 9090))
a = 10
sock.listen(a)
conn, addr = sock.accept()
print('connected:', addr)
lis = random.sample(range(1, 10), 4)
number = ''.join(map(str, lis))
bnumber = bytes(str(number), encoding="UTF-8")
print(number)

while True:
    message = ''
    data = conn.recv(1024)
    if not data:
        break
    else:
        data = data.decode(encoding='UTF-8')
        print(data)
        message = byki.byks(data, number)
        conn.send(bytes(message, encoding="UTF-8"))
    print(message)
    if message == 'HAROSH TI POBEDIL':
        break

# conn.close()