import paho.mqtt.client as mqtt
from paho.mqtt.subscribeoptions import SubscribeOptions
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time

# Subscriber section
def on_message(client, userdata, message):
    print ('Recieved data from AI: ' + str(message.payload))

broker_address = 'localhost'
client = mqtt.Client("client", protocol=mqtt.MQTTv5)
client.connect(broker_address)
client.on_message = on_message
client.subscribe('pipeline')
client.loop_forever()

# Publisher section
publish_properties = Properties(PacketTypes.PUBLISH)
publish_properties.ResponseTopic = 'pipeline'
publish_properties.CorrelationData = b"334"

client.publish('pipeline', "{\"predictions\": \"0.898451\"}", 1, properties=publish_properties)
print ("AI sent data to counter: " + "{\"predictions\": \"0.898451\"}")

