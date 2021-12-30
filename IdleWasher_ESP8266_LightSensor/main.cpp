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
  // ldr sensor's digital input is low when light is detected (LDR indicator is off), 
  // high when dark (LDR indicator lights up). 
  // The LDR indicator & the digitalRead logic levels are inverse.
  if(digitalRead(LDR) == 1) 
  {
    // send "WM is done" message to flask server
    Serial.println("It's dark!");
  }
  else{
    // send "WM is busy" message to flask server, and then periodic deep sleep 
    Serial.println("There's light!");
  }
}

void startWifi() {  
  WiFi.mode(WIFI_STA);               // Specify Wifi connection mode
  WiFi.begin(ssid, password);        // Connect to the network, remains active until connected  or specified max #attempts to expire
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
