# =============================================================================
#  ED · U2 · 2.3 PERSONALIZACIÓN DEL ENTORNO
#  ACTIVIDAD 4 · Pruebas automáticas integradas en el IDE (pytest)
# -----------------------------------------------------------------------------
#  Teoría: 2.1 apartado 3.5 "Pruebas automatizadas" y
#          2.3 apartado 3.1.2 "Automatización de pruebas".
#  Este archivo tiene las FUNCIONES. Sus pruebas están en test_calculos.py
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Instalar pytest
#     En la terminal integrada:   python -m pip install pytest
#
#  PASO 2 · Configurar las pruebas en el IDE
#     Pulsa el icono TESTING de la barra de actividades (el matraz).
#     > "Configure Python Tests" > pytest > "." (root directory).
#     VS Code guarda en .vscode/settings.json:
#         "python.testing.pytestEnabled": true
#     Aparece el árbol de pruebas: carpeta > test_calculos.py > test_...
#
#  PASO 3 · Ejecutar las pruebas
#     · Botón ▶▶ "Run Tests" arriba del panel TESTING: las ejecuta TODAS.
#     · Verde ✔ = pasa · Rojo ✘ = falla.
#     · En test_calculos.py, junto a cada  def test_...  hay un ▶ para
#       ejecutar solo esa prueba. Si falla, el IDE muestra el error ahí
#       mismo (valor esperado / valor obtenido).
#     Ahora pasan las de sumar y es_par; las del EJERCICIO fallan porque
#     las funciones aún no están hechas. ¡Ese es tu trabajo!
#
#  PASO 4 · Una TAREA de tests (como en la actividad A3)
#     Añade a .vscode/tasks.json (dentro de "tasks", separada por coma):
#       {
#           "label": "Ejecutar tests",
#           "type": "shell",
#           "command": "python",
#           "args": ["-m", "pytest", "-v"],
#           "group": { "kind": "test", "isDefault": true },
#           "problemMatcher": []
#       }
#     Lánzala con Ctrl+Shift+P > "Tasks: Run Test Task".
#
#  PASO 5 · Automatizar: que las pruebas se ejecuten SOLAS al guardar
#     (teoría 3.1.2). La extensión Python no lo hace sola, así que usamos
#     otra EXTENSIÓN:
#     a) Ctrl+Shift+X, busca  Run on Save  (de "emeraldwalk") e instálala.
#        Como es de un editor nuevo, VS Code pregunta si confías en él:
#        "Trust Publisher & Install".
#     b) Añade a .vscode/settings.json (dentro de las llaves):
#          "emeraldwalk.runonsave": {
#              "commands": [
#                  { "match": "[.]py$", "cmd": "python -m pytest -q" }
#              ]
#          }
#     c) Guarda cualquier .py (Ctrl+S) y abre el panel OUTPUT
#        (Ctrl+Shift+U), canal "Run On Save": ahí sale el resultado.
#
# =============================================================================


def sumar(a, b):
    """Devuelve a + b."""
    return a + b


def es_par(numero):
    """Devuelve True si el número es par."""
    return numero % 2 == 0


# =============================================================================
#  PARTE B · AHORA TÚ  (con Run on Save, cada Ctrl+S te dice cómo vas)
# =============================================================================
#
#  E4.1 · Programa  media  para que pasen sus pruebas.
#  E4.2 · Programa  nota_textual  para que pasen sus pruebas.
#  E4.3 · Programa  es_primo  para que pasen sus pruebas.
#  E4.4 · En test_calculos.py escribe TÚ dos pruebas nuevas para
#         contar_vocales  y luego programa la función.
#  E4.5 · Rompe a propósito  sumar  (pon a - b), guarda y mira qué pruebas
#         se ponen en rojo. Copia el mensaje de error en RESPUESTAS.md y
#         déjala bien otra vez.
# =============================================================================


def media(numeros):
    """Devuelve la media de la lista. Si la lista está vacía, devuelve 0."""
    raise NotImplementedError("E4.1: programa esta función")


def nota_textual(nota):
    """Convierte una nota numérica en texto.

    0 a <5 Insuficiente · 5 a <6 Suficiente · 6 a <7 Bien
    7 a <9 Notable · 9 a 10 Sobresaliente
    """
    raise NotImplementedError("E4.2: programa esta función")


def es_primo(numero):
    """Devuelve True si el número es primo (1 y los negativos NO lo son)."""
    raise NotImplementedError("E4.3: programa esta función")


def contar_vocales(texto):
    """Devuelve cuántas vocales (a, e, i, o, u, con o sin tilde) hay."""
    raise NotImplementedError("E4.4: programa esta función")
