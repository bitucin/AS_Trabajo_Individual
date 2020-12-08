#!/usr/bin/env python
import pika, sys, os, time

#Codigo basado en la documentacion oficial de RabbitMQ
#Fuente: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

def main():

    time.sleep(20) #Espera a que el server se inicialice para evitar error de conexion

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
