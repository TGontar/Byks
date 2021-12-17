import socket
import random
import byki
from _thread import *
import threading


def threaded(conn, number):
    name = "PLAYER #" + str(random.randint(1, 1000))
    print(name + " joined the game")
    while True:
        message = ''
        data = conn.recv(1024)
        if not data:
            break
        else:
            data = data.decode(encoding='UTF-8')
            print(name + ": " + data)
            message = byki.byks(data, number)
            conn.send(bytes(message, encoding="UTF-8"))
        print(name + ": " + message)
        if message == 'HAROSH TI POBEDIL':
            # print_lock.release()
            break


def Main():
    lis = random.sample(range(1, 10), 4)
    number = ''.join(map(str, lis))
    bnumber = bytes(str(number), encoding="UTF-8")
    print('Answer ' + number)
    sock = socket.socket()
    sock.bind(('', 9090))
    a = 10
    sock.listen(a)
    print('IGRA V KALMARA NACHALAS`')
    while True:
        conn, addr = sock.accept()
        # print('connected:', addr)
        start_new_thread(threaded, (conn, number))


if __name__ == '__main__':
    Main()
