# Usa una imagen base oficial de Python
FROM python:3.12.5-alpine3.20

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el resto del código de la aplicación
COPY . /app/

RUN apt-get update 

# Copia el archivo de requisitos y luego instala las dependencias
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

