import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address="192.168.193.252"
port=8080

complete=(ip_address,port)
s.bind(complete)


while True:
   msg=s.recvfrom(1024)
   decodingMsg=msg[0].decode('ascii')
   print(msg)
