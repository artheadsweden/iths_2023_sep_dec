
from mqtt_connect import connect
import time

client = connect()

cnt = 1
while True:
    client.publish("iths/test3", payload=f"Hello from thing no 3, post {cnt}", qos=0)
    time.sleep(5)
    cnt += 1