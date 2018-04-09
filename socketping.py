#!/usr/bin/env python
#coding=utf-8

import socket
import commands
ip_port=('192.168.4.40',445)
s=socket.socket()
s.bind(ip_port)
s.listen(5)
while True:
    c,addr=s.accept()
    print "Get connection from",addr
    #while True:
    #    data=c.recv(1024)
    #    print "Recv data:",data
    #    if len(data)==0:
    #        print "Lost connection from",addr
    #        c.close()
    #        break
    #   elif not data:
    #        print "Lost connection form",addr
    #        break
    #    else:
    #        st,out=commands.getstatusoutput(data)
    #        print "recv:",data
    #        c.send(out)
    c.close()
