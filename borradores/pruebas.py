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
print(len(R))

print(matriz_img[10, 50])
print(R[10, 50], G[10, 50], B[10, 50])
print(imagen_original.size)

#calcular el brillo a mano sin numpy
brillo = []
for i in range(len(R)) :
    fila_nueva = []
    for r, g, b in zip(R[i], G[i], B[i]) :
        suma = r + g + b
        resultado = suma / 3
        fila_nueva.append(resultado)
    brillo.append(fila_nueva)

brillo = np.array(brillo)
