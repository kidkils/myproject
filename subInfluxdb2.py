import pika
import json
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


def insert_to_influx(data, routing_key):
    client = InfluxDBClient(url="192.168.43.70:8086", token="a6WAt3mAwy4MP2Cq1koohw4wQTiK09M8_gx9WLpzQwtrH_w5eDRyQe1q4bMYCcKn0hT0UTdV94zsBcJgInLFgw==", org="pnup")
    write_api = client.write_api()
    query_api = client.query_api()

    keys = routing_key.split('-')
    measurement = keys[0]
    namenode = keys[1]
    # client.switch_database('iot_multinode_DB')
    data = [{
        "measurement": measurement,
        "tags": {
            "name": namenode
        },
        "fields": {
            "value": data,
            # "namenode": namenode
        }
    }]

    write_api.write(bucket="iot_multinode_DB", org ="pnup", record=data)

credentials = pika.PlainCredentials('admin', '12345coba')

parameters = pika.ConnectionParameters('192.168.43.70', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='test-exchange', exchange_type='topic', durable=True)

result=channel.queue_declare(queue='', exclusive=True)

queue_name=result.method.queue

routing_key = ['hujan', 'suhu', 'kelembapan', 'moisture']

for i in range(1, 6):
    for rk in routing_key:
        channel.queue_bind(queue=queue_name, exchange='test-exchange', routing_key=rk + "-node" + str(i))

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    insert_to_influx(body, method.routing_key)

channel.basic_consume(queue=queue_name, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
