import serial, time, os.path, subprocess, webbrowser
from tkinter import *
from os import path
raiz=Tk()
arduino = serial.Serial('COM7', 9600)
archivo="log.txt"
web="web.html"
def abre_web():
    webbrowser.open_new_tab(web)
raiz.title("Sensores")
raiz.geometry("240x240")
raiz.resizable(False,False)
texto1=Label(text="Humedad").grid(pady=5, row=0, column=0)
texto2=Label(text="Temperatura").grid(pady=5, row=1, column=0)
botonWeb=Button(text="Ver en navegador", command=abre_web).grid(pady=5, row=2, column=2)

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
    mensaje="""<head><script type="text/javascript" src="funciones.js"></script><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script><meta charset="UTF-8"></meta><title>Medidas</title></head><body><div id="contenedor"><h1>Humedad:"""
	#<meta http-equiv="refresh" content="1"/>
    mensaje+=humedad
    mensaje+="""&#37;</h1><h1>Temperatura:"""
    mensaje+=temperatura
    mensaje+="""&#186;C</div></body></html>"""
    f.write(mensaje)
    f.close
    raiz.after(1000, recoger_arduino)
raiz.wm_attributes("-topmost", 1)
raiz.after(2000, recoger_arduino)
raiz.mainloop()
