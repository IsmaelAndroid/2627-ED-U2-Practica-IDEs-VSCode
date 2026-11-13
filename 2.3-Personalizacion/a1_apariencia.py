# =============================================================================
#  ED · U2 · 2.3 PERSONALIZACIÓN DEL ENTORNO
#  ACTIVIDAD 1 · Tema, fuente y configuración (de usuario y de proyecto)
# -----------------------------------------------------------------------------
#  Teoría: https://revilofe.github.io/section3/u02/teoria/EDES-U2.3.-Personalizacion/
#          apartados 2.1.1 (tema), 2.1.2 (fuente) y 2.1.4 (extensiones)
# =============================================================================

# =============================================================================
#  PARTE A · PASO A PASO CON EL PROFESOR
# =============================================================================
#
#  PASO 1 · Cambiar el TEMA DE COLOR
#     File > Preferences > Themes > Color Theme
#     (Archivo > Preferencias > Temas > Tema de color)  o   Ctrl+K Ctrl+T
#     (pulsa Ctrl+K, suelta, y luego Ctrl+T).
#     Muévete con las flechas: el tema cambia al momento (vista previa).
#     Prueba "Light Modern", "Dark+"... y elige el que quieras con Enter.
#     Abajo de la lista: "Browse Additional Color Themes..." busca más
#     temas en el Marketplace (son extensiones).
#
#  PASO 2 · Abrir la CONFIGURACIÓN (Settings)
#     File > Preferences > Settings   o   Ctrl+,
#     En el buscador escribe   font size
#     Cambia "Editor: Font Size" a 16 y mira el código.
#
#  PASO 3 · USUARIO vs PROYECTO (Workspace)
#     Arriba de Settings hay dos pestañas:
#       · User      -> se aplica a TODOS tus proyectos.
#       · Workspace -> se aplica SOLO a este proyecto y se guarda en el
#                      archivo  .vscode/settings.json  de la carpeta.
#     Ve a la pestaña Workspace y busca   render whitespace : ponlo en "all".
#     Mira el EXPLORER: ha aparecido la carpeta  .vscode  con
#     settings.json. Ábrelo: la configuración es un archivo JSON.
#     (Botón "Open Settings (JSON)", arriba a la derecha de Settings,
#      el icono de la hoja con la flecha.)
#
#  PASO 4 · Otras opciones útiles (búscalas en Settings)
#     · Files: Auto Save         -> afterDelay (guarda solo)
#     · Editor: Word Wrap        -> on (ajuste de línea)
#     · Editor: Minimap Enabled  -> quitar/poner el minimapa
#     · Zoom de toda la ventana: Ctrl+ +  /  Ctrl+ -  /  Ctrl+0 (volver).
#
#  PASO 5 · PERFILES: una configuración distinta para cada tipo de trabajo
#     File > Preferences > Profiles  (o la rueda ⚙ de abajo a la izquierda)
#     > New Profile...
#     Ponle de nombre  Clase-ED  y pulsa Create. Un perfil guarda SUS
#     propios ajustes, temas y extensiones. Cambia de perfil desde la
#     misma rueda. (Vuelve al perfil "Default" al terminar.)
#
# =============================================================================

PRECIOS = {"teclado": 25.5, "ratón": 12.0, "monitor": 149.99}

for producto, precio in PRECIOS.items():
    print(f"{producto:<10}{precio:>8.2f} €")


# =============================================================================
#  PARTE B · AHORA TÚ
# =============================================================================
#
#  E1.1 · Instala un tema del Marketplace (por ejemplo "One Dark Pro" o
#         "Dracula Theme") y aplícalo. Anota en RESPUESTAS.md cuál.
#
#  E1.2 · Configura SOLO PARA ESTE PROYECTO (pestaña Workspace) lo siguiente
#         y comprueba que aparece en .vscode/settings.json:
#           · Editor: Font Size       -> 15
#           · Editor: Tab Size        -> 4
#           · Editor: Rulers          -> 79   (línea vertical de PEP 8)
#           · Files: Auto Save        -> afterDelay
#           · Editor: Format On Save  -> activado
#
#  E1.3 · Escribe directamente en .vscode/settings.json esta línea (dentro
#         de las llaves, separada por coma) y guarda:
#             "workbench.colorCustomizations": {"editorRuler.foreground": "#ff0000"}
#         ¿Qué ha cambiado?
#
#  E1.4 · Quita el valor "render whitespace" del PASO 3: en Settings, pasa
#         el ratón por la opción y pulsa la rueda ⚙ > Reset Setting.
#
#  E1.5 · Contesta en RESPUESTAS.md: si cambias la fuente en User y en
#         Workspace con valores distintos, ¿cuál gana? Compruébalo.
# =============================================================================
