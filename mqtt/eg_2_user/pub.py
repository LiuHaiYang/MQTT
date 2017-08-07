import paho.mqtt.publish as publish

# publish a message then disconnect.
host = "172.16.100.188"
topic = "tw/rocksaying"
payload = "hello mqtt"

# If broker asks user/password.
auth = {'username': "wugeek", 'password': "111111"}

# If broker asks client ID.
#client_id = ""

#publish.single(topic, payload, qos=1, hostname=host)

publish.single(topic, payload, qos=1, hostname=host,auth=auth)