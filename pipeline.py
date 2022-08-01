import sys
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

class Mqtt:
    on_message = None
    def __init__(self, on_message) -> None:
        self.on_message = on_message

    def subscribe(self, topic, broker):
        broker_address = broker
        self.client = mqtt.Client("clientsub", protocol=mqtt.MQTTv5)
        #client.username_pw_set("cedalo", "RMY8WQZubP")
        self.client.connect(broker_address)
        self.client.on_message = self.on_message
        self.client.subscribe(topic)
        self.client.loop_start()

    def publish(self, topic, broker, payload):
        broker_address = broker
        self.client = mqtt.Client("clientpub", protocol=mqtt.MQTTv5)
        self.client.connect(broker_address)
        publish_properties = Properties(PacketTypes.PUBLISH)
        publish_properties.ResponseTopic = topic
        publish_properties.CorrelationData = b"334"

        try:
            self.client.publish(topic, payload = payload, qos=0, properties= publish_properties)
            print ("AI sent data to counter: " + payload)
        except Exception as e:
            print('Error: ' + str(e))
            sys.exit(1)

