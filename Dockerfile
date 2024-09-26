# Usa una imagen base oficial de Python
FROM python:3.12.5-alpine3.20

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Copia el archivo de requisitos y luego instala las dependencias
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app/

# Ejecutar migraciones y arrancar el servidor
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application"]

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000
