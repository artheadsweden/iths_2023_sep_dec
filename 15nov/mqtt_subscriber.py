from mqtt_connect import connect

client = connect()
client.subscribe("iths/#")
client.loop_forever()