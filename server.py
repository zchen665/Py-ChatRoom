# -*- coding: UTF-8 -*-
import socket
from threading import Thread
import time
import sys
HOST = 'ip address here'
BUFSIZ = 1024
PORT = 3080

class server():

    def __init__(self, num_user = 5):
        self.ADDR = (HOST, PORT)
        try:
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.s.bind(self.ADDR)
            self.s.listen(num_user)
            self.EXIT = False
            self.clients = {}
            self.thrs = {}
            print('server started...orz')
            self.timer = Thread(target=self.close_all)
            self.timer.start()
        except :
            print('Port %d is down' %PORT)
            return False
    def listen(self):
        try:
            while not self.EXIT:
                cur_c ,addr = self.s.accept()
                cur_c.send(bytes('WELCOME!!','utf-8'))
                print("headcount: ", len(self.clients))
                self.clients[addr] = cur_c;
                print('addr: ',addr)
                self.thrs[addr] = Thread(target=self.readmg, args=[addr])
                self.thrs[addr].start()
                time.sleep(0.5)
        except:
            print("error")
            return False

    def readmg(self, addr):
        if addr not in self.clients.keys():
            return False
        c = self.clients[addr]
        while not self.EXIT:
            try:
                # get message content data
                data = c.recv(BUFSIZ).decode('utf-8')
                print(data)
                for connection in self.clients.values():
                    connection.sendall(bytes(data,'utf-8'))
                # c.sendall(bytes(data,'utf-8'))

            except:
                print(sys.exc_info()[0])
                c.close()
                break
            if not data:
                break

    def close_all(self):
        while True:
            cmd = input()
            if cmd.upper()== 'Q':
                break
        self.EXIT = True
        for c in self.clients.values():
            c.close()
        print("exiting")
        self.s.close()
        exit(0)



if __name__ == '__main__':
    s = server()
    s.listen()
    print('Exited successfully')
