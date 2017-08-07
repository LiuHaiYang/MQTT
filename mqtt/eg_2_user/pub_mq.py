import sys, os, time
import paho.mqtt.client as mqtt
client = mqtt.Client()
# If broker asks client ID.
#client_id = ""

#client = mqtt.Client(client_id=client_id)

# If broker asks user/password.
user = "wugeek"
password = "111111"
client.username_pw_set(user, password)
client.connect("172.16.100.188")
topic = "tw/rocksaying"
payload = "hello mqtt"

for i in range(10):
    client.publish(topic, "%s - %d" % (payload, i))
    time.sleep(2)