# =============================================================================
#  ED · U2 · 2.2 GESTIÓN DE MÓDULOS Y EXTENSIONES
#  ACTIVIDAD 3 · Linter (Pylint) y formateador (autopep8)
# -----------------------------------------------------------------------------
#  Teoría: 2.2 apartado 3.3 "Instalación de linting y formateadores".
#  · LINTER: revisa el código buscando errores y malas prácticas
#    (variables sin usar, nombres que no siguen las normas...).
#  · FORMATEADOR: arregla solo el ASPECTO del código (sangrías, espacios,
#    líneas en blanco) según unas reglas. En Python, las de PEP 8.
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Instalar las extensiones
#     Ctrl+Shift+X y busca e instala (las dos de Microsoft):
#       · Pylint     (ms-python.pylint)
#       · autopep8   (ms-python.autopep8)
#
#  PASO 2 · Ver los avisos del LINTER
#     Vuelve a este archivo y guárdalo (Ctrl+S). El código de abajo
#     ("CÓDIGO SUCIO") se llena de subrayados.
#     Abre PROBLEMS (Ctrl+Shift+M): cada línea es un aviso de Pylint con
#     su código, por ejemplo:
#       W0611 unused-import       -> importas algo que no usas
#       C0103 invalid-name        -> nombre que no sigue snake_case
#       C0116 missing-function-docstring -> función sin documentar
#       W0612 unused-variable     -> variable que no se usa
#     Haz clic en un aviso: el cursor salta a la línea del problema.
#
#  PASO 3 · FORMATEAR el documento
#     Clic derecho en el editor > Format Document  (Shift+Alt+F).
#     Si pregunta qué formateador usar (porque tienes varios), elige
#     "Configure Default Formatter..." > autopep8.
#     Mira cómo cambian las sangrías y los espacios. ¡Pero OJO!: los
#     nombres mal puestos y el import sin usar SIGUEN AHÍ. El formateador
#     solo arregla el aspecto; el linter te dice lo que tienes que pensar tú.
#
#  PASO 4 · Configurar las extensiones
#     File > Preferences > Settings  (Ctrl+,)  y escribe en el buscador:
#        @ext:ms-python.pylint     -> salen TODOS los ajustes de Pylint
#     En "Pylint: Args" pulsa "Add Item" y escribe   --max-line-length=79
#     Guarda este archivo: ahora Pylint avisa de las líneas de más de 79
#     caracteres (el límite de PEP 8).
#     También se llega desde la extensión: rueda ⚙ > Settings.
#     (La teoría cita el ajuste "Show Notifications": las versiones
#      actuales de las extensiones ya no lo tienen.)
#
#  PASO 5 · Arreglamos juntos 2 avisos: borra  import os  y añade un
#     docstring a la función  perimetro . Guarda y mira PROBLEMS.
#
# =============================================================================

# ---------------------------- CÓDIGO SUCIO ----------------------------------
import os
import math
def AreaCirculo( r ):
  a=math.pi*r**2
  return a
def perimetro(r) :
    resultado=2*math.pi*r
    sin_usar = 3
    return resultado
print( "Área:",round(AreaCirculo(2),2) )
print("Perímetro:" , round(perimetro(2),2))


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#
#  E3.1 · Abre  a3_ejercicio_limpia_codigo.py . Sin cambiar lo que hace el
#         programa, déjalo con CERO avisos en PROBLEMS:
#           1) Primero formatea con Shift+Alt+F.
#           2) Luego corrige a mano lo que diga Pylint.
#         Anota en RESPUESTAS.md cuántos avisos había al principio y 3
#         códigos de aviso distintos (por ejemplo C0103) con su significado.
#
#  E3.2 · Termina de limpiar el CÓDIGO SUCIO de este archivo (PARTE A)
#         hasta que no quede ningún aviso que sea de esas líneas.
#
#  E3.3 · En Settings busca  format on save  y actívalo. Desordena una
#         línea (pon espacios de más), guarda con Ctrl+S y mira qué pasa.
# =============================================================================
