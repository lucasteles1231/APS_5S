from traceback import print_tb
import eel
import socket
import threading
import pyautogui

stopWhile = True

porta = int(input('PORT: '))

contacts = list()

name = list()

# Inicia o Client Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# EXECUTA COMANDOS DE INICIALIZAÇÃO
@eel.expose
def onStart():
  pyautogui.hotkey('winleft', 'up')




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

  name = [message, message[:1]]
  return message

@eel.expose
def Name():
  global name
  return name

##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##




###################### CHAT ########################


@eel.expose
def Contacts():
  global client
  global name
  message = "#!getContacts!#"
  client.send(message.encode('UTF-8'))
  while True:
    try:
      message = client.recv(2048).decode('UTF-8')
      break
    except:
      pass
  message = message.split("  :  ")
  message.remove("")
  message.remove(name[0])
  return message

@eel.expose
def SendMessage(message, sendTo):
  global client
  global name
  message = str("#!chat!# " + str(name[0]) + "  :  " + str(sendTo) + "  :  " + str(message))
  client.send(message.encode('UTF-8'))
  
@eel.expose
def initThread():
  thread1 = threading.Thread(target=ReceiveMessage,args=())
  thread1.start()

@eel.expose
def stopWhile():
  global stopWhile
  stopWhile = False

@eel.expose
def ReceiveMessage():
  global stopWhile
  while stopWhile:
    try:
      msg = (client.recv(2048).decode('UTF-8'))
      print('recebeu msg')
      name = msg.split("  :  ")[0]
      msg = msg.split("  :  ")[1]
      data = [msg, name]
      eel.receiveMessage(data)
    except:
      pass



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
  msg = "#!quit!# " + str(name[0])
  client.send(msg.encode('UTF-8'))
  client.close()
  stopWhile = False
  print ('Closed!!')
except:
  stopWhile = False
  print ('Closed!!')
