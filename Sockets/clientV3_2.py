import socket

Host = "127.0.0.1"
Port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    while True:
        data = b""
        while data != b"\n":
            data = s.recv(1024)

        sent = input(">").encode()
        s.sendall(sent)

        data = b""
        while not data:
            data = s.recv(1024)
        print(f"Recieved {data.decode()}")

