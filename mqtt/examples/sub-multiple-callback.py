import sys
try:
    import paho.mqtt.client as mqtt
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.client"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt

def on_message_msgs(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/messages/#
    print("MESSAGES: "+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_message_bytes(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/bytes/#
    print("BYTES: "+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_message(mosq, obj, msg):
    # This callback will be called for messages that we receive that do not
    # match any patterns defined in topic specific callbacks, i.e. in this case
    # those messages that do not have topics $SYS/broker/messages/# nor
    # $SYS/broker/bytes/#
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

mqttc = mqtt.Client()

# Add message callbacks that will only trigger on a specific subscription match.
mqttc.message_callback_add("$SYS/broker/messages/#", on_message_msgs)
mqttc.message_callback_add("$SYS/broker/bytes/#", on_message_bytes)
mqttc.on_message = on_message
mqttc.connect("172.16.100.188", 1883, 60)
mqttc.subscribe("$SYS/#", 0)

mqttc.loop_forever()

