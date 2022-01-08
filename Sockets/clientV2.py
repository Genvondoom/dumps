import socket

Host = "127.0.0.1"
Port = 5556

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    while True:
        sent = input(">").encode()
        s.sendall(sent)
        data = s.recv(1024)

        print(f"Recieved {data.decode()}")
