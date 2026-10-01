import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(2)

print("Waiting for connections...")

while True:
    c, addr = s.accept()
    
    name = c.recv(1024).decode('utf-8')
    print("connected", addr, name)
    

    c.send("Hey BHaiiii".encode('utf-8'))
    
    c.shutdown(socket.SHUT_WR) 
    
    c.close()
