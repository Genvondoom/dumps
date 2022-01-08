import socket

HEADER = 64
PORT = 5059  # browse about ports
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    # msg_lenght = len(message)
    # send_lenght = str(msg_lenght).encode(FORMAT)
    # send_lenght += b' ' * (HEADER - len(send_lenght))
    # client.send(send_lenght)
    client.send(message)
    return (client.recv(2048))


def sampleCreate():

    if send(str(['signup', '18/1789', 'software engineering', '400', 'THimberland011']).lstrip("b'").rstrip(
            "'")) == b'Account created Sucessfully':
        print("Account created")
        if send(str(['login', '18/1789', 'THimberland000'])) == b'Login Sucessful':
            print("Login successful")
    else:
        print("error creating account")


def login():
    loginSend = send(str(['login', '18/1789', 'THimberland011']))
    if loginSend == b'Login Sucessful':
        print("Login successful")
    elif loginSend == b'Invalid Login Details':
        print("Login Failed")

sampleCreate()
input("")

send(str([DISCONNECT_MESSAGE]))
