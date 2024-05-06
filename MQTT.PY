import paho.mqtt.client as mqtt
import json
import time

broker_address = "localhost"
port = 1883
topic = "sensor_data"

# Connexion au broker MQTT
client = mqtt.Client()
client.connect(broker_address, port)

while True:
    sensor_data = {
        "temperature": 25.5,
        "humidity": 50
    }

    client.publish(topic, json.dumps(sensor_data))
    
    time.sleep(5)