import socket
import threading
import mysql.connector

# Inicia servidor
while True:
    try:
        HOST = socket.gethostbyname(socket.gethostname())
        print(HOST)
        PORT = int(input("Port: "))
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((HOST,PORT))
        server.listen()
        print(f'Server is Up and Listening on {HOST}:{PORT} !!')
        break
    except:
        print(f'Unable to start server, try another IP and port!!')
        pass

# Faz conexão com o banco
while True:
    try:
        USERdb = input("User DB: ")
        PASSWORDdb = input("Password DB: ")
        con = mysql.connector.connect(host='localhost', database='APS_Ambiental',user=USERdb,password=PASSWORDdb)
        print(f'Data base is conected!!')
        break
    except:
        print(f'Invalid database username or password!!')
        pass

# Guarda endereço ip e nome dos usuarios
clients = []
usernames = []

# Inicia conexão Server-Client
def initialConnection():
    global clients
    global usernames
    while True:
        try:
            client, address = server.accept()
            user_thread = threading.Thread(target=ClientMessages,args=(client, address))
            user_thread.start()
            print(f"New Connetion: {str(address)}")
        except:
            pass

# Recebe mensagens do usuario
def ClientMessages(client, address):
    global usernames
    global clients
    while True:
        try:

            # Mensagem recebida do cliente
            msg = (client.recv(2048).decode('UTF-8'))



            ########### LOGIN VALIDATION ############
            
            # Se a mensagem vier com "#!usuario!##!senha!# " no inicio será considerada como dados de login para validação
            if msg[:21] == "#!usuario!##!senha!# ":
                msg = msg[21:]
                username = msg.split("  :  ")[0]
                password = msg.split("  :  ")[1]
                response = UserValidation(username, password)
                if response == 1:
                    client.send('USER IS ALREADY CONNECTED'.encode('UTF-8'))
                elif response == 2:
                    client.send('USER DOES NOT EXIST'.encode('UTF-8'))
                else:
                    client.send(f'{response}'.encode('UTF-8'))
                    usernames.append(response)
                    clients.append(client)
                    print(f"{str(response)} completed connection via login!!")


            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#



            ########### CHAT ############

            elif msg[:15] == "#!getContacts!#":
                msg = ""
                for names in usernames:
                    msg = msg + "  :  " + names
                client.send(msg.encode("UTF-8"))

            elif msg[:9] == "#!chat!# ":
                msg = msg[9:]
                name = msg.split("  :  ")[0]
                sendTo = msg.split("  :  ")[1]
                msg = msg.split("  :  ")[2]
                SendMessage(msg, clients[usernames.index(sendTo)], name)

            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#



            ########### CLOSE CLIENT ############

            elif msg[:9] == "#!quit!# ":
                username = msg[9:]
                print(f'{usernames[clients.index(client)]} has left the chat...')
                usernames.remove(usernames[clients.index(client)])
                clients.remove(clients[clients.index(client)])
                client.close()
            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        except:
            pass


# Valida o úsuario e senha
def UserValidation(user, password):
    global con
    global usernames
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM USUARIOS WHERE USUARIO = '{user}' AND SENHA = '{password}';")
        result = cursor.fetchall()
        if len(result) != 0:
            if not user in usernames:
                return str(result[0]).replace('(','').replace(')','').split(',')[4].replace(' \'','').replace('\'', '')
            else:
                return 1
        else:
            return 2

# Manda mensagem para o contato
def SendMessage(message, client, sendFrom):
    message = sendFrom + "  :  " + message
    client.send(str(message).encode('UTF-8'))


########### INICIO (AGUARDA A CONEXÃO COM O CLIENTE) ##############
initialConnection()
#################################
