import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.username_pw_set('wugeek', '111111')
mqttc.connect('172.16.100.188', 1883)
# Publish a message
mqttc.publish("hello/world", "my message",0)