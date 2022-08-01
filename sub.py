from pipeline import Mqtt as Mqtt
import queue
import time

q = queue.Queue()

def on_message_init(client, userdata, message):
    print ('Recieved data from AI: ' + str(message.payload))
    q.put(("{'" + str(message.payload) + "', " + str(message.topic) + "}"))

instance = Mqtt(on_message=on_message_init)
instance.subscribe(broker= 'localhost', topic= 'pipeline')

while True:
    if not q.empty():
        msg = q.get()
        print(msg)
        print('-'*10)
    time.sleep(.1)