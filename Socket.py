# -*- coding: UTF-8 -*-

import socket

s = socket.socket();

s.bind(("127.0.0.1", 12345))

s.listen(5)

while True:
    c, addr = s.accept()     # 建立客户端连接。
    c.send("123456")
    print c.recv