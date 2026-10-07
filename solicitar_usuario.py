import os


def pedir_ruta_imagen() -> str | None:
    """
    Pide por pantalla la ruta de la imagen a procesar y comprueba que exista.

    Returns:
        La ruta ingresada si el archivo existe, o None si no se encuentra.
    """
    ruta = input('Ingrese la ruta de la imagen: ')

    if not os.path.exists(ruta):
        return None
    return ruta



def pedir_pantalla() -> str | None:
    """
    Pide por pantalla qué pantalla usar y comprueba que sea una opción válida.

    El texto ingresado se normaliza: se sacan los espacios sobrantes y se pasa
    a minúsculas, así que 'GameBoy' o ' CRT ' también se aceptan.

    Returns:
        'gameboy' o 'crt' si la opción es válida, o None en caso contrario.
    """
    pantalla = input('Seleccione la pantalla (gameboy/crt): ').strip().lower()

    if pantalla != 'gameboy' and pantalla != 'crt':
        return None
    return pantalla



def pedir_desplazamiento() -> int | None:
    """
    Pide por pantalla el desplazamiento de canales para el filtro CRT.

    Si el usuario no escribe nada, se usa el valor por defecto (3).

    Returns:
        El desplazamiento como entero positivo, o None si lo ingresado no es
        un número entero positivo.
    """
    texto = input('Ingrese el desplazamiento de canales (default=3): ').strip()

    if texto == '':
        return 3
    if not texto.isdecimal() or int(texto) <= 0:
        return None
    return int(texto)

def pedir_ruta_salida() -> str | None:
    """
    Pide por pantalla la ruta donde guardar la imagen procesada.

    Returns:
        La ruta ingresada, o None si el usuario no escribió nada.
    """

    ruta = input('Seleccione la ruta para guardar la imagen procesada: ').strip()
    if ruta == '':
        return None
    return ruta