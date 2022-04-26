import socket
import threading
import sys

# var para coletar IPV4 do servidor
ServerIP = input("Server IP: ")

# var para coletar porta aberta no servidor
PORT = int(input("Port: "))

# inicia o client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # var que recebe o nome escolhido pelo usuário
    username = input('Enter a username: ')

    # inicia a conexão com o servidor 
    client.connect((ServerIP, PORT))

    # se a conexão der certo printa que a conexão deu certo, IP e porta da conexão
    print(f'Connected Successfully to {ServerIP}:{PORT}')
except:

    # se a conexão falhar entra num loop dizendo que teve erro na conexão
    print(f'ERROR: Please review your input: {ServerIP}:{PORT}')


# função para receber a mensagem
def receiveMessage():
    while True:
        try:
            # var que recebe a mensagem vinda do servidor decodificada
            message = client.recv(2048).decode('UTF-8')

            # envia o nome do usuário para servidor
            if message=='getUser':
                client.send(username.encode('UTF-8'))
            
            elif message=='Name already exists on the server':
                print(message)
                client.close()
            else:
                print(message)
        except:
            print('ERRO')
            break

def sendMessage():
    while True:
        client.send(input().encode('UTF-8'))

thread1 = threading.Thread(target=receiveMessage,args=()) 
thread2 = threading.Thread(target=sendMessage,args=())

thread1.start()
thread2.start()