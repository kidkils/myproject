#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <dht.h>
#define sensor 14
#define rainDigital D1

dht DHT;
const int sensor_pin = A0;

const char* ssid = "Agus purnawan";
const char* password = "nieAndra01";
const char* mqtt_server = "192.168.43.70";
const char* mqtt_user = "admin";
const char* mqtt_password = "12345coba";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  pinMode(rainDigital,INPUT);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  delay(500);
}

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client2", mqtt_user, mqtt_password)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
    
      // ... and resubscribe
      // client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
 
void loop() {
  if (!client.connected()) {
    reconnect();
  }
  int rainDigitalVal = analogRead(rainDigital);
  float moisture_percentage;
  moisture_percentage = ( 100.00 - ( (analogRead(sensor_pin)/1023.00) * 100.00 ) );
  DHT.read11(sensor);
  
  Serial.print("Kelembaban udara = ");
  Serial.print(DHT.humidity);
  Serial.print("% ");
  Serial.print("Suhu = ");
  Serial.print(DHT.temperature); 
  Serial.println(" C ");

  Serial.print("Soil Moisture(in Percentage) = ");
  Serial.print(moisture_percentage);
  Serial.println("%");

  if(rainDigitalVal < 1){
    Serial.print("sedang hujan = ");
    Serial.print(rainDigitalVal);
  }
  else {
    Serial.print("tidak hujan = ");
    Serial.print(rainDigitalVal);
  }
 
  if(client.publish("kelembapan-node2", String(DHT.humidity).c_str())){
    Serial.print("kelembapan telah dikirm");
    Serial.println();
  } 
  else{
    Serial.print("kelembapan gagal dikirm");
    client.connect("ESP8266Client2", mqtt_user, mqtt_password);
    delay(10);
    client.publish("kelembapan-node2", String(DHT.humidity).c_str());
  }
 
  if(client.publish("suhu-node2", String(DHT.temperature).c_str())){
    Serial.print("suhu telah dikirm");
    Serial.println();
  } 
  else{
    Serial.print("suhu gagal dikirm");
    client.connect("ESP8266Client2", mqtt_user, mqtt_password);
    delay(10);
    client.publish("suhu-node2", String(DHT.temperature).c_str());
  }
  
  if(client.publish("moisture-node2", String(moisture_percentage).c_str())){
    Serial.print("moisture telah dikirm");
    Serial.println();
  } 
  else{
    Serial.print("moisture gagal dikirm");
    client.connect("ESP8266Client2", mqtt_user, mqtt_password);
    delay(10);
    client.publish("moisture-node2", String(moisture_percentage).c_str());
  }
  
  if(client.publish("hujan-node2", String(rainDigitalVal).c_str())){
    Serial.print("hujan telah dikirm");
    Serial.println();
  } 
  else{
    Serial.print("hujan gagal dikirm");
    client.connect("ESP8266Client2", mqtt_user, mqtt_password);
    delay(10);
    client.publish("moisture-node2", String(rainDigitalVal).c_str());
  }

  Serial.println("");
  delay(2000);

  client.loop();
 
}
