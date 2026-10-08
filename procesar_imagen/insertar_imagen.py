import numpy as np
from PIL import Image
from procesar_imagen.resize_imagen import resize

def insertar_en_pantalla(resultado:Image.Image, aparato:Image.Image, mascara:Image.Image) -> Image.Image:
    """
    Insertar la imagen con filtro en aparato correspondiente
    segun lo especificado
    
    Args
        param resultado: Descripción
        type resultado: Image.Image
        param aparato: Descripción
        type aparato: Image.Image
        param mascara: Descripción
        type mascara: Image.Image
    Returns:
        return: Imagen de aparato con imagen filtrada en pantalla
        rtype: Image.Image
    """
    # Paso 1. Convertir imagenes a matrices
    matriz_aparato = np.array(aparato.convert("RGB"))
    matriz_mascara = np.array(mascara.convert("L"))

    # Paso 2. Obtener dimensión de la máscara
    columna_inicio, fila_inicio, columna_fin, fila_fin = obtener_coordenadas_pantalla(matriz_mascara)
    

    # Declaramos ancho y alto segun coordenadas con menor y mayor indice de pixeles blancos presentes
    ancho_mascara = columna_fin - columna_inicio + 1
    alto_mascara = fila_fin - fila_inicio + 1

     # Paso 3. Convertir imagen a RGB
    imagen = resultado.convert("RGB")

    # Paso 4. Hacer resize de matriz de imagen filtrada
    # para que entre en la pantalla del aparato segun su ancho y alto
    imagen_escalada = imagen.resize((ancho_mascara, alto_mascara))

    # Paso 4. Convertir imagen escalada en matriz
    matriz_resultado = np.array(imagen_escalada)

    # Paso 4. Hacer copia de matriz aparato porque va a ser la matriz final
    matriz_imagen_final = matriz_aparato.copy()

    # Paso 5. Iterar desde fila_inicio y columna_inicio hasta fila_fin y columna_fin
    # (solo nos interesa iterar sobre la pantalla del aparato)
    i = 0
    for fila in range(fila_inicio, fila_fin):
        j = 0
        for columna in range(columna_inicio, columna_fin):
            # Si el pixel actual es blanco en matriz_mascara cambiamos el pixel
            # del aparato por el de la imagen filtrada ajustada a la pantalla
            # del aparato
            if matriz_mascara[fila, columna] == 255:
                matriz_imagen_final[fila, columna] = matriz_resultado[i, j]
            j += 1
        i += 1
    imagen_final = Image.fromarray(matriz_imagen_final)
    return imagen_final



def obtener_coordenadas_pantalla(matriz_mascara:list) -> tuple:
        """
        Obtener coordenadas donde irá la imagen filtrada, para
        luego redimensionar dicha imagen a ese tamaño.
        
        Args:
            matriz_mascara: Matriz de grises con pantalla en pixeles blancos,
            y el resto pixeles negros.
            type matriz_mascara: list

        Returns:
            return: Coordenadas de donde comienza oantalla y donde termina
            rtype: tuple
        """
        # Paso 1. Obtenemos el valor maximo que pueden tomar una fila
        # y columna (para compara hacia abajo)
        x0, y0 = np.shape(matriz_mascara)
        # Paso 1,1. Declaramos en valor mínimo que puede tomar una fila
        # y columna (para comparar hacia arriba)
        x1, y1 = 0, 0

        # Paso 2. Iteramos el array de la máscara para comparar filas y columnas
        for fila in range(len(matriz_mascara)):
            columnas = matriz_mascara[fila]
            for columna in range(len(columnas)):
                # Paso 2,1. Si el píxel es blanco, chequeamos si hay reasignacion
                # de variables por hacer
                if matriz_mascara[fila, columna] == 255:
                    # Si columna es menor a y0 esta mas cerca de ser
                    # la columna con menor índice que tiene pixel blanco
                    if columna < x0:
                        x0 = columna
                    # Si fila es menor a x0 esta mas cerca de ser
                    # la fila con menor índice que tiene pixel blanco
                    if fila < y0:
                        y0 = fila
                    # Si columna es mayor a y1 esta mas cerca de ser
                    # la columna con mayor índice que tiene pixel blanco
                    if columna > x1:
                        x1 = columna
                    # Si fila es mayor a x1 esta mas cerca de ser
                    # la fila con menor índice que tiene pixel blanco
                    if fila > y1:
                        y1 = fila
        # Declaramos ancho y alto segun coordenadas con menor y mayor indice de pixeles blancos presentes
        
        return x0, y0, x1, y1

