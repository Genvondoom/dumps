import socket
import threading
import dbconn

HEADER = 64
PORT = 5059  # browse about ports
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # famil, type of addresses
server.bind(ADDR)
election = [['CES1222210', 'bucc presidential election', 'faculty', 'computing and engineering science', '20/11/2022',
             '10:10am', '4hrs 30mins', '02:40pm', 'active'],
            ['CES1223210', 'Bucc Presidential Election', 'faculty', 'Computing And Engineering Science', '20/12/2022',
             '11:50am', '2hrs', '01:50pm', 'active']]


def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    con = dbconn.DBconnect()
    connected = True
    login = False
    ELECTION = ()
    try:
        while connected:
            msg = conn.recv(2048).decode(FORMAT)
            msg = eval(msg)
            if msg[0] == 'login':

                res = con.login(msg[1:])
                if res:
                    conn.send("Login Sucessful".encode(FORMAT))
                    print(f"[ALERT]:{addr} logged in successfully")
                    ELECTION = res
                    login = True
                elif res == False:
                    conn.send('Invalid Login Details'.encode(FORMAT))
                    print("yay")
            if msg[0] == 'signup':

                account_creation = con.insertUsers(msg[1:])
                if account_creation == "Done":
                    conn.send("Account created Sucessfully".encode(FORMAT))
                    print(f"[ALERT]:{addr} created account successfully")
                elif account_creation == "Duplicate id":
                    conn.send("Account already exist".encode(FORMAT))
                    print(f"[ALERT]:{addr} duplicate account detected")


            if msg[0] == "logout":  # logs out
                conn.send(f"{addr} logged out successfully".encode(FORMAT))
                login = False

            if login is True:  # allow certain actions when user has logged in
                if msg[0] == 'viewElection':  # checks available elections
                    conn.send(str(election).encode(FORMAT))

                if msg[0] == 'selectElection':  # selects election
                    election_id = election[msg[1]][0]
                    conn.send(f"{election_id} selected successfully".encode(FORMAT))
                    print(f"[ALERT]:{addr} selected electionid {election[msg[1]][0]}")

            if msg[0] == DISCONNECT_MESSAGE:
                connected = False
    except SyntaxError:
        pass

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
