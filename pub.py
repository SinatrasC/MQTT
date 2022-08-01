from pipeline import Mqtt as Mqtt

instance = Mqtt(on_message = None)
instance.publish(
    broker= 'localhost', 
    topic= 'pipeline', 
    payload= r'{"predictions": "0.898451"}')
