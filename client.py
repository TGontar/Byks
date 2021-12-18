import socket
sock = socket.socket()
sock.connect((str(input()), 9090))
message = ''
print("""DOBRO POZHALOVAT V IGRY BYKI I KOROVI. 
TSEL PROSTA: OTGADAT` 4 ZNACHNOE CHISLO, ZAGADANNOY KOMPOM, 
ESLI VI UGADALI TSIFRY I EE POZITSIY, TO ETO BYK. ESLI UGADALI TSIFRY, 
NO POZITSIA DRYGAYA, TO ETO KOROVA""")
while message != 'HAROSH TI POBEDIL':
    sock.send(bytes(str(input()), encoding='UTF-8'))
    data = sock.recv(1024)
    message = data.decode()
    print(message)
# sock.close()
#
# print(str(data, encoding='UTF-8'))