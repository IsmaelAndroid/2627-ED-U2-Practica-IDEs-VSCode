# =============================================================================
#  ED · U2 · 2.3 PERSONALIZACIÓN DEL ENTORNO
#  ACTIVIDAD 2 · Atajos de teclado personalizados
# -----------------------------------------------------------------------------
#  Teoría: 2.3 apartado 2.1.3 "Atajos de teclado personalizados".
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Abrir el editor de ATAJOS
#     File > Preferences > Keyboard Shortcuts   o   Ctrl+K Ctrl+S
#     Verás una tabla: Command (acción) · Keybinding (teclas) ·
#     When (cuándo funciona) · Source (Default / User).
#
#  PASO 2 · Asignar  Ctrl+Alt+F  a "Format Document" (ejemplo de la teoría)
#     a) En el buscador escribe   format document
#     b) Haz doble clic en la fila "Format Document" (la que tiene
#        When: editorHasDocumentFormattingProvider...).
#     c) Pulsa a la vez  Ctrl+Alt+F  y luego Enter.
#     d) La columna Source ahora pone "User": es TU atajo.
#     Pruébalo: desordena el código de abajo y pulsa Ctrl+Alt+F.
#
#  PASO 3 · ¿Ya está usado ese atajo?
#     Antes de asignar unas teclas, mira el aviso "X existing commands
#     have this keybinding" que sale al pulsarlas. Si ya se usan, puedes
#     cambiar el atajo antiguo o buscar otro.
#     Truco: el icono del teclado del buscador (Record Keys) busca qué
#     comando tiene una combinación de teclas concreta.
#
#  PASO 4 · Los atajos también son un archivo JSON
#     Botón "Open Keyboard Shortcuts (JSON)" (arriba a la derecha) ->
#     keybindings.json. Verás tu atajo así:
#       { "key": "ctrl+alt+f", "command": "editor.action.formatDocument" }
#
#  PASO 5 · Chuleta oficial
#     Help > Keyboard Shortcuts Reference (Ayuda > Referencia de métodos
#     abreviados de teclado): abre un PDF con los atajos más usados.
#
# =============================================================================

def area_rectangulo(base,altura):
    """Devuelve el área de un rectángulo."""
    return base*altura
print(  "Área:",area_rectangulo(3,4))


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#
#  E2.1 · Busca en Keyboard Shortcuts qué atajo tienen por defecto estas
#         acciones y anótalo en RESPUESTAS.md:
#           · Toggle Line Comment
#           · Copy Line Down
#           · Rename Symbol
#           · View: Toggle Terminal
#
#  E2.2 · Asigna  Ctrl+Alt+M  a "View: Toggle Minimap". Pruébalo.
#
#  E2.3 · Asigna  Ctrl+Alt+R  a "Python: Run Python File in Terminal".
#         Ejecuta este archivo con tu atajo.
#
#  E2.4 · Con el botón Record Keys, averigua qué comando ejecuta  Ctrl+B .
#
#  E2.5 · Elimina el atajo del E2.2 (clic derecho > Remove Keybinding) y
#         comprueba en keybindings.json que ha desaparecido.
# =============================================================================
