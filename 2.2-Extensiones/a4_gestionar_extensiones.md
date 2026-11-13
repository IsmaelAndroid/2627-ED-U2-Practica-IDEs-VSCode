# 2.2 · Actividad 4 · Gestionar extensiones: desactivar, desinstalar, actualizar y recomendar

Teoría: [2.2 apartado 5 "Desinstalación y actualización de extensiones"](https://revilofe.github.io/section3/u02/teoria/EDES-U2.2.-Modulos/).

> Abre este archivo y pulsa **Ctrl+Shift+V** para verlo con formato (vista previa de Markdown).

## PARTE A · Paso a paso con el profesor

**PASO 1 · Filtrar las extensiones**
Abre Extensions (**Ctrl+Shift+X**) y escribe en el buscador:

| Filtro | Qué muestra |
|---|---|
| `@installed` | las que tienes instaladas |
| `@enabled` / `@disabled` | las activas / desactivadas |
| `@updates` | las que tienen una actualización pendiente |
| `@recommended` | las recomendadas para este proyecto |

**PASO 2 · Desactivar una extensión (sin borrarla)**
En `@installed`, sobre **autopep8** pulsa la rueda ⚙ > **Disable**. Hay dos opciones:

- **Disable**: se desactiva en todos tus proyectos.
- **Disable (Workspace)**: se desactiva solo en este proyecto.

Abre `a3_ejercicio_limpia_codigo.py` y pulsa Shift+Alt+F: ya no formatea. Vuelve a activarla con **Enable**.
Así se mantiene el IDE ligero: solo activas lo que necesitas en cada proyecto.

**PASO 3 · Desinstalar**
Rueda ⚙ > **Uninstall** (en versiones antiguas, el icono de la papelera). La extensión desaparece. (Esto lo haremos en el ejercicio, no desinstales ahora la de Python.)

**PASO 4 · Actualizar**
VS Code actualiza las extensiones automáticamente. Puedes comprobarlo a mano con el botón **...** del panel de Extensions > **Check for Extension Updates**. Si una tiene versión nueva, aparece el botón **Update**.
En la rueda ⚙ de cada extensión también puedes **Install Specific Version...** para volver a una versión anterior.

**PASO 5 · Recomendar extensiones a tu equipo**
Si alguien abre tu proyecto, VS Code le puede sugerir las extensiones que necesita. Se guardan en `.vscode/extensions.json` dentro del proyecto:
Ctrl+Shift+P > **Extensions: Configure Recommended Extensions (Workspace Folder)**.

## PARTE B · Ahora tú

**E4.1** Instala la extensión **Error Lens** (de *Alexander*, `usernamehw.errorlens`). Abre `a1_extension_python.py`, descomenta el BLOQUE E1.3 y describe en RESPUESTAS.md qué cambia.

**E4.2** Desactiva **Error Lens** solo para este proyecto (**Disable (Workspace)**). Comprueba que deja de verse. Después desinstálala.

**E4.3** Crea el archivo `.vscode/extensions.json` del proyecto con las recomendaciones de las tres extensiones que hemos usado (Python, Pylint y autopep8). Escribe `@recommended` en el buscador y comprueba que salen.
Pista: el identificador de cada extensión aparece en su página (por ejemplo `ms-python.python`).

**E4.4** (Opcional) Instala **Spanish Language Pack for Visual Studio Code** (de Microsoft). Reinicia VS Code cuando te lo pida. ¿Qué ha cambiado? Si prefieres el inglés: Ctrl+Shift+P > **Configure Display Language** > `en`.

**E4.5** Contesta en RESPUESTAS.md: ¿qué diferencia hay entre desactivar y desinstalar una extensión? ¿Para qué sirve **Disable (Workspace)**?
