#!/usr/bin/env python
import pika
import time
import random
import datetime
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
time.sleep(15)


conn_params = pika.ConnectionParameters('queue', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='randomNumbers')

random.seed(42)
    
    
while True:
	try:
		randNum = random.randint(1, 255)
		
		channel.basic_publish(exchange='', routing_key='randomNumbers', body=str(randNum))
		logging.info("Number {} sent".format(randNum))
		
		st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		logging.info(st)
		
		timeSleep = random.randint(1, 5)
		logging.info("We will sleep for {} :)".format(timeSleep))

		time.sleep(timeSleep)
	except KeyboardInterrupt:
		channel.stop_consuming()
	except Exception:
		channel.stop_consuming()
		traceback.print_exc(file=sys.stdout)
	finally:
		channel.stop_consuming()
