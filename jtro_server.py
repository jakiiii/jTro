#!/usr/bin/env python3
import socket


lst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lst.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lst.bind(("192.168.31.207", 1337))
lst.listen(5)
print("[+] Waiting for incoming connection.")
lst.accept()
print("[+] Connection has been established.")
