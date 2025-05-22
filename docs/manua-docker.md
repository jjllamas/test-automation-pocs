# 🐳 **Manual: Primeros pasos con Docker para tu repositorio de pruebas**

## ✅ Requisitos previos

1. **Instalar Docker Desktop**:

   * [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
   * Disponible para Windows, Mac y Linux.
   * Asegúrate de que puedes ejecutar:

     ```bash
     docker --version
     ```

2. **Tu estructura base de repo en GitHub**:

   ```bash
   test-automation-pocs/
   ├── modulo-0-xpath-css/
   ├── modulo-1-behave-selenium/
   ├── modulo-2-robot-framework/
   ├── modulo-3-playwright/
   ├── modulo-4-api-automation/
   ├── modulo-5-integraciones/
   ├── requirements.txt
   ├── Dockerfile
   └── README.md
   ```

---

## 🛠 Paso 1: Crear el `requirements.txt` global

```txt
# requirements.txt
selenium
behave
robotframework
robotframework-seleniumlibrary
robotframework-requests
allure-behave
playwright
```

---

## 🛠 Paso 2: Crear el `Dockerfile` en la raíz del repo

```dockerfile
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
```

---

## 🛠 Paso 3: Construir tu imagen Docker

Desde la raíz de tu repo, abre una terminal y ejecuta:

```bash
docker build -t test-automation .
```

Esto crea una imagen llamada `test-automation`.

---

## 🛠 Paso 4: Ejecutar el contenedor

```bash
docker run -it --rm test-automation
```

Esto abrirá una terminal dentro del contenedor donde puedes ejecutar cualquier módulo:

```bash
# Dentro del contenedor:
cd modulo-1-behave-selenium
behave

cd ../modulo-3-playwright
pytest

cd ../modulo-2-robot-framework
robot tests/
```

---

## 📁 Ejemplo de estructura funcional en tu repo

```bash
test-automation-pocs/
├── Dockerfile
├── requirements.txt
├── modulo-1-behave-selenium/
│   ├── features/
│   ├── steps/
│   ├── environment.py
├── modulo-2-robot-framework/
│   └── tests/
├── modulo-3-playwright/
│   └── tests/
└── README.md
```

---

## 🧹 Comandos útiles

| Acción                   | Comando                  |
| ------------------------ | ------------------------ |
| Ver imágenes instaladas  | `docker images`          |
| Ver contenedores activos | `docker ps`              |
| Borrar contenedor parado | `docker container prune` |
| Salir del contenedor     | `exit`                   |

---

## 📝 Tips adicionales

* Puedes mapear un volumen local si no quieres copiar archivos al contenedor:

  ```bash
  docker run -it --rm -v "$PWD":/tests test-automation
  ```

* Puedes crear un alias o script:

  ```bash
  alias testdocker='docker run -it --rm -v "$PWD":/tests test-automation'
  ```

---

## ✅ ¿Qué sigue?

* Implementar una POC en `modulo-1-behave-selenium` y probarla dentro del contenedor.
* Añadir `docker-compose.yml` si quieres lanzar más de un servicio (Allure, Jenkins, etc.).
* Publicar tu imagen en Docker Hub si quieres compartirla con el equipo.

---

¿Quieres que te prepare un ejemplo completo en `modulo-1-behave-selenium` con un test que puedas correr ahora mismo dentro del contenedor?
