import eel
import socket
import threading

stopWhile = True

porta = int(input('PORT: '))

contacts = list()

name = list()

# Inicia o Client Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Caminho base
base_directory = "web/pages/"
delay = 0.1

# Caminho das telas 
@eel.expose
def openPage(origin, destiny):
  opening = True

  eel.show(base_directory + destiny)

  while opening:
    eel.sleep(0.1)

    if len(eel._websockets) > 1:

      close_function = {
        "login.html": eel.closeLoginScreen,
        "chat.html": eel.closeChatScreen,
        "dashboard.html": eel.closeDashboardScreen,
        "cadastro.html": eel.closeCadastroScreen
      }[origin]

      close_function()()

      opening = False




####################################################
########## FUNÇÕES EEL CHAMADAS PELO JS ############
####################################################



#################### LOGIN #########################

# INICIA CONEXÃO COM O SERVIDOR
@eel.expose
def StartConnection(IpPort):
  global client
  try:
    ServerIP = str(IpPort).split(":")[0]
    PORT = str(IpPort).split(":")[1]
    client.connect((str(ServerIP), int(PORT)))
    return True
  except:
    return False


# FAZ AUTENTICAÇÃO DO USUARIO
@eel.expose
def Authenticate(usuario, senha):
  global client
  global name
  client.send(str("#!usuario!##!senha!# " + str(usuario) + "  :  " + str(senha)).encode('UTF-8'))

  while True:
    try:
      message = client.recv(2048).decode('UTF-8')
      break
    except:
      pass
  if message != 'USER IS ALREADY CONNECTED' and message != 'USER DOES NOT EXIST':
    thread1 = threading.Thread(target=ReceiveMessage,args=())
    thread1.start()
  name = [message, message[:1]]
  return message

@eel.expose
def Name():
  global name
  return name

##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##




###################### CHAT ########################


@eel.expose
def SendMessage(message, sendTo):
  global client
  global name
  message = str("#!chat!# " + str(name[0]) + "  :  " + str(sendTo) + "  :  " + str(message))
  client.send(message.encode('UTF-8'))

def ReceiveMessage():
  global stopWhile
  while stopWhile:
    try:
      msg = (client.recv(2048).decode('UTF-8'))
      name = msg.split("  :  ")[0]
      msg = msg.split("  :  ")[1]
      data = [msg, name]
      eel.receiveMessage(data)
    except:
      pass



##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##


# Inicializa eel
eel.init("src")

try:
  # Começa o programa pela tela de login
  eel.start(base_directory + 'login.html', mode='chrome', host='localhost', port=porta)
except (SystemExit, MemoryError, KeyboardInterrupt):
  pass

try:
  msg = "#!quit!# " + str(name[0])
  client.send(msg.encode('UTF-8'))
  client.close()
  stopWhile = False
  print ('Closed!!')
except:
  stopWhile = False
  print ('Closed!!')