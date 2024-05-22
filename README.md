# Hexagonal Architecture Project

Este es un ejemplo básico de una arquitectura hexagonal en Python.

## Estructura del Proyecto

- `src/domain`: Contiene las entidades del dominio, los repositorios y los servicios.
- `src/application`: Contiene los servicios de aplicación.
- `src/infrastructure`: Contiene las implementaciones de los adaptadores de infraestructura.
- `src/main.py`: Archivo principal para ejecutar la aplicación.
- `tests`: Contiene los tests unitarios.

## Cómo Ejecutar

1. Crear un entorno virtual y activarlo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
