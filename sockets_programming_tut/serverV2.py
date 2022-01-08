import socket
import threading

PORT = 3309  # browse about ports
SERVER = "192.168.43.63"
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # famil, type of addresses
server.bind(ADDR)


def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")


def start():
    server.listen()
    print(f"[LISTENING]: SERVER is listening on {SERVER}")

    conn, addr = server.accept()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    print(f"[NEW CONNECTION]: connecting to {addr}")
    # conn.send("hello.".encode())
    connected = True
    try:  # prevents server from crashing
        while connected:
            msg = conn.recv(2048).decode(FORMAT)
            # data = msg.split(',')
            # print(data)
            if msg == "hi":
                conn.send("hello.".encode())
            elif msg == "how are you":
                conn.send("am fine.".encode())
            elif msg == "okay bye":
                conn.send("bye.".encode())
                # connected = False

            else:

                conn.send("message received.".encode())

            if msg:
                print(f"[{addr}] {msg}")



    except ConnectionResetError:
        conn.close()
        print(f"[{addr}] HAS BEEN DISCONNECTED!!")
    except BrokenPipeError:
        conn.close()
    # conn.close()
    print(f"{addr} disconnected")


print("[STARTING] server is starting . . . ")
start()
