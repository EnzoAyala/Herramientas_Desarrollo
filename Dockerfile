# Imagen base de Python
FROM python:3.11-slim

# Evita crear archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2 / MySQL
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo tu proyecto
COPY . .

# Exponer puerto Flask
EXPOSE 5000

# Comando para correr la app
CMD ["python", "app.py"]