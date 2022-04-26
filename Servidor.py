import socket
import threading
import mysql.connector


HOST = input("Host: ")
PORT = int(input("Port: "))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f'Server is Up and Listening on {HOST}:{PORT}')

clients = []
usernames = []

def dadosDB(id, client):
    con = mysql.connector.connect(host='localhost', database='MYSQL_PYTHON',user='root',password='root')
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Tabela_Dados WHERE ID = {id};")
        result = cursor.fetchall()
        if len(result) == 1:
            getDB(f'{usernames[clients.index(client)]}: || {result[0][0]} || {result[0][1]} || {result[0][2]} || {result[0][3]} || {result[0][4]} || {result[0][5]} ||'.encode('UTF-8'))
        else:
            getDB(f'{usernames[clients.index(client)]}: ID inválido'.encode('UTF-8'))

def globalMessage(message):
    for client in clients:
        if usernames[clients.index(client)] != message[:len(usernames[clients.index(client)])].decode('UTF-8'):
            client.send(message)

def getDB(message):
    for client in clients:
        if usernames[clients.index(client)] == message[:len(usernames[clients.index(client)])].decode('UTF-8'):
            message = message.decode('UTF-8')[len(usernames[clients.index(client)])+2:].encode('UTF-8')
            client.send(message)


def handleMessages(client):
    while True:
        try:
            receiveMessageFromClient = client.recv(2048).decode('UTF-8')
            if receiveMessageFromClient[:5] == "getid":
                try:
                    dadosDB(receiveMessageFromClient[6:], client)
                except:
                    print(f"não achou o ID solicitado por {usernames[clients.index(client)]}")
            else:
                globalMessage(f'{usernames[clients.index(client)]}: {receiveMessageFromClient}'.encode('UTF-8'))
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} has left the chat...')
            globalMessage(f'{clientLeavedUsername} has left us...'.encode('UTF-8'))
            usernames.remove(clientLeavedUsername)


def initialConnection():
    while True:
        try:
            client, address = server.accept()
            clients.append(client)
            client.send('getUser'.encode('UTF-8'))
            username = client.recv(2048).decode('UTF-8')
            if not username in usernames:
                usernames.append(username)
                globalMessage(f'{username} just joined the chat!'.encode('UTF-8'))
                user_thread = threading.Thread(target=handleMessages,args=(client,))
                user_thread.start()
                print(f"New Connetion: {str(address)}")
            else: 
                clients.remove(client)
                client.send('Name already exists on the server'.encode('UTF-8'))
                client.close()
        except:
            pass

initialConnection()