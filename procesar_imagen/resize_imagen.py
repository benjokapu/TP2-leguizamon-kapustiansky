from PIL import Image

def resize(ancho_deseado: int, alto_deseado: int, imagen_original: Image.Image) -> Image.Image :
    """
    Redimensiona una imagen para que entre en una caja, manteniendo su proporción.

    Un lado de la imagen resultante coincide con el de la caja y el otro queda
    igual o más chico. Si la imagen original es más chica que la caja, se agranda.

    Args:
        ancho_deseado: Ancho de la caja, en píxeles.
        alto_deseado: Alto de la caja, en píxeles.
        imagen_original: Imagen de Pillow a redimensionar.

    Returns:
        Una imagen nueva, ya redimensionada. La original no se modifica.
    """
    ancho, alto = imagen_original.size
    # Resize de la imagen pero teniendo cuidado que no se deforme usando el escalar mas grande para que mantenga su proporcion
    escalar_ancho = ancho / ancho_deseado 
    escalar_alto = alto / alto_deseado 
    escalar_maximo = max(escalar_ancho, escalar_alto)
    
    # Calculo el nuevo ancho y alto para aplicarle el resize de la imagen.
    ancho_nuevo = round(ancho / escalar_maximo)
    alto_nuevo = round(alto / escalar_maximo)
    # Aplico el resize de la imagen. .resize((ancho, alto))
    imagen_escalada = imagen_original.resize((ancho_nuevo, alto_nuevo))

    return imagen_escalada
