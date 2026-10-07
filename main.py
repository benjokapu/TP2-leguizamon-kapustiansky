from PIL import Image

import solicitar_usuario
from procesar_imagen.gameboy import filtro_gameboy


def main():
    while True:
        # Pedir ruta
        ruta = solicitar_usuario.pedir_ruta_imagen()
        if ruta is None:
            print("\nNo se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.")
            break
        # Pedir pantalla
        pantalla = solicitar_usuario.pedir_pantalla()
        if pantalla is None: 
            print("\nPantalla inválida. Las opciones son 'gameboy' o 'crt'.")
            break
        # Pedir desplazamiento si es necesario.
        if pantalla == "crt" :
            desplazamiento = solicitar_usuario.pedir_desplazamiento()
            if desplazamiento is None:
                print("\nEl desplazamiento debe ser un número entero positivo.")
                break
        # Pedir ruta de salida
        ruta_salida = solicitar_usuario.pedir_ruta_salida()
        if ruta_salida is None:
            print("\nLa ruta de guardado no puede estar vacía.")
            break

        # Procesado de imagen:
        imagen = Image.open(ruta)

        if pantalla == "gameboy":
            resultado = filtro_gameboy(imagen)

        # Para probar, falta la mascara
        resultado.save(ruta_salida)
        print(f"\nImagen guardada en {ruta_salida}")
        # (ARCHIVO CON LAS FUNCIONES DE LOS FILTROS)
        # (ARCHIVO CON LAS FUNCIONES PARA APLICAR MASCARA)

        # Si la pantalla es gameboy, aplicar el filtro Game Boy (con dithering) e insertar el resultado en la pantalla de gameboy.png usando gameboy_mascara.png.
        # FUNCION aplicar filtro gameboy con dithering --> imagen para insertar en el gameboy
        # FUNCION para aplicarle la mascara --> resultado final

        # Si la pantalla es crt, aplicar el filtro CRT e insertar el resultado en la pantalla de tv.png usando tv_mascara.png.
        # FUNCION aplicar filtro crt --> imagen para insertar en el crt
        # FUNCION para aplicarle la mascara --> resultado final (podria ser igual a la de arriba)

        # Guarde la imagen resultante en la ruta indicada.
        # FUNCION guardar imagen en la ruta

        # Aunque salga todo bien, debe estar para que no corra el codigo infinitamente.
        break

if __name__ == "__main__":
    main()