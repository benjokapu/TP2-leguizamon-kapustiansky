# Solicitar al usuario: (ARCHIVO CON LAS FUNCIONES PARA SOLICITAR COSAS)

# La ruta de la imagen a procesar.
# FUNCION pedir ruta de imagen --> la ruta o none si es invalido.
# ERROR Si no se encuentra la imagen de entrada.

# La pantalla a usar: gameboy o crt.
# FUNCION pedir filtro --> gameboy o crt o none.
# ERROR Si la pantalla elegida no es gameboy ni crt.

# Si eligió crt, el desplazamiento de canales (entero positivo, por defecto 3).
# if eligio crt, FUNCION pedir desplazameinto de canales (default 3) --> n entero positivo o none
# ERROR Si el desplazamiento no es un número entero positivo.

# La ruta donde guardar el resultado.
# FUNCION pedir ruta de guardado de imagen --> la ruta.


# Procese la imagen:
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
