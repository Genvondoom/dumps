import socket

Host = "127.0.0.1"
Port = 5556

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected to {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Recieved {data.decode()}")
                sent = input(">").encode()
                try:
                    conn.sendall(sent)
                except ConnectionResetError as e:
                    break
