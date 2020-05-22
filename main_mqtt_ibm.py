import requests 
import paho.mqtt.client as mqtt 
import time 
import json 

def sendWatsonIbm(jsonString):
    
    payloadJson = json.loads(jsonString)
    print("Se mando llamar: " , payloadJson)
    payload =  {"humidity": 0, "temperature": 0}
    payload["humidity"] = float(payloadJson["humidity"])
    payload["temperature"] = float(payloadJson["temperature"])
    print(">>>>" , payload)
    response = requests.post(url, json=payload,headers=headers)
    if response.status_code==200:
        print('La peticion fue correcta')
    else: 
        print("Error" , response.status_code)


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    
    sendWatsonIbm(str(message.payload.decode("utf-8")))
 
if __name__=='__main__':
    url = 'https://teonq3.messaging.internetofthings.ibmcloud.com/api/v0002/device/types/sensores/devices/rpbroker/events/temperatura'
    headers = {'Authorization': 'Basic dXNlLXRva2VuLWF1dGg6NTF6KEJ5alA/aF9GdDk1bms2','Content-Type': 'application/json'}
    # Datos del Moquitto
    host = '127.0.0.1' 
    topic = 'temperatura'


    print("creating new instance")
    client = mqtt.Client("P1") #create new instance
    client.on_message=on_message #attach function to callback
    print("connecting to broker")
    client.connect(host) #connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","sensor/temperatura")
    client.subscribe("sensor/"+topic)
    time.sleep(40) # wait
    client.loop_stop() #stop the loop

    
    
    
    
