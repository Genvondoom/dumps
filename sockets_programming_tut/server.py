import socket
import threading

HEADER = 64
PORT = 5054  # browse about ports
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # famil, type of addresses
server.bind(ADDR)


def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        conn.send("Hello".encode(FORMAT))
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()
    print(f"[{addr}] HAS BEEN DISCONNECTED!!")


def start():
    server.listen()
    print(f"[LISTENING]: SERVER is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION]: connecting to {addr}")
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting . . . ")
start()
