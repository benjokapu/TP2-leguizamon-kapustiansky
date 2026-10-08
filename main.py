from PIL import Image

import solicitar_usuario
from procesar_imagen.gameboy import filtro_gameboy
from procesar_imagen.crt import filtro_crt
from procesar_imagen.insertar_imagen import insertar_en_pantalla


def main() -> None:
    # Pedir ruta
    ruta = solicitar_usuario.pedir_ruta_imagen()
    if ruta is None:
        print("\nNo se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.")
        return

    # Pedir pantalla
    pantalla = solicitar_usuario.pedir_pantalla()
    if pantalla is None:
        print("\nPantalla inválida. Las opciones son 'gameboy' o 'crt'.")
        return

    # Pedir desplazamiento si es necesario
    if pantalla == "crt":
        desplazamiento = solicitar_usuario.pedir_desplazamiento()
        if desplazamiento is None:
            print("\nEl desplazamiento debe ser un número entero positivo.")
            return

    # Pedir ruta de salida
    ruta_salida = solicitar_usuario.pedir_ruta_salida()
    if ruta_salida is None:
        print("\nLa ruta de guardado no puede estar vacía.")
        return

    # Procesar la imagen
    imagen = Image.open(ruta)

    if pantalla == "gameboy":
        resultado = filtro_gameboy(imagen)
        aparato = Image.open('imagenes/gameboy.png')
        mascara = Image.open('imagenes/gameboy_mascara.png')
    else:
        resultado = filtro_crt(imagen, desplazamiento)
        aparato = Image.open('imagenes/tv.png')
        mascara = Image.open('imagenes/tv_mascara.png')

    resultado = insertar_en_pantalla(resultado, aparato, mascara)

    # Guardar el resultado
    resultado.save(ruta_salida)
    print(f"\nImagen guardada en {ruta_salida}")


if __name__ == "__main__":
    main()