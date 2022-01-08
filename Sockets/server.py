import socket

Host = "127.0.0.1"
Port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected to {addr}")
            data = conn.recv(1024)
            print(f"Recieved {data.decode()}")
            conn.sendall(data)
