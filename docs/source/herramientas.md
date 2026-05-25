# Herramientas

Este curso utiliza las siguientes herramientas y tecnologías:

---

## Tecnologías computacionales

- [Python](https://www.python.org/): lenguaje de programación principal.
- [uv](https://docs.astral.sh/uv/): gestor rápido de entornos virtuales y paquetes para Python.
- [PyMC](https://www.pymc.io/welcome.html): biblioteca para modelado bayesiano.
- [pgmpy](https://pgmpy.org/): librería para trabajar con modelos gráficos probabilísticos.

---

## Configuración del entorno

A continuación, vamos paso a paso para preparar tu entorno de trabajo:

---

### 1. Instalar uv

:::{note}
`uv` facilita la creación de entornos virtuales e instalación de dependencias de forma rápida y reproducible.
:::

- Visita la guía oficial: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
- Elige el método para tu sistema operativo (Windows, macOS o Linux)
- Sigue las instrucciones del instalador
- Verifica la instalación desde una terminal o consola:

```bash
uv --version
```

### 2. Instalar Git

:::{tip}
Git te permite clonar repositorios y controlar versiones de tu código.
:::

- Descárgalo desde: [https://git-scm.com/](https://git-scm.com/)
- Instálalo con las opciones predeterminadas

:::{important}
Si usas Windows, se recomienda usar Git Bash en lugar del símbolo del sistema o PowerShell.
:::

#### ¿Qué es Git Bash?

- **Git Bash** es una terminar que se instala junto con Git en Windows.
- Proporciona comandos similares a los de Linux/macOS (`ls`, `cd`, `rm`, etc.)

Puedes abrir Git Bash desde el menú de inicio, buscando "Git Bash".

Verifica la instalación de Git con:

```bash
git --version
```

### 3. Crear una cuenta en GitHub

- Abre [https://github.com](https://github.com)
- Crea una cuenta gratuita
- Esta cuenta te permitirá acceder al repositorio del curso y, si lo deseas, contribuir con tus propios cambios.

### 4. Elegir cómo seguir el curso

Tienes varias opciones para trabajar con los _notebooks_:

#### Opción A: Trabajar en local (requiere Git, uv y GitHub)

Vamos a seguir el repositorio del curso para mantenernos sincronizados con el material oficial.

Los pasos siguientes muestran cómo mantener actualizado tu repositorio local con los cambios del repositorio original `upstream`:

##### Pasos para clonar y conectarse al repositorio original

1. Ingresa al repositorio: [https://github.com/patymunoz/modelos-graficos-probabilisticos](https://github.com/patymunoz/modelos-graficos-probabilisticos)

2. Haz clic en **Fork** (esquina superior derecha) para crear una copia en tu cuenta de GitHub.

3. Abre **Git Bash** y clona tu fork en tu equipo:

```bash
git clone https://github.com/patymunoz/modelos-graficos-probabilisticos.git
```

3.1. Navega al directorio del proyecto:

```bash
cd modelos-graficos-probabilisticos
```

3.2. Verifica que estás en la rama actual `v2026`:

```bash
git branch
```

> Deberías ver un asterisco (\*) junto a `v2026`.

4. Agrega el repositorio original como remoto adicional `upstream`, para mantenerte sincronizado con los cambios del curso:

```bash
git remote add upstream https://github.com/patymunoz/modelos-graficos-probabilisticos.git
```

5. Verifica que tienes ambos remotos configurados:

```bash
git remote -v
```

Deberías ver algo como:

```bash
origin    https://github.com/**tu-usuario**/modelos-graficos-probabilisticos.git (fetch)
upstream  https://github.com/patymunoz/modelos-graficos-probabilisticos.git (fetch)
```

##### Mantener tu copia actualizada

Cuando el curso se actualice, puedes sincronizarte con:

```
git checkout v2026
git pull upstream v2026
```

Esto trae los cambios del curso original a tu copia local.

Luego, si quieres actualizar tu _fork_ en GitHub:

```
git push origin v2026
```

6. Crear y activar el entorno virtual con uv

Después de clonar el repositorio, crea el entorno con:

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r requirements.txt
```

En Windows (PowerShell), activa el entorno con:

```powershell
.venv\Scripts\Activate.ps1
```

7. Abre el proyecto en VSCode o IDE de preferencia.

#### Opción B: Usar Binder

- Necesitas abrir [este enlace.](https://mybinder.org/v2/gh/patymunoz/modelos-graficos-probabilisticos/main)

#### Opción C: Usar Google Colab

- Descarga los notebooks directamente del [repositorio.](https://github.com/patymunoz/modelos-graficos-probabilisticos)

- Abre los notebooks directamente desde el navegador.

- No necesitas instalar ningún software adicional.

- Solo se requiere una cuenta de Google.

- Ideal si prefieres **no configurar el entorno localmente.**

#### Opción D: Usar con Spyder

- Descarga los notebooks directamente del [repositorio.](https://github.com/patymunoz/modelos-graficos-probabilisticos)

- Abre Spyder y carga los notebooks.
