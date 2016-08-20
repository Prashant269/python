import socket
socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.100.105.111",90))
sock.listen(2)
(client,(ip,port))=sock.accept()
