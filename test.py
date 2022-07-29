import sys
import paho.mqtt.client as mqtt
from paho.mqtt.subscribeoptions import SubscribeOptions
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time

# Subscriber section
def on_message(client, userdata, message):
    print ('Recieved data from AI: ' + str(message.payload))
    # take timestamp of message
    timestamprecieved = time.time()
    #find time difference between timestampsent and timestamprecieved
    timediff = timestamprecieved - timestampsent
    #print timediff as ms
    print ('Time difference: ' + str(timediff*1000))

broker_address = 'localhost'
client = mqtt.Client("client", protocol=mqtt.MQTTv5)
#client.username_pw_set("cedalo", "RMY8WQZubP")
client.connect(broker_address)
client.on_message = on_message
client.subscribe('pipeline')

# Publisher section
publish_properties = Properties(PacketTypes.PUBLISH)
publish_properties.ResponseTopic = 'pipeline'
publish_properties.CorrelationData = b"334"

#try publishing a message to client catch exception if not connected
try:
    client.publish('pipeline', payload = "{\"predictions\": \"0.898451\"}", qos=0, properties= publish_properties)
    #take the timestamp of the message
    timestampsent = time.time()
    print ("AI sent data to counter: " + "{\"predictions\": \"0.898451\"}")
except Exception as e:
    print('Error: ' + str(e))
    time.sleep(1)
    sys.exit(1)

client.loop_forever()

