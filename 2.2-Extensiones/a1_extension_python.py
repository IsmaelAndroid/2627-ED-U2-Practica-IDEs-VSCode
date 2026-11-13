# =============================================================================
#  ED · U2 · 2.2 GESTIÓN DE MÓDULOS Y EXTENSIONES
#  ACTIVIDAD 1 · Instalar la extensión de Python y ver lo que aporta
# -----------------------------------------------------------------------------
#  Teoría: https://revilofe.github.io/section3/u02/teoria/EDES-U2.2.-Modulos/
#          apartados 2 (¿Qué son?) y 3.1-3.2 (Marketplace e instalación)
#  Una EXTENSIÓN (plugin) añade funciones nuevas al IDE. VS Code "de serie"
#  es casi un editor; con extensiones se convierte en un IDE completo.
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 0 · ANTES de instalar nada, fíjate en este archivo:
#     · No hay botón ▶ arriba a la derecha.
#     · Escribe  texto.  (con el punto) al final de la PARTE A: no salen
#       los métodos de los textos. Bórralo después.
#
#  PASO 1 · Abrir el MARKETPLACE de extensiones
#     Pulsa el icono EXTENSIONS de la barra de actividades (cuatro
#     cuadrados, uno separado)  o  Ctrl+Shift+X.
#
#  PASO 2 · Buscar e INSTALAR la extensión "Python"
#     a) Escribe  python  en el buscador.
#     b) Elige la que se llama "Python" y es de "Microsoft" (con la marca
#        azul de editor verificado). Pulsa sobre ella: se abre su página
#        con la descripción, el número de descargas y las valoraciones.
#     c) Pulsa  Install.
#     d) Mira la lista de instaladas (@installed): se han instalado también
#        "Pylance" y "Python Debugger". Son DEPENDENCIAS: la extensión
#        Python las necesita y las instala sola.
#
#  PASO 3 · Lo que ha cambiado: EJECUTAR (intérprete integrado)
#     Vuelve a este archivo. Ahora aparece arriba a la derecha el botón
#     ▶ "Run Python File". Púlsalo: se ejecuta en la terminal.
#     Abajo a la derecha, en la barra de estado, aparece la versión de
#     Python. Si pulsas ahí puedes elegir otro intérprete
#     (también con Ctrl+Shift+P > "Python: Select Interpreter").
#
#  PASO 4 · INTELLISENSE (autocompletado inteligente)
#     a) Al final de la PARTE A escribe  texto.  -> ahora salen TODOS los
#        métodos de un str (upper, lower, split...) con su explicación.
#     b) Pasa el ratón por encima de  len  o de  contar_palabras : sale
#        una ventanita con su documentación (docstring).
#
#  PASO 5 · ERRORES EN TIEMPO REAL
#     Descomenta (Ctrl+ç) la línea  # print(resultdo)  del final de la
#     PARTE A. Sale subrayada en rojo/amarillo SIN ejecutar: la variable no
#     existe. Abre el panel PROBLEMS (Ctrl+Shift+M) para ver la lista de
#     errores. Corrígelo (resultado) o vuelve a comentarlo.
#
#  PASO 6 · NAVEGAR y REFACTORIZAR el código
#     · Ctrl+clic sobre  contar_palabras  (donde se usa) -> salta a su
#       definición (Go to Definition, F12).
#     · Clic en  contar_palabras  y pulsa  F2  (Rename Symbol): escribe
#       numero_palabras y Enter -> cambia el nombre EN TODOS LOS SITIOS
#       donde se usa. Esto es una REFACTORIZACIÓN automática.
#
# =============================================================================


def contar_palabras(frase):
    """Devuelve cuántas palabras tiene la frase."""
    return len(frase.split())


def invertir(frase):
    """Devuelve la frase al revés."""
    return frase[::-1]


texto = "Los entornos de desarrollo nos hacen la vida más fácil"
resultado = contar_palabras(texto)
print("Frase:", texto)
print("Palabras:", resultado)
print("Al revés:", invertir(texto))

# print(resultdo)


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#
#  E1.1 · Ejecuta el archivo con el botón ▶ y copia la salida en
#         RESPUESTAS.md.
#
#  E1.2 · Usando IntelliSense (escribe  texto.  y busca en la lista),
#         completa la función  en_mayusculas  para que devuelva el texto
#         en MAYÚSCULAS. ¿Qué método has usado?
#
#  E1.3 · Descomenta el BLOQUE E1.3. Tiene 3 errores. Sin ejecutar,
#         localízalos con el panel PROBLEMS y corrígelos.
#
#  E1.4 · Con F2 cambia el nombre de la función  f  por  contar_vocales
#         (comprueba que también cambia donde se llama).
#
#  E1.5 · Abre la página de la extensión "Python" en el Marketplace y
#         contesta en RESPUESTAS.md: ¿quién la publica?, ¿qué otras
#         extensiones instala con ella?, ¿qué versión tienes?
# =============================================================================


def en_mayusculas(frase):
    """Devuelve la frase en mayúsculas."""
    return frase  # E1.2: cambia esta línea


def f(frase):
    """Cuenta las vocales (sin tildes) de la frase."""
    return sum(1 for letra in frase.lower() if letra in "aeiou")


print("Mayúsculas:", en_mayusculas(texto))
print("Vocales:", f(texto))

# --- BLOQUE E1.3 ---
# nombre = "Visual Studio Code"
# print("Longitud:", len(nombr))
# print("Primera letra:", nombre[0]
# prin("Minúsculas:", nombre.lower())
