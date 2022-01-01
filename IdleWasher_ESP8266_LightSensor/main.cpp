#include <Arduino.h>
#include <ESP8266WiFi.h>   
#include <ESP8266Ping.h> 
#include <string>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

// Wifi credentials
const char *ssid = "CHANGE ME"; 
const char *password = "CHANGE ME";  

// HTTP settings for LOCAL HOSTED Flask server
WiFiClient client;
const int portnum = 5000;
IPAddress server_ip("CHANGE ME");
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);
const char * server_url = "CHANGE ME";

// Ping a remote machine
IPAddress remote_ip("CHANGE ME");
// const char* remote_host = "";

// LDR pins
#define LDR 5
#define LED 4
uint8 gotLight;

// Function declarations
void setEspPins();
void startWifi();
void sendSensorData();
void pingHost();


void setup() {
  setEspPins();
  Serial.begin(115200); 
  startWifi();
  pingHost();
  Serial.println();
}

void loop() {

  // ldr sensor's digital input is low when light is detected (LDR indicator is off), 
  // high when dark (LDR indicator lights up). 
  // The LDR indicator & the digitalRead logic levels are inverse.
  if(digitalRead(LDR) == 1) 
  {
    // send "WM is done" message to flask server
    Serial.println("It's dark!");
    gotLight = 0;
  }
  else{
    // send "WM is busy" message to flask server, and then periodic deep sleep 
    Serial.println("There's light!");
    gotLight = 1;
  }

  // setupHttpClient();
  sendSensorData();
  delay(7000);

}


void startWifi() { 
  WiFi.config(server_ip, gateway, subnet);  // For local hosted server
  WiFi.mode(WIFI_STA);               // Specify Wifi connection mode
  WiFi.begin(ssid, password);        // Connect to the network, remains active until connected or specified max #attempts expired
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");
  
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) {   // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
    Serial.println(WiFi.status());
  }

  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());              // Tell us what network we're connected to
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());           // Send the IP address of the ESP8266 to the computer
  
}

void setEspPins() {  
  pinMode(LDR, INPUT);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
}

void sendSensorData(){

  HTTPClient http;
  http.begin(server_url);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  String requestData = "light=" + String(gotLight) + "&count=" + String(true);
  int httpCode = http.POST(requestData); //Send the request
  String payload = http.getString(); //Get the response payload
  Serial.println(httpCode); //Print HTTP return code
  http.end(); //Close connection
  Serial.println("Sent POST URLencoded request to server.");
  

  String jsonData;
  StaticJsonDocument<300> jb;
  jb["light"] = gotLight;
  jb["key"] = "value";
  serializeJson(jb, jsonData);

  http.addHeader("Content-Type", "application/json"); 
  httpCode = http.POST(jsonData); //Send the request
  payload = http.getString(); //Get the response payload
  Serial.println(httpCode); //Print HTTP return code
  http.end(); //Close connection
  Serial.println("Sent POST json request to server.");

  Serial.println();

} 

void pingHost() {
  Serial.print("Pinging host: ");
  Serial.println(remote_ip);

  if(Ping.ping(remote_ip)) {
    Serial.println("Success!!");
  } else {
    Serial.println("Error :(");
  }
}
