# ----------------------------------------
# Program  : Efectuer un ping
# FileName : ping_testing.py
# I/P 	  : 127.0.0.1
# O/P 	  :  
# By       : Kevin J DUBUCHE 
# ---------------------------------------- 

# Ecrire un programme en python qui permet d'effectuer un ping
# Contraintes: Port 6332  | use Idle | use socket     

# __________________________________________________________

import socket
from datetime import datetime
IP = input("Enter the IP address: ")
t1 = datetime.now()
ttl = 0.025
PORT = 8080
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