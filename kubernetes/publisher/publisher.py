#!/usr/bin/env python
import pika, sys, time

#Codigo basado en el tutorial de la documentacion oficial de RabbitMQ
#Fuente: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

time.sleep(20) #Espera que el servidor se inicialice para evitar problemas de conexion

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
pika.ConnectionParameters('192.168.99.101', 31600, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Soy Diego Vesga y este es mi trabajo de RabbitMQ en Docker"

channel.basic_publish(exchange='', 
routing_key='hello', body=message)
print(" [x] Sent %r" % message)
connection.close()
