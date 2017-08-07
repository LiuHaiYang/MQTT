import paho.mqtt.client as mqtt  
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code "+str(rc))  

def on_message(client, userdata, msg):  
    print(msg.topic+" "+str(msg.payload))  
  
client = mqtt.Client()  
client.on_connect = on_connect  
client.on_message = on_message  
  
client.connect("172.16.100.188", 1883, 60)  
client.subscribe("lettuce",0)  
client.loop_forever()  