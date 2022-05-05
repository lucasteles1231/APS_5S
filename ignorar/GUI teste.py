from tkinter import *
from win32api import GetMonitorInfo, MonitorFromPoint

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
task_bar = monitor_area[3] - work_area[3]

def Window(windowName, bg, Wwidth, Wheight):

    x = (work_area[2] - Wwidth)/2
    y = (work_area[3] - Wheight - 35)/2

    if Wheight > work_area[3] - 35:
        Wheight = work_area[3] - 35
        y = 0

    if Wwidth > work_area[2]:
        Wwidth = work_area[2]

    # Janela principal
    globals()[windowName] = Tk()

    # Titulo
    globals()[windowName].title("")

    # Remove titulo da janela
    globals()[windowName].overrideredirect(1)

    # Cor de Fundo da janela principal
    globals()[windowName].configure(background='#000')

    # Definir a cor de fundo da janela principal como transparente
    globals()[windowName].wm_attributes('-transparentcolor', globals()[windowName]['bg'])

    # Definir o tamanho da janela principal igual ao tamanho da tela do usuário
    globals()[windowName].geometry("%dx%d" % (work_area[2], work_area[3]))

    indexHexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    bgLight = '#'

    for i in list(bg[1:]):
        if i.lower() != 'f':
            bgLight = bgLight + indexHexa[indexHexa.index(i) + 1]
        if i.lower() == 'f':
            bgLight = bgLight + 'F'

    # Criar a barra de titulo dentro da janela principal
    framepadTop = Frame(globals()[windowName], width= Wwidth, height= y, background= globals()[windowName]['bg'])
    framepadTop.pack()

    # Criar a barra de titulo dentro da janela principal
    frametitlebar = Frame(globals()[windowName], width= Wwidth, height= 35, background= bgLight)
    frametitlebar.pack()

    # Criar um frame corpo dentro da janela principal 
    framebody = Frame(globals()[windowName], width= Wwidth, height= Wheight, background= bg)
    framebody.pack()

    globals()[windowName].mainloop()

Window('window', '#454545', 500, 500)