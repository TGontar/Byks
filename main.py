import socket
import random
import byki
from _thread import *
import threading


# print_lock = threading.Lock()


# sock = socket.socket()
# sock.bind(('', 9090))
# a = 10
# sock.listen(a)
# conn, addr = sock.accept()
# print('connected:', addr)
# lis = random.sample(range(1, 10), 4)
# number = ''.join(map(str, lis))
# bnumber = bytes(str(number), encoding="UTF-8")
# print(number)

def threaded(conn):
    # print('Thread: ' + str(conn))
    lis = random.sample(range(1, 10), 4)
    number = ''.join(map(str, lis))
    bnumber = bytes(str(number), encoding="UTF-8")
    print('Answer ' + number)
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
            # print_lock.release()
            break
def Main():
    sock = socket.socket()
    sock.bind(('', 9090))
    a = 10
    sock.listen(a)
    while True:
        conn, addr = sock.accept()
        print('connected:', addr)
        # print_lock.acquire()
        # print('Connected to :', addr[0], ':', addr[1])
        start_new_thread(threaded, (conn,))
        # t1 = threading.Thread(target=threaded(conn))
        # t1.start()
    # conn.close()
# conn.close()
if __name__ == '__main__':
    Main()