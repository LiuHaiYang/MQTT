import datetime
import socket, sys
import paho.mqtt.publish as publish

def transmitMQTT(strMsg):
    strBroker = "172.16.100.188"
    strMqttChannel = "/inode/mychannel"
    print(strMsg)
    publish.single(strMqttChannel, strMsg, hostname = strBroker)

if __name__ == '__main__':
    transmitMQTT("Hello,MQTT Proxy, I am client inside python.")
    print ("Send msg ok.")