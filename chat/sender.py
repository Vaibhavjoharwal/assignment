import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="192.168.193.100"
port=1234
complete=(ip_add,port)
while True:
    message=input("wassup!!")
    encode_message= message.encode('ascii')
    s.sendto(encode_message,complete)




 