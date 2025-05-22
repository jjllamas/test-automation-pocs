# 🧪 Test Automation POCs

Repositorio estructurado por módulos con **POCs (Proof of Concepts)** para aprender, probar y comparar diferentes tecnologías de **automatización de pruebas**.

Cada módulo corresponde a una herramienta o técnica específica, organizada de forma independiente y con ejemplos prácticos.

---

## 📦 Estructura del proyecto

```
test-automation-pocs/
│
├── Dockerfile                  # Imagen base con todo el stack
├── requirements.txt           # Dependencias globales (Python)
├── .gitignore                 # Archivos ignorados por Git
├── README.md                  # Este archivo
│
├── docs/                      # Documentación general
│   └── glosario.md
│
├── scripts/                   # Scripts de utilidad
│   ├── run_all_tests.sh
│   └── entrypoint.sh
│
├── modulo-0-xpath-css/        # XPath, Selectores HTML y CSS
├── modulo-1-behave-selenium/  # Pruebas BDD con Selenium + Behave
├── modulo-2-robot-framework/  # Automatización con Robot Framework
├── modulo-3-playwright/       # Automatización moderna con Playwright
├── modulo-4-api-automation/   # Tests de API REST (Behave + Robot)
└── modulo-5-integraciones/    # Docker, Jenkins, Allure, reporting
```

---

## 🚀 ¿Cómo empezar?

### 1. Clona este repositorio

```bash
git clone https://github.com/jjllamas/test-automation-pocs.git
cd test-automation-pocs
```

### 2. Construye la imagen Docker

```bash
docker build -t test-automation .
```

### 3. Entra al contenedor

```bash
docker run -it --rm -v "$PWD":/tests test-automation
```

### 4. Ejecuta los módulos

```bash
# Dentro del contenedor:
cd modulo-1-behave-selenium && behave
cd ../modulo-3-playwright && pytest
cd ../modulo-2-robot-framework && robot tests/
```

---

## 🎯 Objetivo de cada módulo

| Módulo | Objetivo |
|--------|----------|
| `modulo-0-xpath-css` | Dominar selectores para tests UI |
| `modulo-1-behave-selenium` | Automatizar pruebas funcionales con BDD |
| `modulo-2-robot-framework` | Crear tests con Robot Framework (UI + API) |
| `modulo-3-playwright` | Automatización moderna, rápida y paralela |
| `modulo-4-api-automation` | Validar APIs RESTful desde código |
| `modulo-5-integraciones` | Integración con Docker, Jenkins, Allure |

---

## 📚 Documentación

- [Glosario de términos y conceptos](docs/glosario.md)
- Cada módulo tiene su propio `README.md` con detalles y ejemplos.

---

## 🛠 Requisitos

- Docker (recomendado)
- Git

---

## 📌 Autor

Proyecto personal de estudio y experimentación sobre automatización de pruebas.  