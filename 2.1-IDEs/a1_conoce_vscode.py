# =============================================================================
#  ED · U2 · 2.1 ENTORNOS DE DESARROLLO INTEGRADO (IDEs)
#  ACTIVIDAD 1 · Conoce Visual Studio Code y los componentes de un IDE
# -----------------------------------------------------------------------------
#  Teoría: https://revilofe.github.io/section3/u02/teoria/EDES-U2.1.-IDEs/
#          apartados 2 (¿Qué es un IDE?) y 3 (Componentes de un IDE)
#
#  PARTE A -> la hacemos JUNTOS en clase, paso a paso.
#  PARTE B -> EJERCICIOS para ti (al final del archivo).
#  Las respuestas escritas van en 2.1-IDEs/RESPUESTAS.md
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Abrir el proyecto como CARPETA
#     File > Open Folder...  (Archivo > Abrir carpeta...)
#     Elige la carpeta raíz del proyecto descargado.
#     Si aparece "Do you trust the authors of the files in this folder?"
#     pulsa "Yes, I trust the authors" (Sí, confío en los autores).
#     -> Un IDE trabaja con PROYECTOS (carpetas), no con archivos sueltos.
#
#  PASO 2 · Las 5 zonas de la ventana de VS Code
#     [1] Barra de actividades: la columna de iconos de la izquierda.
#         Explorer · Search · Source Control · Run and Debug · Extensions
#     [2] Barra lateral: muestra lo que hayas elegido en [1]
#         (ahora mismo, el Explorer con los archivos del proyecto).
#     [3] Editor: donde está este archivo. Puedes abrir varios en pestañas.
#     [4] Panel inferior: Terminal, Problems, Output, Debug Console.
#         Ábrelo/ciérralo con Ctrl+J.
#     [5] Barra de estado (abajo del todo): línea/columna, lenguaje...
#
#  PASO 3 · EDITOR DE CÓDIGO AVANZADO (componente 3.1 de la teoría)
#     a) RESALTADO DE SINTAXIS: mira el código de abajo. Las palabras
#        reservadas (def, for, if), los textos y los números tienen colores
#        distintos. Así se lee mejor y se ven antes los errores.
#     b) AUTOCOMPLETADO: ve a la línea "# escribe aquí" (al final de la
#        PARTE A), escribe debajo   print(alu   y espera un segundo.
#        VS Code te propone "alumnos": pulsa Tab o Enter y cierra el
#        paréntesis -> print(alumnos)
#        (De momento solo sugiere palabras del archivo. En la 2.2 lo
#        mejoraremos con la extensión de Python.)
#     c) PLEGADO DE CÓDIGO: pasa el ratón a la izquierda de "def" y pulsa
#        la flechita (v) para plegar/desplegar la función.
#     d) MINIMAPA: la miniatura del archivo a la derecha del editor.
#
#  PASO 4 · INTÉRPRETE INTEGRADO a través de la TERMINAL (componente 3.2)
#     Abre la terminal: Terminal > New Terminal (Terminal > Nuevo terminal)
#     o con  Ctrl+ñ
#     Escribe:   python --version
#        -> debe salir "Python 3.x.x". (Si no, prueba con: py --version)
#     Escribe:   python 2.1-IDEs/a1_conoce_vscode.py
#        -> verás la salida del programa SIN salir del IDE.
#
#  PASO 5 · PALETA DE COMANDOS y APERTURA RÁPIDA
#     Ctrl+Shift+P -> PALETA DE COMANDOS: desde aquí se llega a todo.
#        Escribe  theme  y mira las opciones (aún no cambies nada).
#        Pulsa Esc para cerrarla.
#     Ctrl+P -> abre un archivo escribiendo parte de su nombre.
#        Escribe  a2_edi  y pulsa Enter: se abre la actividad 2.
#
#  PASO 6 · DEPURADOR y CONTROL DE VERSIONES (componentes 3.3 y 3.4)
#     Pulsa el icono "Run and Debug" (triángulo con un bicho).
#        Para depurar Python, VS Code necesita una EXTENSIÓN.
#        -> ¡Eso es justo lo que haremos en el punto 2.2!
#     Pulsa el icono "Source Control" (tres círculos unidos por líneas).
#        Git viene integrado en el IDE: lo veremos en la actividad A3.
#
# =============================================================================

alumnos = ["Ana", "Luis", "Marta", "Iker"]
notas = [7.5, 4.0, 9.25, 6.0]


def mostrar_notas(nombres, calificaciones):
    """Muestra cada alumno con su nota y si aprueba o suspende."""
    for nombre, nota in zip(nombres, calificaciones):
        estado = "APROBADO" if nota >= 5 else "SUSPENSO"
        print(f"{nombre:<8} {nota:>5}  {estado}")


print("=== Notas de 1º DAM ===")
mostrar_notas(alumnos, notas)

# escribe aquí


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#
#  E1.1 · Ejecuta este programa desde la terminal integrada y copia la
#         salida en RESPUESTAS.md (apartado E1.1).
#
#  E1.2 · Añade a la alumna "Sara" con un 5.5 a las listas  alumnos  y
#         notas  (usa el autocompletado). Vuelve a ejecutar el programa.
#         Pista: en la terminal, la flecha ↑ repite el último comando.
#
#  E1.3 · Busca en TODO el proyecto con  Ctrl+Shift+F  la palabra  pytest
#         ¿En cuántos archivos aparece? ¿Cuáles? (Contesta en RESPUESTAS.md)
#
#  E1.4 · Con  Ctrl+Shift+P  busca el comando  "View: Toggle Minimap"
#         y ejecútalo dos veces. ¿Qué hace?
#
#  E1.5 · Cierra la carpeta (File > Close Folder) y vuelve a abrirla con
#         File > Open Recent (Archivo > Abrir reciente).
#
#  E1.6 · Completa en RESPUESTAS.md la tabla "Zonas de VS Code y
#         componentes de un IDE".
# =============================================================================
