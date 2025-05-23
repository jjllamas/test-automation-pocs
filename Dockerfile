# Dockerfile
FROM python:3.10-slim

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    curl \
    unzip \
    git \
    nodejs \
    npm

# Instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instala navegadores Playwright
RUN pip install --no-cache-dir playwright && \
    playwright install

# Crear carpeta para tus pruebas
WORKDIR /tests
COPY . /tests

# Comando por defecto: abrir una shell interactiva
CMD [ "bash" ]