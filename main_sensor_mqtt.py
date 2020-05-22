import paho.mqtt.client as paho
import pigpio
import DHT22
from time import sleep

# Initiate GPIO for pigpio
pi = pigpio.pi()
# Setup the sensor
dht22 = DHT22.sensor(pi, 4) # use the actual GPIO pin name
dht22.trigger()
# We want our sleep time to be above 2 seconds.
sleepTime = 3
def readDHT22():
# Get a new reading
dht22.trigger()
# Save our values
humidity = '%.2f' % (dht22.humidity())
temp = '%.2f' % (dht22.temperature())
return (humidity, temp)
def on_connect(client, userdata, flags, rc):
    print("Connected, rc:"+str(rc))

def on_publish(client, userdata, mid):
    print("published, mid: "+str(mid))

client = paho.Client()
client.on_connect   = on_connect
client.on_publish   = on_publish


while True:
humidity, temperature = readDHT22()
hum=float(humidity)
temp= float(temperature)
mensaje="{\"humidity\":\"" + str(hum) + "\", \"temperature\":\"" + str(temp)+"\"}"
print("{humidity:" + str(hum) + ", temperature:" + str(temp)+"}")
#print("Temperature is: " + str(temp) + "C")
client.connect("localhost", 1883)
client.publish("sensor/temperatura", mensaje, qos=1)
client.disconnect()
sleep(sleepTime)