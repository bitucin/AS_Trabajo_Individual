#Imagen del Sistema
FROM python:2.7-alpine

#Descargar e instalar dependencias
RUN pip install pika

#Variables de entorno
ENV PYTHONUNBUFFERED=1

#Directorio de trabajo
WORKDIR /usr/src/app

#Copiar al directorio de trabajo
COPY consumer.py .

#Comando de arranque
CMD ["python", "/usr/src/app/consumer.py"]
