
from mqtt_connect import connect
import time

client = connect()

cnt = 1
while True:
    client.publish("iths/test1", payload=f"Hello from Python, post {cnt}", qos=0)
    time.sleep(5)
    cnt += 1