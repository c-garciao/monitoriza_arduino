import serial, time, os.path
from tkinter import *
raiz=Tk()
raiz.title("Sensor DHT11")
raiz.geometry("240x240")
raiz.resizable(False,False)
texto1=Label(text="Humedad").grid(pady=5, row=0, column=0)
texto2=Label(text="Temperatura").grid(pady=5, row=1, column=0)
arduino = serial.Serial('COM7', 9600)
archivo="log.txt"
def comprueba_archivo():
    if not os.path.isfile(archivo):
        open(archivo, 'rb+').close()
def recoger_arduino():
    datos = arduino.readline()
    print(datos)
    comprueba_archivo
    txt = open(archivo,'rb+')
    txt.write(datos)
    txt.close()
    humedad = datos.decode().split(';')[0]
    temperatura = datos.decode().split(';')[1]
    texto3=Label(text=humedad + '%').grid(pady=5, row=0, column=1)
    texto4=Label(text=temperatura + 'ºC').grid(pady=5, row=1, column=1)
    raiz.after(250, recoger_arduino)
raiz.after(250, recoger_arduino)
raiz.wm_attributes("-topmost", 1)
raiz.mainloop()
