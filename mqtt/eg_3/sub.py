import sys
import paho.mqtt.client as mqtt
def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))
def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.username_pw_set('wugeek', '111111')
mqttc.connect("172.16.100.188", 1883, 60)
mqttc.subscribe("hello/world")
mqttc.loop_forever()

