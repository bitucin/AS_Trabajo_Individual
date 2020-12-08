Este directorio contiene un Dockerfile para construir la imagen
para publicar un mensaje en el servidor rabbitmq de kubernetes.

El script publisher.py declara la IP del cluster, el puerto 31600
del protocolo AMPQ, el nombre del virtualhost '/' y las credenciales
de usuario ('guest', 'guest')
