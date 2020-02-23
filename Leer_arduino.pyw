# -*- coding: utf-8 -*-
import serial, time, os.path, subprocess, webbrowser
from tkinter import *
from os import path
raiz=Tk()
arduino = serial.Serial('COM6', 9600)
archivo="log.txt"
web="index.html"
datos_texto="prueba.txt"
def abre_web():
    webbrowser.open_new_tab(web)
raiz.title("Sensores")
raiz.geometry("240x240")
raiz.resizable(False,False)
texto1=Label(text="Humedad").grid(pady=5, row=0, column=0)
texto2=Label(text="Temperatura").grid(pady=5, row=1, column=0)
botonWeb=Button(text="Ver en navegador", command=abre_web).grid(pady=5, row=2, column=2)
def recoger_arduino():
    datos = arduino.readline()
    print(datos)
    f = open('datos.txt','wb')
    f.write(datos)
    f.close
    humedad = datos.decode().split(';')[0]
    temperatura = datos.decode().split(';')[1]
    texto3=Label(text=humedad + '%').grid(pady=5, row=0, column=2)
    texto4=Label(text=temperatura + 'ºC').grid(pady=5, row=1, column=2)
    raiz.after(1000, recoger_arduino)
def on_closing():
    raiz.destroy()
raiz.wm_attributes("-topmost", 1)
raiz.after(2000, recoger_arduino)
raiz.protocol("WM_DELETE_WINDOW", on_closing)
raiz.mainloop()
