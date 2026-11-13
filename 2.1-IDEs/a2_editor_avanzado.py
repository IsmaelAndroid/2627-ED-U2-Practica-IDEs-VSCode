# =============================================================================
#  ED · U2 · 2.1 ENTORNOS DE DESARROLLO INTEGRADO (IDEs)
#  ACTIVIDAD 2 · El editor avanzado: escribir y modificar código más rápido
# -----------------------------------------------------------------------------
#  Teoría: apartado 3.1 "Editor de código avanzado".
#  Un IDE no es solo "un bloc de notas con colores": su editor tiene
#  herramientas para escribir y cambiar código sin repetir trabajo.
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · MOVER y COPIAR LÍNEAS
#     Pon el cursor en la línea  "Martes"  de la lista  dias  (más abajo).
#     Alt+↑ / Alt+↓          -> mueve la línea arriba/abajo.
#     Ordena los días correctamente (Lunes, Martes, Miércoles...).
#     Shift+Alt+↓            -> duplica la línea (copia hacia abajo).
#     Ctrl+Shift+K           -> borra la línea entera.
#
#  PASO 2 · COMENTAR / DESCOMENTAR
#     Selecciona las 3 líneas del bloque "PRUEBAS" y pulsa  Ctrl+ç
#     (en teclado inglés es Ctrl+/). Vuelve a pulsarlo para descomentar.
#     Si no te funciona: Edit > Toggle Line Comment.
#
#  PASO 3 · MULTICURSOR (escribir en varios sitios a la vez)
#     a) Alt+clic en varias líneas -> aparece un cursor en cada una.
#     b) Haz doble clic en la palabra  precio  y pulsa  Ctrl+D  varias
#        veces: selecciona la SIGUIENTE aparición cada vez.
#     c) Ctrl+Shift+L: selecciona TODAS las apariciones de golpe.
#        Escribe  importe  -> se cambian todas a la vez.
#
#  PASO 4 · BUSCAR y REEMPLAZAR
#     Ctrl+F -> buscar en este archivo.  Ctrl+H -> buscar y reemplazar.
#     Reemplaza  "IVA"  por  "impuesto"  solo en los comentarios del
#     bloque CARRITO (usa la flecha de "Replace" de uno en uno).
#
#  PASO 5 · IR A LÍNEA y AJUSTE DE LÍNEA
#     Mira la barra de estado: algo como "Ln 12, Col 5" = línea y columna.
#     Ctrl+G y escribe 1 -> el cursor salta a la línea 1.
#     Alt+Z -> ajuste de línea (las líneas largas no se salen de la
#     pantalla). Pruébalo con la línea larga del final de la PARTE A.
#
# =============================================================================

dias = [
    "Martes",
    "Lunes",
    "Jueves",
    "Miércoles",
    "Viernes",
]

# --- CARRITO: el IVA es del 21 %. El total lleva IVA incluido. ---
precio = 20.0
precio_con_iva = precio * 1.21
print("Precio sin IVA:", precio)
print("Precio con IVA:", precio_con_iva)

# --- PRUEBAS ---
print("Días de clase:", dias)
print("Número de días:", len(dias))
print("Primer día:", dias[0])

MENSAJE = "Esta línea es muy larga a propósito para que pruebes el ajuste de línea con Alt+Z y veas que el texto se adapta al ancho de la ventana del editor sin necesidad de usar la barra de desplazamiento horizontal."


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#
#  E2.1 · Ordena la lista  asignaturas  alfabéticamente usando SOLO
#         Alt+↑ / Alt+↓ (sin cortar ni pegar).
#
#  E2.2 · La lista  modulos  está comentada y no tiene comillas ni comas.
#         Descoméntala (Ctrl+ç) y, usando
#         MULTICURSOR (Alt+clic, o selecciona las 5 líneas y pulsa
#         Shift+Alt+I para poner un cursor al final de cada una)
#         conviértela en una lista válida de Python:
#             "Programación",
#             "Bases de datos", ...
#
#  E2.3 · En la función  calcular  la variable se llama  x . Cámbiala por
#         nota  en todas sus apariciones a la vez con Ctrl+D o Ctrl+Shift+L.
#         ¡Cuidado! "max" también tiene una x: compruébalo antes de escribir.
#
#  E2.4 · Comenta con Ctrl+ç las dos líneas marcadas como "BORRAR".
#
#  E2.5 · Ejecuta el archivo en la terminal y comprueba que no da errores.
# =============================================================================

asignaturas = [
    "Sistemas informáticos",
    "Entornos de desarrollo",
    "Programación",
    "Bases de datos",
    "Lenguajes de marcas",
]

# Convierte estas líneas en una lista de Python (E2.2):
# modulos = [
#     Programación
#     Bases de datos
#     Entornos de desarrollo
#     Sistemas informáticos
#     Lenguajes de marcas
# ]


def calcular(x):
    """Devuelve la nota limitada entre 0 y 10."""
    if x < 0:
        x = 0
    x = min(x, 10)
    return max(x, 0)


print("BORRAR: esta línea sobra")
print("BORRAR: esta también")
print(asignaturas)
print(calcular(11), calcular(-2), calcular(7))
