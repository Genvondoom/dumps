import socket

HEADER = 64
PORT = 5051  # browse about ports
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' '*(HEADER- len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048))
send("Hello World!!")
input("")
send("Hello Everyone!!")
input("")
send("Hello Vondoom!!")
input("")
send(DISCONNECT_MESSAGE)