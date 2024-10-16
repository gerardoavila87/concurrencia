# Procesamiento Concurrente de Imágenes

Este proyecto permite procesar imágenes de manera concurrente aplicando un filtro de desenfoque a cada imagen '.jpg' que se encuentre en el directorio '/img'. El procesamiento se realiza utilizando `ThreadPoolExecutor` para distribuir las tareas a diferentes hilos.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instaladas las siguientes dependencias:

### Librerías necesarias:

1. **Pillow**: Una librería de Python para abrir, manipular y guardar imágenes.
   
   Puedes instalar Pillow con el siguiente comando:
   
   ```bash
   pip install Pillow
