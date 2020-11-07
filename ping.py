## Lancer le serveur avant de lancer ping
import socket
from datetime import datetime
import http.server
import socketserver
import sys

IP = sys.argv[1]
t1 = datetime.now()
ttl = 0.025
PORT = 6332
socket.setdefaulttimeout(ttl)




def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,PORT))
   if result == 0:
      return 1
   else :
      return 0

def ping(addr):
      if (scan(addr)):
         t2 = datetime.now()
         total = t2 - t1
         print('Succes !!')
         print ("from {}: ttl={} time={} ms".format(addr,ttl,total))
      else:
          print('Port unreachable')

ping(IP)