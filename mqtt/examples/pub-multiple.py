import sys
try:
    import paho.mqtt.publish as publish
except ImportError:
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.publish as publish

msgs = [{'topic':"paho/test/multiple", 'payload':"multiple 1"}, ("paho/test/multiple", "multiple 2", 0, False)]
publish.multiple(msgs, hostname="172.16.100.188")
