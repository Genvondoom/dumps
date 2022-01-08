import socket

Host = "127.0.0.1"
Port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen()

    conn1, addr = s.accept()
    with conn1:
        print(f"Connected to {addr}")
        conn2, addr2 = s.accept()
        with conn2:
            print(f"Connected to {addr2}")
            while True:
                conn1.sendall(b"\n")
                data = b""
                while not data:
                    data = conn1.recv(1024)
                    print(f"{addr}:{data}")
                conn2.sendall(data)
                conn2.sendall(b"\n")
                data = b""
                while not data:
                    data = conn2.recv(1024)
                    print(f"{addr2}:{data}")
                conn1.sendall(data)
