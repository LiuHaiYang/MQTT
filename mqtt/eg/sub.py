import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("chat")


def on_message(client, userdata, msg):
    #print(msg.topic+":"+str(msg.payload.decode()))
    #print(msg.topic+":"+msg.payload.decode())
    payload = json.loads(msg.payload.decode())
    print(payload.get("user")+":"+payload.get("say"))


if __name__ == '__main__':
    client = mqtt.Client()
    #client.username_pw_set("wugeek", "1111")
    client.on_connect = on_connect
    client.on_message = on_message

    HOST = "172.16.100.188"

    client.connect(HOST, 1883, 10)
    #client.loop_forever()

    user = input("请输入名称:")
    client.user_data_set(user)

    client.loop_start()

    while True:
        str = input()
        if str:
            client.publish("chat", json.dumps({"user": user, "say": str}))