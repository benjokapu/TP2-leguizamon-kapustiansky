import math
import numpy as np
from PIL import Image
from procesar_imagen.resize_imagen import resize


# Tamaño de la pantalla de la ctr
ANCHO_PANTALLA = 320
ALTO_PANTALLA = 240


def filtro_crt(imagen_original: Image.Image, desplazamiento:int) -> Image.Image:
    """
    Docstring para filtro_ctr
    
    :param imagen_original: Descripción
    :type imagen_original: Image.image
    :return: Descripción
    :rtype: 
    """
    # Paso 1. Convertir imagen a solo formato RGB
    imagen = imagen_original.convert('RGB')

    # Paso 2. Resize de la imagen
    # Resize con proporcion
    imagen_escalada = resize(ANCHO_PANTALLA, ALTO_PANTALLA, imagen)

    # Paso 3. Obtener la matriz de pixeles de la imagen escalada
    matriz_img = np.array(imagen_escalada)

    # Paso 4. Aplicar desplazamiento
    matriz_desplazada = aplicar_desplazamiento(matriz_img, desplazamiento)

    # Paso 5. Aplicar scanlines a imagen desplazada
    matriz_final = aplicar_scanlines(matriz_desplazada)

    # Paso 6. Convertir matriz a imagen nueva
    imagen_final = Image.fromarray(matriz_final)

    return imagen_final

    
