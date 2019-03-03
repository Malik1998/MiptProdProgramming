#!/usr/bin/env python
import pika
import time
import random
import datetime

time.sleep(20)


conn_params = pika.ConnectionParameters('queue', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='randomNumbers')

random.seed(42)

while True:
	randNum = random.randint(1, 255)
	
	channel.basic_publish(exchange='', routing_key='randomNumbers', body=str(randNum))
	print("Number {} sent".format(randNum))

	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	print(st)
	
	timeSleep = random.randint(1, 5)
	print("We will sleep for {} :)".format(timeSleep))

	time.sleep(timeSleep)
    

connection.close()
