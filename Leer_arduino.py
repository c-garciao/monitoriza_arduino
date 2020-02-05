# -*- coding: utf-8 -*-
#
import serial, time
arduino = serial.Serial('COM7', 9600)
time.sleep(2)
while  True:
    datos = arduino.readline()
    humedad = datos.decode().split(';')[0]
    temperatura = datos.decode().split(';')[1]
    print ("Humedad " + humedad + "%")
    print ("Temperatura: " + temperatura +" ºC")