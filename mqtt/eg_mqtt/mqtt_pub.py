import paho.mqtt.client as mqtt      
mqttc = mqtt.Client()  
mqttc.connect("172.16.100.188", 1883, 60)    
mqttc.publish("lettuce", "Hello, World baby!",0)  