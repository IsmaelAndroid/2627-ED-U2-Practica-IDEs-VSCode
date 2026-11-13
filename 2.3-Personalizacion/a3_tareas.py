# =============================================================================
#  ED · U2 · 2.3 PERSONALIZACIÓN DEL ENTORNO
#  ACTIVIDAD 3 · Automatizar con TAREAS (tasks.json)
# -----------------------------------------------------------------------------
#  Teoría: 2.3 apartado 3.1.1 "Crear una tarea de ejecución automática".
#  Una TAREA es un comando que el IDE ejecuta por ti (compilar, ejecutar,
#  pasar los tests...). Se guardan en  .vscode/tasks.json
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Crear tasks.json
#     Terminal > Configure Tasks...  (Terminal > Configurar tareas...)
#     > "Create tasks.json file from template" > "Others".
#     Se crea  .vscode/tasks.json  con una tarea de ejemplo "echo".
#
#  PASO 2 · Escribir la tarea "Ejecutar Python" (la de la teoría)
#     Sustituye TODO el contenido de tasks.json por:
#
#     {
#         "version": "2.0.0",
#         "tasks": [
#             {
#                 "label": "Ejecutar Python",
#                 "type": "shell",
#                 "command": "python",
#                 "args": ["${file}"],
#                 "group": { "kind": "build", "isDefault": true },
#                 "problemMatcher": []
#             }
#         ]
#     }
#
#     · label   -> el nombre de la tarea.
#     · command -> el programa que se ejecuta. En Windows es  python
#                  (en Linux/Mac suele ser  python3 , como en la teoría).
#     · ${file} -> VARIABLE: el archivo que tengas abierto en el editor.
#     · group build + isDefault -> es la tarea de "compilar" por defecto.
#     Guarda (Ctrl+S).
#
#  PASO 3 · Lanzar la tarea
#     Vuelve a ESTE archivo y pulsa  Ctrl+Shift+B  (Run Build Task).
#     Se ejecuta en la terminal con el nombre de la tarea.
#     Otra forma: Terminal > Run Task... > Ejecutar Python.
#
#  PASO 4 · Un ATAJO para la tarea (paso 4 de la teoría)
#     Ctrl+K Ctrl+S > botón "Open Keyboard Shortcuts (JSON)" y añade
#     dentro de los corchetes [ ]:
#
#       {
#           "key": "ctrl+alt+j",
#           "command": "workbench.action.tasks.runTask",
#           "args": "Ejecutar Python"
#       }
#
#     Guarda y prueba Ctrl+Alt+J en este archivo.
#
# =============================================================================

import datetime
import platform

ahora = datetime.datetime.now()
print("Hola desde una TAREA de VS Code")
print("Fecha y hora:", ahora.strftime("%d/%m/%Y %H:%M:%S"))
print("Sistema operativo:", platform.system())
print("Versión de Python:", platform.python_version())


# =============================================================================
#  PARTE B · AHORA TÚ
#  (Todas las tareas van en el MISMO tasks.json, dentro de "tasks": [ ... ],
#   separadas por comas.)
# =============================================================================
#
#  E3.1 · Crea una tarea "Versión de Python" que ejecute   python --version
#         Lánzala con Terminal > Run Task...
#
#  E3.2 · Crea una tarea "Comprobar estilo" que pase Pylint al archivo
#         abierto:   python -m pylint ${file}
#         (Antes, en la terminal:   python -m pip install pylint  )
#
#  E3.3 · Crea una tarea "Formatear" que ejecute
#            python -m autopep8 --in-place ${file}
#         (Antes:   python -m pip install autopep8  )
#
#  E3.4 · Crea una tarea "Formatear y ejecutar" que NO tenga command y que
#         use  "dependsOn": ["Formatear", "Ejecutar Python"]  y
#         "dependsOrder": "sequence" . ¿Qué hace?
#
#  E3.5 · Haz que "Versión de Python" se ejecute SOLA al abrir la carpeta:
#         añade a esa tarea   "runOptions": { "runOn": "folderOpen" }
#         Cierra y abre la carpeta. (VS Code te pedirá permiso: pulsa
#         "Allow and run" / Permitir.)
# =============================================================================
