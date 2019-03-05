#!/usr/bin/env python
import pika
import traceback, sys, time
import datetime
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

time.sleep(15)


conn_params = pika.ConnectionParameters('queue', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='randomNumbers')

def callback(ch, method, properties, body):
    logging.info("We received {}".format(body))
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    logging.info(st)

channel.basic_consume(callback, queue='randomNumbers', no_ack=True)

while True:
	try:
		channel.start_consuming()
	except KeyboardInterrupt:
		channel.stop_consuming()
	except Exception:
		channel.stop_consuming()
		traceback.print_exc(file=sys.stdout)
	finally:
		channel.stop_consuming()
