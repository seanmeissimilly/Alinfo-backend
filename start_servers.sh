#!/bin/bash

# Inicia el servidor de Apache Tika
java -jar tika-server.jar &

# Guarda el PID del servidor de Tika
TIKA_PID=$!

# Inicia el servidor de Django
python manage.py runserver

# Cuando el servidor de Django se detenga, detén el servidor de Tika
kill $TIKA_PID
