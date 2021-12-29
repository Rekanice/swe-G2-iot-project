#include <Arduino.h>
#include <ESP8266WiFi.h>      

// Wifi credentials
const char *ssid = "change_this"; 
const char *password = "filler_pwd";  

// LDR pins
#define LDR 5
#define LED 4

// Function declarations
void setEspPins();
void startWifi();

void setup() {

  setEspPins();
  Serial.begin(115200); 
  startWifi();
}

void loop() {
  if(digitalRead(LDR) == 1) // if ldr sensor's digital input is high
  {
    // send "WM is busy" message to flask server, and then periodic deep sleep 
    Serial.println("There's light!");
  }
  else{
    // send "WM is done" message to flask server
    Serial.println("It's dark!");
  }
}

void startWifi() {  
  
  WiFi.begin(ssid, password);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");
  
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());             // Tell us what network we're connected to
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());          // Send the IP address of the ESP8266 to the computer
  
}

void setEspPins() {
  pinMode(LDR, INPUT);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
}
