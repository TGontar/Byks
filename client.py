import socket
sock = socket.socket()
sock.connect((str(input()), 9090))
message = ''
while message != 'HAROSH TI POBEDIL':
    sock.send(bytes(str(input()), encoding='UTF-8'))
    data = sock.recv(1024)
    message = data.decode()
    print(message)
# sock.close()
#
# print(str(data, encoding='UTF-8'))