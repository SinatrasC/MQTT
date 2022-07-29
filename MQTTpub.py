import paho.mqtt.client as mqtt

#MQTT 3.1.1

client = mqtt.Client()
#client.username_pw_set("peresthayal", "123456")
client.connect("localhost",1883,60)

client.publish("test", "Hello world 2!")
client.disconnect()