import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
     
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f"Subscribed: {mid}, QOS: {granted_qos}")

def on_publish(client, userdata, mid, properties=None):
    print(f"Publish: {mid}")

def on_message(client, userdata, msg):
    print(f"Received topic: {msg.topic}")
    print(f"Received message: {msg.payload}")
    print(f"Received QoS: {msg.qos}")

def connect(client_id=""):
    # Using MQTT version 5 here, for version 3.1.1 use MQTTv311, 3.1 use MQTTv31

    client = paho.Client(client_id=client_id, userdata=None, protocol=paho.MQTTv5)

    client.on_connect = on_connect

    # enable TLS for secure connection
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

    client.username_pw_set("iths1", "IthsMqtt1")

    client.connect('ea5abedbce0d46b0b62320705574e6be.s1.eu.hivemq.cloud', 8883)

    client.on_subscribe = on_subscribe
    client.on_publish = on_publish
    client.on_message = on_message

    return client
