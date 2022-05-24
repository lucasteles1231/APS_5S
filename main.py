from pydoc import cli
from tkinter import E
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

# EXECUTA COMANDOS DE INICIALIZAÇÃO




####################################################
########## FUNÇÕES EEL CHAMADAS PELO JS ############
####################################################

# Tela Cheia
@eel.expose
def onStart():
  pyautogui.hotkey('winleft', 'up')


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
  global client
  global stopWhile
  num = 0
  while stopWhile:
    try:
      msg = (client.recv(2048).decode('UTF-8'))
      print(msg)

      #Login
      if msg[:10] == "#!login!# ":
        msg = msg[10:]
        name = msg
        msg = msg + "  :  " + msg[:1]
        print(msg)
        eel.receiveMessage(msg, "login")

      #Cadastro Despejo
      elif msg[:13] == "#!cadastro!# ":
        msg = msg[13:]
        eel.receiveMessage(msg, "cadastro")

      #Chat
      elif msg[:9] == "#!chat!# ":
        msg = msg[9:]
        eel.receiveMessage(msg, "chat")
        num += 1

      #Dashboard
      elif msg[:14] == "#!dashboard!# ":
        msg = msg[14:]
        print(msg)
        if msg == "fim  :  fim":
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