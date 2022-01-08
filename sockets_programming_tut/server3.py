import socket


host = socket.gethostbyname(socket.gethostname())
port = 5050
print(host)

server_sock = socket.socket(socket.AF_INET)
server_sock.bind((host, port))
server_sock.listen(1)

client_sock, addr = server_sock.accept()
print('Connected by', addr)
data = "1234567"
client_sock.send(data.encode())

client_sock.close()
server_sock.close()