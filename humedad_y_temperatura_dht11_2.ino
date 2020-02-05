#include <Adafruit_Sensor.h>
#include <DHT_U.h>
#define DHTPIN 2
#define DHTTYPE    DHT11     // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}
void loop() {
  delay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println("Error en la lectura");
    return;
  }
  Serial.print(h);
  Serial.print(";");
  Serial.print(t);
  Serial.print('\n');
}