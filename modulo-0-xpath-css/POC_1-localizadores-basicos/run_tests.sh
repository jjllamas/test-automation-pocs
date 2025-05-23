#!/bin/bash
# Ejecuta los tests de Selenium para esta POC
echo "Ejecutando pruebas de POC_1-localizadores-basicos..."
pytest tests/ --maxfail=2 --disable-warnings -v
