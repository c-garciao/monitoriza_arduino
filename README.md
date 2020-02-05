# Proyecto monitorización sala de servidores
Monitorización de múltiple parámetros en una sala pequeña de servidores (casera en este caso). El proyecto pretende recoger, procesar y mostrar la información obtenida. Además, dicha información será tratada (notificar en caso de mediciones altas, etc).

## Herramientas necesarias

* Arduino (nano en este caso)
  * Librerías necesarias
      * [_Adafruit Sensor_](https://github.com/adafruit/Adafruit_Sensor)
      * [_DHT Sensor Library_](https://github.com/adafruit/DHT-sensor-library)
 * Python versión 3.7 o superior
   * Librería necesaria
     * [_PySerial_](https://pypi.org/project/pyserial/)
## Funcionamiento
Una vez instaladas las librerías necesarias, se debe ejecutar _Leer_arduino.py_ o _Leer_arduino.pyw_, dependiendo si se trata de consola o interfaz gráfica respectivamente.
### Interfaz Web
El programa también muestra los resultados en un archivo html, el cual se actualiza dinámicamente gracias a un script escrito en _JQuery_:

![Captura_arduino](https://user-images.githubusercontent.com/51420640/73871014-51c88980-484d-11ea-8397-5d0f4bb54e64.PNG)

## Tareas pendientes
[x] ~~Actualizar de forma dinámica el contenedor~~
- [ ] Mejorar y añadir más contenido a la versión web
- [ ] Mejorar el rendimiento de la interfaz gráfica
- [ ] Añadir más lecturas
- [ ] Limpiar el código
- [ ] Comunicación remota con el arduino

## Autor

* **Carlos Garcia** - *Autor* - [c-garciao](https://github.com/c-garciao)
