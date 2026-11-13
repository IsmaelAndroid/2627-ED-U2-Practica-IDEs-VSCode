# =============================================================================
#  ED · U2 · 2.2 GESTIÓN DE MÓDULOS Y EXTENSIONES
#  ACTIVIDAD 2 · El DEPURADOR (lo aporta la extensión "Python Debugger")
# -----------------------------------------------------------------------------
#  Teoría: 2.1 apartado 3.3 "Depurador integrado" y 2.2 apartado 2.1
#          ("Herramientas de depuración avanzadas" llegan con extensiones).
#  Depurar = parar el programa en un punto y mirar qué valen las variables
#  para encontrar por qué no hace lo que esperamos.
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Poner un PUNTO DE INTERRUPCIÓN (breakpoint)
#     Haz clic a la izquierda del número de línea de
#         total = total + nota
#     (dentro de la función media). Sale un punto ROJO.  (También: F9)
#
#  PASO 2 · Empezar a depurar
#     Pulsa F5 (o Run > Start Debugging). La primera vez pregunta:
#     elige "Python Debugger" y luego "Python File".
#     El programa se PARA en la línea del punto rojo (queda resaltada).
#
#  PASO 3 · Mirar las VARIABLES
#     A la izquierda, en RUN AND DEBUG, el apartado VARIABLES muestra
#     notas, total y nota con su valor actual.
#     También puedes pasar el ratón por encima de una variable del código.
#
#  PASO 4 · Avanzar con la BARRA DE DEPURACIÓN (arriba)
#     F5  Continue   -> sigue hasta el siguiente punto de interrupción.
#     F10 Step Over  -> ejecuta la línea y pasa a la siguiente.
#     F11 Step Into  -> entra DENTRO de la función que se llama.
#     Shift+F11 Step Out -> termina la función y sale de ella.
#     Shift+F5 Stop  -> para la depuración.
#     Pulsa F5 varias veces y mira cómo cambia  total  en cada vuelta.
#
#  PASO 5 · WATCH y DEBUG CONSOLE
#     · En WATCH pulsa  +  y escribe   total / len(notas)
#       -> el IDE calcula la expresión en cada paso.
#     · En el panel DEBUG CONSOLE puedes escribir expresiones, por ejemplo
#       sum(notas)   y pulsar Enter.
#
#  PASO 6 · Quita el punto rojo (clic encima otra vez) y para con Shift+F5.
#
# =============================================================================


def media(notas):
    """Calcula la nota media de una lista de notas."""
    total = 0
    for nota in notas:
        total = total + nota
    return total / len(notas)


notas_clase = [6, 8, 5, 9, 7]
print("Media de la clase:", media(notas_clase))


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#  Las dos funciones de abajo tienen un ERROR (bug). El programa no falla,
#  pero da un resultado incorrecto. ¡Encuéntralos con el DEPURADOR!
#
#  E2.1 · contar_aprobados([5, 3, 7, 5, 10]) debería dar 4, pero da otra
#         cosa. Pon un breakpoint dentro del for, avanza con F5 y mira
#         nota y aprobados. ¿En qué vuelta falla? Escribe en RESPUESTAS.md
#         el valor de  nota  cuando no cuenta y la corrección.
#
#  E2.2 · nota_maxima([-3, -8, -1]) debería dar -1, pero da 0.
#         Depura con F10 desde la primera línea de la función. ¿Por qué
#         da 0? Corrígelo.
#
#  E2.3 · Usa WATCH con la expresión  nota > maxima  mientras depuras
#         nota_maxima. Explica qué valores toma.
#
#  E2.4 · Con F11 entra en la función  media  desde la última línea del
#         archivo. ¿Qué ves en la sección CALL STACK?
# =============================================================================


def contar_aprobados(notas):
    """Cuenta cuántas notas son aprobado (5 o más)."""
    aprobados = 0
    for nota in notas:
        if nota > 5:
            aprobados = aprobados + 1
    return aprobados


def nota_maxima(notas):
    """Devuelve la nota más alta de la lista."""
    maxima = 0
    for nota in notas:
        if nota > maxima:
            maxima = nota
    return maxima


print("Aprobados:", contar_aprobados([5, 3, 7, 5, 10]), "(debería ser 4)")
print("Máxima:", nota_maxima([-3, -8, -1]), "(debería ser -1)")
print("Media:", media([10, 0]))
