import numpy as np
from PIL import Image

# Cargar la imagen y asegurarnos de que esté en modo RGB
imagen_original = Image.open('imagenes/marilyn.jpeg').convert('RGB')

# Convertir la imagen a una matriz de NumPy
# Tendrá una forma (forma/shape) de (699, 687, 3) -> Alto, Ancho, Canales (R, G, B)
matriz_img = np.array(imagen_original)

# 4. Separar los canales de color de toda la matriz
R = matriz_img[:, :, 0]
G = matriz_img[:, :, 1]
B = matriz_img[:, :, 2]

print(R[0])
print(len(R[0]))
