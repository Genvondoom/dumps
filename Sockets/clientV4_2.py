import socket, threading

Host = "127.0.0.1"
Port = 5556


def listen():
    global sent
    while True:
        data = b""
        while not data:
            data = s.recv(1024)
        print(f"\b\bRecieved {data.decode()}\n", end = "")


def getInput():
    global sent
    while True:
        data = b""
        while not data:
            data = input("> ").encode()
        sent = data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    sent = b""
    listen_Thread = threading.Thread(target=listen).start()
    input_Thread = threading.Thread(target=getInput).start()
    while True:
        if sent:
            s.sendall(sent)
            sent = b""
