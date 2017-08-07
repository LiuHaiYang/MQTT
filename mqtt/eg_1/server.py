import sys
import datetime
import socket, sys
import paho.mqtt.client as mqtt

#======================================================
def on_connect(mqttc, obj, rc):
    print("OnConnetc, rc: "+str(rc))

def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print("Log:"+string)

def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    print(strcurtime + ": " + msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    on_exec(str(msg.payload))

def on_exec(strcmd):
    print ("Exec:",strcmd)
    strExec = strcmd
    
#=====================================================
if __name__ == '__main__': 
    mqttc = mqtt.Client("mynodeserver")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log

    #strBroker = "localhost"
    strBroker = "172.16.100.188"

    mqttc.connect(strBroker, 1883, 60)
    mqttc.subscribe("/inode/mychannel", 0)
    mqttc.loop_forever()