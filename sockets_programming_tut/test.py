import socket
import threading

HEADER = 64
PORT = 3309  # browse about ports
SERVER = "192.168.43.63"#socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # famil, type of addresses
server.bind(ADDR)


def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    try:

        while connected:
            msg = conn.recv(2048).decode()
            data = msg.split(',')

            if data[0] == "login":
                if data[1] == 'vondoom' and data[2] == "THimberland":
                    print(data)
                    conn.send("success.".encode())


            else:
                conn.send("message received.".encode())
            if msg:
                print(f"[{addr}] {msg}")
    except BrokenPipeError:
        connected = False
        conn.close()
        print(f"[{addr}] HAS BEEN DISCONNECTED!!")
    except ConnectionResetError:
        connected = False
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
