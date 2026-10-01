import socket

c = socket.socket()
c.connect(('localhost', 9999))

name = input("Enter Your Name: ")
c.send(name.encode('utf-8'))


data = c.recv(1024).decode('utf-8')
print(data)

c.close()
