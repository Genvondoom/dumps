import socket

Host = "127.0.0.1"
Port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    s.sendall(b"Hello this is a connection")
    data = s.recv(1024)
print(f"Recieved {data.decode()}")
