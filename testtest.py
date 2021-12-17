# from _thread import *
# import threading
#
#
# def threaded(conn):
#     conn = int(conn[0])
#     print('Thread: ' + str(conn))
#     while True:
#         conn += 1
#         print(conn)
#         if conn == 5:
#             break
#
#
# def Main():
#     while True:
#         conn = tuple(str(input()))
#         start_new_thread(threaded, (conn))
#
#
# if __name__ == '__main__':
#     Main()
import socket
sock = socket.socket()
sock.connect((str(input()), 9080))
print(sock.recv(1024).decode('UTF-8'))
message = ''
text = """
Куда будете бить?
1. Направо
2. Налево
3. Центр
"""
while message != "Игра закончена!":
    sock.send(bytes(int(input(text))))
    data = sock.recv(1024)
    message = data.decode()
    print(message)