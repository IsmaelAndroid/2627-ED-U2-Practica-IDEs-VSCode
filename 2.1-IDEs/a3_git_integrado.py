# =============================================================================
#  ED · U2 · 2.1 ENTORNOS DE DESARROLLO INTEGRADO (IDEs)
#  ACTIVIDAD 3 · Control de versiones integrado en el IDE
# -----------------------------------------------------------------------------
#  Teoría: apartado 3.4 "Integración con sistemas de control de versiones".
#  VS Code trae Git integrado: puedes ver cambios, compararlos y hacer
#  commits sin escribir comandos.
#  (Necesitas Git instalado: https://git-scm.com/downloads)
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Abrir el panel SOURCE CONTROL  (Ctrl+Shift+G)
#     · Si CLONASTE el proyecto: verás "Changes" con los archivos que ya
#       has modificado en las actividades A1 y A2.
#     · Si lo descargaste en ZIP: pulsa "Initialize Repository"
#       (Inicializar repositorio). Desde ese momento la carpeta es un repo.
#
#  PASO 2 · Ver qué ha cambiado
#     · En el EXPLORER, los archivos modificados salen con una  M  y los
#       nuevos con una  U  (untracked).
#     · En el editor, la franja de la izquierda marca en color las líneas
#       cambiadas (verde = nueva, azul = modificada, rojo = borrada).
#     · En Source Control, haz clic en un archivo de "Changes": se abre la
#       VISTA DE DIFERENCIAS (diff): a la izquierda cómo estaba, a la
#       derecha cómo está ahora.
#
#  PASO 3 · Hacer un COMMIT
#     a) Pasa el ratón por "Changes" y pulsa  +  (Stage All Changes).
#     b) Escribe un mensaje arriba, por ejemplo:
#            2.1: actividades A1 y A2 hechas
#     c) Pulsa el botón  Commit.
#     Si te pide nombre y correo de Git, en la terminal:
#            git config --global user.name "Tu Nombre"
#            git config --global user.email "tu@correo.es"
#
#  PASO 4 · Ver el HISTORIAL
#     En el EXPLORER, abajo, despliega  TIMELINE  con este archivo abierto:
#     verás sus commits. En la barra de estado, abajo a la izquierda,
#     aparece la rama actual (main).
#
# =============================================================================

version = 1
print("Versión del programa:", version)


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#
#  E3.1 · Cambia  version = 1  por  version = 2 . Abre Source Control y
#         mira el diff. ¿De qué color sale la línea antigua? ¿Y la nueva?
#         (Contesta en RESPUESTAS.md)
#
#  E3.2 · Añade una línea  print("Hecho por: TU NOMBRE")  y haz un commit
#         con el mensaje   2.1-A3: versión 2 con autor
#
#  E3.3 · Cambia cualquier línea y DESCARTA el cambio desde Source Control
#         (flecha curva "Discard Changes"). ¿Qué ha pasado con el archivo?
#
#  E3.4 · Abre TIMELINE de este archivo. ¿Cuántos commits aparecen?
#
#  E3.5 · Abre la terminal y escribe   git log --oneline
#         ¿Coincide con lo que ves en el IDE?
# =============================================================================
