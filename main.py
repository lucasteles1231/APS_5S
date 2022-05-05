import eel
import socket
import threading

# inicia o client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Directories and files
base_directory = "web/pages/"
delay = 0.1

# Screen routes
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


# Applications functions

@eel.expose
def authenticate(usuario, senha):
  return True

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
def sendMessage():
  print("teste")

@eel.expose
def onReceiveMessage():
  print("teste")

@eel.expose
def registerNewUser(name, email, password, userType):
  print(name, email, password, userType)

# Start
eel.init("src")

eel.start(base_directory + 'login.html')