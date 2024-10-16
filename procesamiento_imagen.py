#!/usr/bin/env python3
import os
import time
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageFilter

"""
Este proyecto permite procesar imágenes de manera concurrente aplicando un
filtro de desenfoque a cada imagen '.jpg' que se encuentre en el directorio 
'/img'.

El procesamiento se realiza utilizando `ThreadPoolExecutor` para distribuir
las tareas a diferentes hilos.
"""

# Función para procesar imágenes


def process_image(task: tuple) -> int:
    """
    Procesa una imagen aplicando un filtro de desenfoque y la guarda en el
    directorio de salida el cual crea en caso de no existir el directorio 
    de las imagenes es /img y el de salida /img/out.

    Args:
        args (tuple): Tupla que contiene la ruta de la imagen y el ID del worker.

    Returns:
        int: 
        Retorna 1 si la imagen fue procesada exitosamente, 0 si hubo un error.
    """
    image_path, worker_id = task
    try:
        print(f"\nWorker {worker_id} procesando {image_path}...")
        start_time = time.time()
        time.sleep(1)

        # Abrimos la imagen y aplicamos un filtro de desenfoque
        img = Image.open(image_path)
        img = img.filter(ImageFilter.BLUR)

        # Definir ruta de salida
        output_file = os.path.basename(image_path)
        output_path = os.path.join(
            './img', 'out', f"output_{output_file}")

        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path)

        elapsed_time = time.time() - start_time
        print(f"Worker {worker_id} completó {image_path} en {
              elapsed_time:.2f} segundos y guardada en {output_path}")

        # Devuelve 1 si el proceso se completó correctamente
        return 1
    except (IOError, OSError) as e:
        print(f"Error en Worker {worker_id} procesando {image_path}: {e}")
        # Devuelve 0 si hubo algún error
        return 0

# Función del proceso "master" que distribuye las tareas para ejecutarlas de
# manera concurrente


def master_task(paths: list) -> int:
    """
    Distribuye las tareas para el procesamiento de imágenes de manera concurrente.

    Args:
        paths: Lista de rutas de imágenes a procesar.
    Returns:
        int: Número de imágenes procesadas correctamente.
    """
    # Asignar un ID para cada tarea
    tasks = [(path, i + 1) for i, path in enumerate(paths)]

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_image, tasks))

    # Devuelve el número de imágenes procesadas correctamente
    return sum(results)


# entry point
if __name__ == '__main__':
    DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
    CARPETA_IMAGENES = os.path.join(DIRECTORIO_ACTUAL, 'img')
    imagenes = [os.path.join(CARPETA_IMAGENES, f)
                for f in os.listdir(CARPETA_IMAGENES) if f.endswith('.jpg')]

    print(f"Inicia el proceso de {len(imagenes)} imágenes...")

    # Ejecutar el proceso master para distribuir las tareas
    processed_images = master_task(imagenes)

    print(f"Procesamiento finalizado. {
          processed_images}/{len(imagenes)} imágenes procesadas correctamente.")
