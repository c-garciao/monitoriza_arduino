import serial, time, os.path, subprocess
from tkinter import *
from os import path
raiz=Tk()
raiz.title("Sensor DHT11")
raiz.geometry("240x240")
raiz.resizable(False,False)
texto1=Label(text="Humedad").grid(pady=5, row=0, column=0)
texto2=Label(text="Temperatura").grid(pady=5, row=1, column=0)
botonWeb=Button(text="Ver en web", command=subprocess.call([sys.executable,'web.html'])).grid(pady=5, row=2, column=2)
arduino = serial.Serial('COM7', 9600)
archivo="log.txt"
web="web.html"
if not os.path.exists(web):
    open(web, 'w').close()

def comprueba_archivo():
    if not os.path.isfile(archivo):
        open(archivo, 'rb+').close()
def recoger_arduino():
    datos = arduino.readline()
    print(datos)
    # comprueba_archivo
    # txt = open(archivo,'rb+')
    # txt.write(datos)
    # txt.close()
    humedad = datos.decode().split(';')[0]
    temperatura = datos.decode().split(';')[1]
    texto3=Label(text=humedad + '%').grid(pady=5, row=0, column=2)
    texto4=Label(text=temperatura + 'ºC').grid(pady=5, row=1, column=2)
    f = open(web,'w')
    mensaje="""<head><meta http-equiv="refresh" content="1"/><title>Medidas</title></head><body><h1>Humedad:"""
    mensaje+=humedad
    mensaje+="""</h1><br/><h1>Temperatura:"""
    mensaje+=temperatura
    mensaje+="""</body></html>"""
    f.write(mensaje)
    f.close
    raiz.after(1000, recoger_arduino)
raiz.wm_attributes("-topmost", 1)
raiz.after(2000, recoger_arduino)
raiz.mainloop()
