# Monitoring Multiple Data Sensor Using Portable Server and Webserver

# requirement Hardware
1. rasberry Pi3//4
2. node ESP8266
3. sensor rain, moisture, DHT11
4. power for every node

# requirement Software
1. OS raspberry Pi
2. installing influxdb
3. installing erlang
4. installing rabbitmq
5. arduino IDE
6. flask micro freamwork

# install influxdb
> https://otodiginet.com/database/how-to-install-influxdb-on-ubuntu-20-04-lts/

# install erlang
- sudo apt-get update
- sudo apt-get install erlang

> https://www.erlang.org/downloads

# install rabbitmq
> https://computingforgeeks.com/how-to-install-latest-rabbitmq-server-on-ubuntu-linux/

# install flask micro freamwork
> https://flask.palletsprojects.com/en/1.1.x/installation/

# enable moduls mqtt below on linux terminal
$rabbitmq-plugins enable rabbitmq_management rabbitmq_management_agent rabbitmq_mqtt rabbitmq_web_mqtt rabbitmq_web_mqtt_examples

# run rabbitmq server
$ sudo rabbitmq-server

# make config file location
1. enter the directory rabbitmq /etc/rabbitmq
2. make a file config with nano rabbitmq.conf
```
mqtt.default_user     = admin
mqtt.default_pass     = 12345coba
mqtt.allow_anonymous  = true
mqtt.vhost            = /
mqtt.exchange         = test-exchange
# 24 hours by default
mqtt.subscription_ttl = 86400000
mqtt.prefetch         = 10
mqtt.listeners.ssl    = none
## Default MQTT with TLS port is 8883
# mqtt.listeners.ssl.default = 8883
mqtt.listeners.tcp.default = 1883
mqtt.tcp_listen_options.backlog = 128
mqtt.tcp_listen_options.nodelay = true
```
