import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    if rc == 0:
        print("connected ok")
        client.subscribe("my/test/topic")
        client.subscribe("$SYS/#")
    else:
        pass

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message: "+msg.topic+" "+str(msg.payload))

client = mqtt.Client("python1")
client.on_connect = on_connect
client.on_message = on_message
client.tls_set()
client.username_pw_set(username="jackANDj1ll", password="pangaeaQWSA1")

print("started...")
client.connect("d45fff2751494701a6007b82c596c0bc.s1.eu.hivemq.cloud", 8883, 60)
client.loop_forever()