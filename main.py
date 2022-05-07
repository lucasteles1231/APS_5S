import eel
import socket
import threading

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


# FAZ AUTENTICAÇÃO DO USUARIO
@eel.expose
def authenticate(usuario, senha):
  global client
  client.send(str("#!usuario!##!senha!# " + str(usuario) + "  :  " + str(senha)).encode('UTF-8'))

  while True:
    try:
      message = client.recv(2048).decode('UTF-8')
      break
    except:
      pass
  return message

# INICIA CONEXÃO COM O SERVIDOR
@eel.expose
def startConnection(IpPort):
  global client
  try:
    ServerIP = str(IpPort).split(":")[0]
    PORT = str(IpPort).split(":")[1]
    client.connect((str(ServerIP), int(PORT)))
    return True
  except:
    return False


@eel.expose
def sendMessage(message):
  #global client
  #client.send(message.encode('UTF-8'))
  print("Send Message")


@eel.expose
def ReceiveMessage():
  print("Recive Message")


@eel.expose
def RegisterNewUser(name, email, password, userType):
  print("Register New User")

# Inicializa eel
eel.init("src")

# Começa o programa pela tela de login
eel.start(base_directory + 'login.html')
