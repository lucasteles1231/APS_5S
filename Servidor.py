import socket
import threading
import time
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
            user_thread = threading.Thread(target=ClientMessages,args=(client, address), name="t2")
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
            print(msg)



            ########### LOGIN VALIDATION ############
            
            # Se a mensagem vier com "#!usuario!##!senha!# " no inicio será considerada como dados de login para validação
            if msg[:10] == "#!login!# ":
                msg = msg[10:]
                username = msg.split("  :  ")[0]
                password = msg.split("  :  ")[1]
                response = UserValidation(username, password)
                if response == 1:
                    msg = "#!login!# " + 'USER IS ALREADY CONNECTED'
                    client.send(msg.encode('UTF-8'))
                elif response == 2:
                    msg = "#!login!# " + 'USER DOES NOT EXIST'
                    client.send(msg.encode('UTF-8'))
                else:
                    msg = "#!login!# " + response
                    print(1)
                    client.send(msg.encode('UTF-8'))
                    print(2)
                    nome = response.split("  :  ")[0]
                    print(3)
                    SendMessage(f"#!chat!# {str(nome)} joined the chat!!  :  Servidor", client)
                    print(4)
                    usernames.append(nome)
                    print(5)
                    clients.append(client)
                    print(6)
                    print(f"{str(nome)} completed connection via login!!")


            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#



            ########### CHAT ############

            elif msg[:9] == "#!chat!# ":
                name = usernames[clients.index(client)]
                msg =  msg + "  :  "+ name
                SendMessage(msg, client)

            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#

            ########### CADASTRO DE DESPEJOS ############

            elif msg[:13] == "#!cadastro!# ":
                msg = msg[13:]
                msg = str(msg).split("  :  ")

                msg = "#!cadastro!# " + str(CadDespejo(msg[0], msg[1], msg[2], msg[3], msg[4]))
                client.send(msg.encode("UTF-8"))

            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#

            ########### COLETAR DADOS DA TABELA DESPEJOS ############

            elif msg[:14] == "#!dashboard!# ":
                rows = GetDespejo()
                if rows != "vazio":
                    for row in rows:
                        msg = "#!dashboard!# " + row
                        time.sleep(0.1)
                        client.send(msg.encode('UTF-8'))
                else:
                    msg = "#!dashboard!# " + "vazio"
                    client.send(msg.encode('UTF-8'))

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
            if not str(result[0]).replace('(','').replace(')','').split(',')[4].replace(' \'','').replace('\'', '') in usernames:
                msg = str(str(result[0]).replace('(','').replace(')','').split(',')[4].replace(' \'','').replace('\'', '')) + "  :  " + str(str(result[0]).replace('(','').replace(')','').split(',')[1].replace(' \'','').replace('\'', ''))
                return msg
            else:
                return 1
        else:
            return 2

# Manda mensagem para o contato
def SendMessage(msg, client):
    for i in clients:
        if i != client:
            i.send(msg.encode('UTF-8'))

# Cadastra despejo no banco de dados
def CadDespejo(company, typeEviction, qty, region, description):
    global con
    try:
        if con.is_connected():
            cursor = con.cursor()
            cursor.execute(f'INSERT INTO DESPEJOS(ID_DESPEJOS, TIPO_DESPEJO, EMPRESA, REGIAO, DESCRICAO, QUANTIDADE) VALUES (null, "{typeEviction}", "{company}", "{region}", "{description}", {qty});')
            con.commit()
            return "true"
    except:
        return "false"

# Retorna dados existentes na tabela despejos
def GetDespejo():
    global con
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM DESPEJOS;")
        result = cursor.fetchall()
        rows = list()
        if len(result) != 0:
            rows.append(f"num  :  {len(result)}")
            for row in result:
                row = str(row).replace('(','').replace(')','').replace(' \'','').replace('\'', '').split(',')
                id = row[0]
                typeEviction = row[1]
                company = row[2]
                region = row[3]
                description = row[4]
                qty = row[5]
                msg = id + "  :  " + company + "  :  " + typeEviction + "  :  " + qty + "  :  " + region + "  :  " + description
                rows.append(msg)
            rows.append("fim  :  fim")
            return rows
        else:
            return "vazio"

########### INICIO (AGUARDA A CONEXÃO COM O CLIENTE) ##############
initialConnection()
#################################
