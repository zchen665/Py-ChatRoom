# -*- coding: UTF-8 -*-
import time
from socket import *
import sys
from threading import Thread

HOST = 'ip address here'
BUFSIZ = 1024
PORT = 3080


class client():
    def __init__(self, name='anonymous'):
        self.name = name
        try:
            self.c = socket(AF_INET, SOCK_STREAM)
            self.c.connect((HOST, PORT))
            welcome_msg = time.ctime() + name + '加入聊天'
            self.c.send(bytes(welcome_msg, 'utf-8'))
            self.send = Thread(target= self.sendmg)
            self.recv = Thread(target=self.recvmg)
            self.send.start()
            self.recv.start()
        except ConnectionResetError:
            print("server is closed. Thanks")
            self.c.close()
        except error:
            print(sys.exc_info())
            self.c.close()

    def sendmg(self):
        while self.c.connect_ex((HOST, PORT)):
            msg = input('>:')
            if not self.c.connect_ex((HOST, PORT)):
                break
            o_msg = time.ctime() + ' ' + self.name + ': ' + msg
            o_msg = (bytes(o_msg, 'utf-8'))
            self.c.send(o_msg)

    def recvmg(self):
        while self.c.connect_ex((HOST, PORT)):
            if not self.c.connect_ex((HOST, PORT)):
                break
            msg = self.c.recv(BUFSIZ).decode('utf-8')
            print(msg)


if __name__ == '__main__':
    c = client(sys.argv[1])  # get name

# s = socket.socket()
# host = socket.gethostname()
# port = 3080
# s.connect((host,port))
# print(s.recv(1024).decode('utf-8'))
# mes = input('Enter a message:')
# s.send(bytes('hola server from client: ' + mes, 'utf-8'))
# print(s.recv(1024).decode('utf-8'))
# print(time.time())
# s.close()
