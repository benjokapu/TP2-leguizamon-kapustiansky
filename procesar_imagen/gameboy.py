import numpy as np
from PIL import Image
from resize_imagen import resize

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

# Paso 3. Dithering ordenado.
BAYER_4 = [
    [ 0,  8,  2, 10],
    [12,  4, 14,  6],
    [ 3, 11,  1,  9],
    [15,  7, 13,  5],
]
paso = 64

alto_brillo, ancho_brillo = brillo.shape
