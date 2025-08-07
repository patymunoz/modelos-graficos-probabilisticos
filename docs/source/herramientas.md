# Herramientas

Este curso utiliza las siguientes herramientas y tecnologías:

---

## Tecnologías computacionales

- [Python](https://www.python.org/): lenguaje de programación principal.
- [Anaconda](https://www.anaconda.com/): distribución de Python con entorno científico integrado.
- [PyMC](https://www.pymc.io/welcome.html): biblioteca para modelado bayesiano.
- [pgmpy](https://pgmpy.org/): librería para trabajar con modelos gráficos probabilísticos.

---

## Configuración del entorno

A continuación, vamos paso a paso para preparar tu entorno de trabajo:

---

### 1. Instalar Anaconda

:::{note}
Anaconda facilita la instalación de Python, Jupyter y bibliotecas científicas sin conflictos.
:::

- Visita [https://www.anaconda.com](https://www.anaconda.com)
- Descarga la versión para tu sistema operativo (Windows, macOS o Linux)
- Sigue las instrucciones del instalador
- Verifica la instalación desde una terminal o consola:

```bash
conda --version
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

Tienes dos opciones para trabajar con los _notebooks_ y el código código:

#### Opción A: Trabajar en local (requiere Git, Anaconda y GitHub)

Vamos a seguir el repositorio del curso para mantenernos sincronizados con el material oficial.

Los pasos siguientes muestran cómo mantener actualizado tu repositorio local con los cambios del repositorio original `upstream`:

##### Pasos para clonar y conectarse al repositorio original

1. Ingresa al repositorio: [https://github.com/patymunoz/modelos-graficos-probabilisticos](https://github.com/patymunoz/modelos-graficos-probabilisticos)

2. Haz clic en **Fork** (esquina superior derecha) para crear una copia en tu cuenta de GitHub.

3. Abre **Git Bash** y clona tu fork en tu equipo (reemplaza `tu-usuario` por tu nombre de usuario en GitHub):

```bash
git clone https://github.com/tu-usuario/modelos-graficos-probabilisticos.git
cd modelos-graficos-probabilisticos
```

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
origin    https://github.com/tu-usuario/modelos-graficos-probabilisticos.git (fetch)
upstream  https://github.com/patymunoz/modelos-graficos-probabilisticos.git (fetch)
```

##### Mantener tu copia actualizada

Cuando el curso se actualice, puedes sincronizarte con:

```
git pull upstream main
```

Esto trae los cambios del curso original a tu copia local.

Luego, si quieres actualizar tu _fork_ en GitHub:

```
git push origin main
```

6. Crear y activar el entorno Conda

Después de clonar el repositorio, crea el entorno con:

```bash
conda env create --name mgp python
conda activate mgp
```

Luego instala las bibliotecas necesarias usando el archivo `ènvironment.yml` incluido en el repositorio:

```bash
conda env update --file environment.yml --prune
```

también puedes instalar manualmente las bibliotecas con:

```bash
pip install -r requirements.txt
```

7. Abre el proyecto en VSCode o IDE de preferencia.

#### Opción B: Usar Binder

- Abre los notebooks directamente desde el navegador.

- No necesitas instalar ningún software adicional.

- Para que el código de la clase se guarde, necesitas guardar una copia en PDF.

#### Opción C: Usar Google Colab

- Abre los notebooks directamente desde el navegador.

- No necesitas instalar ningún software adicional.

- Solo se requiere una cuenta de Google.

- Ideal si prefieres no configurar el entorno localmente.
