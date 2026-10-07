import math

import numpy as np
from PIL import Image

from resize_imagen import resize

# Tamaño de la pantalla de la Game Boy
ANCHO_PANTALLA = 160
ALTO_PANTALLA = 144

# Del tono más oscuro al más claro.
GAMEBOY = [(15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
BAYER_4 = [
    [ 0,  8,  2, 10],
    [12,  4, 14,  6],
    [ 3, 11,  1,  9],
    [15,  7, 13,  5],
]
PASO = 64


def filtro_gameboy(imagen_original: Image.Image) -> Image.Image:
    """
    Aplica el filtro Game Boy (4 tonos de verde, con dithering ordenado).

    Pasos: ajusta la resolución a una caja de 160x144, calcula el brillo de
    cada píxel, le suma el ajuste de la matriz de Bayer, lo cuantiza a uno de
    los 4 tonos de la paleta y pinta el píxel con ese color.

    Args:
        imagen_original: Imagen de Pillow a filtrar.

    Returns:
        Una imagen nueva en RGB, ya filtrada. La original no se modifica.
    """
    imagen = imagen_original.convert('RGB')

    # Paso 1. Resize de la imagen.
    # Resize con proporcion
    imagen_escalada = resize(ANCHO_PANTALLA, ALTO_PANTALLA, imagen)
    # # Resize sin proporcion
    # imagen_escalada = imagen.resize((ANCHO_PANTALLA, ALTO_PANTALLA))

    matriz_img = np.array(imagen_escalada)

    # Paso 2. Calcular el brillo (convertimos a int para que no se pase de 255).
    R = matriz_img[:, :, 0].astype(int)
    G = matriz_img[:, :, 1].astype(int)
    B = matriz_img[:, :, 2].astype(int)
    brillo = (R + G + B) / 3

    # Pasos 3, 4 y 5. Dithering, índices entre 0 y 3 y pintado.
    alto, ancho = brillo.shape
    imagen_final = np.zeros((alto, ancho, 3), dtype=np.uint8)

    for y in range(alto):
        for x in range(ancho):
            ajuste = (((BAYER_4[y % 4][x % 4] + 0.5) / 16) - 0.5) * PASO
            brillo[y, x] += ajuste
            indice = math.floor(brillo[y, x] / PASO)
            indice = min(3, max(0, indice))
            imagen_final[y, x] = GAMEBOY[indice]

    return Image.fromarray(imagen_final)

if __name__ == "__main__":
    imagen = Image.open('imagenes/marilyn.jpeg')
    filtro_gameboy(imagen).show()