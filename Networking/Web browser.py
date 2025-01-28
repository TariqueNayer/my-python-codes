import socket
call = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
call.connect(('data.pr4e.org',80))

gmd = 'GET http://data.pr4e.org/clown.txt HTTP/1.0\r\n\r\n'.encode()
print(gmd)
call.send(gmd)
while True:
    data = call.recv(512)
    if len(data) < 1:
        break
    #print(data)
    print(data.decode())
call.close()
