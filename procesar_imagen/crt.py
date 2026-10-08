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

def aplicar_desplazamiento(matriz_img: list, desplazamiento: int) -> list:
    """
    Si la posicion de la columna desplazada esta entre 0 y el largo de las columnas
    desplazamos la columna y tomamos el valor del desplazamiento segun sea RED o BLUE
    Si no, la posicion se mantiene igual. 
    
    Args:
        matriz_img: Matriz de la imagen original
        type matriz_img: list
        desplazamiento: n posiciones a desplazar parte R y B del pixel
        type desplazamiento: int

    Returns:
        matriz_img_desplazada: Una nueva matriz con valores R y B,
        de cada pixel desplazados segun corresponda. 
    """
    # Paso 1. Copiar matriz original para guardar matriz desplazada en copia
    matriz_img_desplazada = matriz_img.copy()

    # Paso 2. Iterar por fila y columna (indices fijos)
    for n_fila in range(len(matriz_img_desplazada)):
        columnas = matriz_img_desplazada[n_fila]
        for columna in range(len(columnas)):
            # Paso 2,1. Si posicion desplazada no se va de indice cambiar valor de canal rojo y azul
            # sino dejar valores R y B constantes. G siempre constante.
            if (columna + desplazamiento) < len(columnas):
                # Desplazamos B de la copia
                matriz_img_desplazada[n_fila, columna, 2] = matriz_img[n_fila, columna + desplazamiento, 2]
            
            if (columna - desplazamiento) > 0:
                # Desplazamos B de la copia
                matriz_img_desplazada[n_fila, columna, 0] = matriz_img[n_fila, columna - desplazamiento, 0]

    return matriz_img_desplazada

def aplicar_scanlines(matriz_desplazada: list) -> list:
    """
    Quitarle color a las filas pares, multiplicando cada pixel por 0.5
    y redondeando los valores para que queden enteros y no genero problemas
    al pasar a imagen.
    
    Args:
        matriz_desplazada: Matriz ya con Red y Blue desplazados segun corresponda
        type matriz_desplazada: list

    Returns:
        matriz_final: Matriz con valores finales
        type: list
    """
    # Paso 1. Copiar matriz desplazada para luego agregarle scanlines en filas pares
    matriz_final = np.copy(matriz_desplazada)

    # Paso 2. Multiplicar filas pares por 0.5
    matriz_filas_pares_multiplicada = np.multiply(matriz_desplazada[::2,:,:], 0.5)

    # Paso 3. Redondear matriz nueva
    matriz_filas_pares_redondeadas_final = np.round(matriz_filas_pares_multiplicada)

    # Paso 4. Agregar filas multiplicadas y redondeadas a matriz desplazada
    matriz_final[::2,:,:] = matriz_filas_pares_redondeadas_final

    return matriz_final