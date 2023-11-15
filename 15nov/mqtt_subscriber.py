from mqtt_connect import connect

def on_message(client, userdata, msg):
    print('Now we are in control and can do things like storing to a db')

client = connect()
client.subscribe("iths/#")
client.on_message = on_message
client.loop_forever()