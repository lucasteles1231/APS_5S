import eel
import socket
import threading
import pyautogui

stopWhile = True

porta = int(input('PORT: '))

name = ""

# Inicia o Client Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

rows = list()

tamrows = 0

screen = ""

ip = ""
port = ""

nivel = ""

# EXECUTA COMANDOS DE INICIALIZAÇÃO




####################################################
########## FUNÇÕES EEL CHAMADAS PELO JS ############
####################################################

# INICIO
@eel.expose
def onStart():
  global screen
  global name
  global ip
  global port
  global nivel
  dados = [screen, name, ip, port, nivel]
  if screen == "":
    pyautogui.hotkey('winleft', 'up')
    screen = "login"

  return dados

@eel.expose
def SaveScreen(Screen):
  global screen
  screen = Screen

#################### LOGIN #########################

# INICIA CONEXÃO COM O SERVIDOR
@eel.expose
def StartConnection(IpPort):
  global client
  global ip
  global port
  ip = str(IpPort).split(":")[0]
  port = str(IpPort).split(":")[1]
  try:
    ServerIP = str(IpPort).split(":")[0]
    PORT = str(IpPort).split(":")[1]
    client.connect((str(ServerIP), int(PORT)))
    return True
  except:
    return False

##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##


###################### CHAT ########################

# RECEBE MENSAGENS
@eel.expose
def initThread():
  t1 = threading.Thread(target=ReceiveMessage,args=(),name="t1")
  t1.start()

@eel.expose
def StopWhile():
  global stopWhile
  stopWhile = False

@eel.expose
def ReceiveMessage():
  global name
  global nivel
  global client
  global stopWhile
  global rows
  global tamrows
  while stopWhile:
    try:
      msg = (client.recv(2048).decode('UTF-8'))
      print(msg)

      #Login
      if msg[:10] == "#!login!# ":
        msg = msg[10:]
        if msg != "USER IS ALREADY CONNECTED" and msg != "USER DOES NOT EXIST":
          msg = msg.split("  :  ")
          name = msg[0]
          nivel = msg[1]
          msg = msg[0] + "  :  " + msg[0][:1] + "  :  " + msg[1]
        eel.receiveMessage(msg, "login")

      #Cadastro Despejo
      elif msg[:13] == "#!cadastro!# ":
        msg = msg[13:]
        eel.receiveMessage(msg, "cadastro")

      #Chat
      elif msg[:9] == "#!chat!# ":
        msg = msg[9:]
        eel.receiveMessage(msg, "chat")

      #Dashboard
      elif msg[:14] == "#!dashboard!# ":
        msg = msg[14:]
        if msg[:8] == "num  :  ":
          msg = msg[8:]
          tamrows = int(msg)
        elif msg == "fim  :  fim":
          if len(rows) == tamrows:
            eel.receiveMessage(rows, "dashboard")
          rows.clear()
        elif msg == "vazio":
          eel.receiveMessage(rows, "dashboard")
          rows.clear()
        else:
          rows.append(msg)
    except:
      pass



# ENVIA MENSAGENS
@eel.expose
def SendMessage(message, screen):
  global client
  print('entrou')
  message = str(f"#!{screen}!# " + str(message))
  client.send(message.encode('UTF-8'))

##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##





# Inicializa eel com o diretório base
eel.init("src")

try:
  # Inicia a aplicaçao utilizando um HTML como base para renderizar
  # as demais telas através da combinação das bibliotecas EEL + Jinja2
  eel.start('web/pages/controller.html', jinja_templates="web/pages", host="localhost", port=porta)
except (SystemExit, MemoryError, KeyboardInterrupt):
  pass

try:
  msg = "#!quit!# " + str(name)
  client.send(msg.encode('UTF-8'))
  client.close()
  stopWhile = False
  print ('Closed!!')
except:
  stopWhile = False
  print ('Closed!!')