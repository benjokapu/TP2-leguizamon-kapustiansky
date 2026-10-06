import numpy as np
from PIL import Image
import math



# Cargar la imagen y asegurarnos de que esté en modo RGB
imagen_original = Image.open('imagenes/marilyn.jpeg').convert('RGB')

# Paso 1. Resize de la imagen.
# Resize con proporcion
# Importamos la funcion resize desde otro archivo
imagen_escalada = resize(160, 144, imagen_original)
# # Resize sin proporcion
# imagen_escalada = imagen_original.resize((160, 144))

# Convertir la imagen a una matriz de NumPy
# Tendrá una forma (forma/shape) de (ALTO, ANCHO, CANALES) -> Canales = (R, G, B)
matriz_img = np.array(imagen_escalada)

# Separar los canales de color de toda la matriz
R = matriz_img[:, :, 0]
G = matriz_img[:, :, 1]
B = matriz_img[:, :, 2]

R = R.astype(int)
G = G.astype(int)
B = B.astype(int)

# Paso 2. Calcular el brillo.
brillo = (R + G + B) / 3

# Paso 3, 4 y 5. Dithering ordenado e indices entre 0 y 3. Pintar la imagen.
alto_brillo, ancho_brillo = brillo.shape

imagen_final = np.zeros((alto_brillo, ancho_brillo, 3), dtype=np.uint8)

# Del tono mas oscuro al mas claro.
GAMEBOY = [(15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
BAYER_4 = [
    [ 0,  8,  2, 10],
    [12,  4, 14,  6],
    [ 3, 11,  1,  9],
    [15,  7, 13,  5],
]
paso = 64

indices = np.zeros((alto_brillo, ancho_brillo), dtype=int)

for y in range(alto_brillo):
    for x in range(ancho_brillo) :
        ajuste = (((BAYER_4[y % 4][x % 4] + 0.5) / 16 ) - 0.5 ) * paso
        brillo[y, x] += ajuste
        indice = math.floor(brillo[y, x] / paso)
        indice = min(3, max(0, indice))
        imagen_final[y,x] = GAMEBOY[indice]

resultado = Image.fromarray(imagen_final)
resultado.show()