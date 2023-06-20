import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import time

client=mqtt.Client()
client.connect('mqtt brocker URL', 1883)
client.loop_start()

while True:
    _, temperature = dht.read_retry(dht.DHT11, 4)

    data = time.strftime('%y-%m-%d %H:%M:%S  ') + str(temperature) + '도'
    print(data)
    client.publish('topic/tmp', data, 1)
    time.sleep(1h)
