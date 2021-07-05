import paho.mqtt.client as mqtt

class SubscribeService(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        print("Connected with result code " + str(rc))
        self.subscribe("my/test/topic")

    def on_message(self, mqttc, obj, msg):
        print("[Recieved]: Topic: "+msg.topic+" ; retainFlag: " + str(msg.retain) + " ; message: "+str(msg.payload.decode("utf-8")))

    def on_log(self,mqttc, obj, level, string):
        print("[log]:" + string)

    def run(self,
            brokerhostname:str,
            brokerport:int,
            credusername:str,
            credpassword:str
            ):
        self.tls_set()
        #self.subscribe("my/test/topic")
        self.username_pw_set(username=credusername, password=credpassword)
        self.connect(brokerhostname, brokerport, 120)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc


instance1 = SubscribeService()

# TODO: Change below line to read from config file.
rc = instance1.run("[hostname]", [port num], "[broker username]", "[broker password]")
print (str(rc))
