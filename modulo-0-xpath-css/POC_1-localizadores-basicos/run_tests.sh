#!/bin/bash
# Ejecuta los tests de Selenium para esta POC

echo "====================================="
echo "Ejecutando pruebas de Selenium"
echo "Carpeta: POC_1-localizadores-basicos"
echo "Fecha: $(date)"
echo "====================================="

# Mostrar la versión de pytest y Python
echo ""
echo "Entorno:"
pytest --version
python --version
echo ""

# Ejecutar los tests
pytest tests/ \
  --maxfail=20 \
  --disable-warnings \
  -vv \
  --tb=short \
  --durations=5

