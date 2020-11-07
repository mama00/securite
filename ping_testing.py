# ----------------------------------------
# Program  : Efectuer un ping
# FileName : ping_testing.py
# I/P 	  : 127.0.0.1
# O/P 	  :  
# By       : Kevin J DUBUCHE 
# ---------------------------------------- 

# Ecrire un programme en python qui permet d'effectuer un ping
# Contraintes: Port 6332  | use Idle | use socket | architecture Client/Server  

# __________________________________________________________
   #socket.SOCK_STREAM           The default protocol that’s used is TCP (Is reliable; Has in-order data delivery)

#importation des packages utiles a programme
import socket
from datetime import datetime
import http.server
import socketserver
#fin des importations

IP = input("Enter the IP address: ")
t1 = datetime.now()
ttl = 0.025
PORT = 6332
socket.setdefaulttimeout(ttl)

# def startServer(PORT):
#    Handler = http.server.SimpleHTTPRequestHandler
#    with socketserver.TCPServer(("", PORT), Handler) as httpd:
#       print("serving at port", PORT)
      # httpd.serve_forever()



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

# startServer(PORT)        
ping(IP)