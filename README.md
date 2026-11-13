# ED · Unidad 2 · Entornos de desarrollo integrado con Visual Studio Code

Práctica guiada de **Entornos de Desarrollo (1º DAM)** para trabajar, con Visual Studio Code, los puntos de teoría:

| Punto | Teoría | Carpeta del proyecto |
|---|---|---|
| 2.1 | [Entornos de desarrollo integrado (IDEs)](https://revilofe.github.io/section3/u02/teoria/EDES-U2.1.-IDEs/) | `2.1-IDEs/` |
| 2.2 | [Gestión de módulos y extensiones](https://revilofe.github.io/section3/u02/teoria/EDES-U2.2.-Modulos/) | `2.2-Extensiones/` |
| 2.3 | [Personalización y automatización del entorno](https://revilofe.github.io/section3/u02/teoria/EDES-U2.3.-Personalizacion/) | `2.3-Personalizacion/` |

## Cómo se trabaja

Cada actividad es un archivo (`A1_...`, `A2_...`) con dos partes:

1. **PARTE A · Paso a paso con el profesor.** Los pasos están escritos en los comentarios del propio archivo. Los hacemos **juntos en clase**: el profesor lo hace en el proyector y tú lo repites en tu ordenador.
2. **PARTE B · Ahora tú.** Al final del archivo hay **ejercicios pequeños** para que practiques lo mismo tú solo.

Las respuestas escritas (preguntas, tablas, salidas de programas) van en el archivo `RESPUESTAS.md` de cada carpeta.

Sigue este orden:

```
2.1-IDEs/
   a1_conoce_vscode.py        Zonas de VS Code y componentes de un IDE
   a2_editor_avanzado.py      Atajos del editor: multicursor, mover líneas, buscar/reemplazar
   a3_git_integrado.py        Control de versiones integrado (Source Control)
   RESPUESTAS.md
2.2-Extensiones/
   a1_extension_python.py     Instalar la extensión Python: ejecutar, IntelliSense, errores
   a2_depurador.py            Depurador: puntos de interrupción, variables, paso a paso
   a3_linter_formateador.py   Pylint (linter) y autopep8 (formateador)
   a3_ejercicio_limpia_codigo.py
   a4_gestionar_extensiones.md  Desactivar, desinstalar, actualizar, recomendar extensiones
   RESPUESTAS.md
2.3-Personalizacion/
   a1_apariencia.py           Tema, fuente, configuración de usuario y de proyecto, perfiles
   a2_atajos.py               Atajos de teclado personalizados
   a3_tareas.py               Automatizar con tareas (tasks.json)
   a4_tests/calculos.py       Pruebas automáticas con pytest
   a4_tests/test_calculos.py
   RESPUESTAS.md
```

## Antes de empezar (una sola vez)

1. Instala **Visual Studio Code**: <https://code.visualstudio.com/download>
2. Instala **Python 3**: <https://www.python.org/downloads/> (en Windows marca **"Add python.exe to PATH"**).
3. Descarga el proyecto. Lo mejor es **clonarlo** (así en la actividad 2.1-A3 verás Git integrado):

   ```bash
   git clone https://github.com/IsmaelAndroid/2627-ED-U2-Practica-IDEs-VSCode.git
   ```

   También puedes usar **Code > Download ZIP** y descomprimirlo.
4. Abre VS Code y usa **File > Open Folder...** (*Archivo > Abrir carpeta...*) sobre la carpeta del proyecto. Abre siempre **la carpeta raíz**, no un archivo suelto.

> VS Code puede estar en inglés o en español. En las instrucciones verás el menú en inglés y, entre paréntesis, en español: **File > Open Folder** (*Archivo > Abrir carpeta*).

## Entrega

No hay entrega: es material de práctica. Si lo has clonado, haz commits de tu trabajo y súbelo a **tu propio** repositorio si quieres guardarlo.
