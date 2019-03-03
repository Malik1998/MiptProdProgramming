#!/usr/bin/env python
import pika
import traceback, sys, time
import datetime

time.sleep(20)


conn_params = pika.ConnectionParameters('queue', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='randomNumbers')

def callback(ch, method, properties, body):
    print("We received {}".format(body))
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print(st)

channel.basic_consume(callback, queue='randomNumbers', no_ack=True)

while True:
	try:
		channel.start_consuming()
	except KeyboardInterrupt:
		channel.stop_consuming()
	except Exception:
		channel.stop_consuming()
		traceback.print_exc(file=sys.stdout)
