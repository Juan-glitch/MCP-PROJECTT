# ImgProcessingContainer

## Descripción

**ImgProcessingContainer** es un entorno de desarrollo basado en Docker para el procesamiento de imágenes y SVGs de forma eficiente, modular y escalable. Permite manipular imágenes por lotes (como redimensionado, cambio de formato o transformaciones avanzadas) utilizando configuraciones flexibles definidas en YAML.

## Características Principales

* Entorno aislado y reproducible mediante Docker.
* Procesamiento de imágenes ráster y vectores SVG.
* Modularidad para incorporar nuevos flujos de procesamiento.
* Soporte para modelos de escalado por red neuronal (ej. FSRCNN).
* Configurable vía archivo `config.yml`.

---

## Estructura del Proyecto

```
ImgProcessingContainer/
├── .devcontainer/          # Configuración del entorno de desarrollo remoto
├── .vscode/                # Configuración de VS Code (debug, tareas, etc.)
├── docs/                   # Documentación y guías del proyecto
├── modules/                # Módulos principales de procesamiento
│   ├── icons/              # Procesamiento de SVGs
│   ├── images/             # Procesamiento de imágenes ráster
│   ├── models/             # Modelos preentrenados para escalado
│   ├── project_tree/       # Generación del árbol de estructura
│   └── utils/              # Funciones de utilidad comunes
├── resources/              # Scripts y recursos adicionales
├── config.yml              # Archivo de configuración YAML
├── LICENSE                 # Licencia del proyecto (MIT)
├── main.py                 # Script principal de ejecución
└── README.md               # Este archivo
```

---

## Módulos Disponibles

### `icons`

* `iconPipeline.py`: Procesamiento de archivos SVG (colores, tamaño, optimizaciones).

### `images`

* `imgPipeline.py`: Ejecutor principal del pipeline de imágenes.
* `imgTransforms.py`: Transformaciones como recortes, escalado y cambios de color.
* `upscale.py`: Escalado de imágenes mediante redes neuronales (FSRCNN).

### `project_tree`

* `project_tree.py`: Generador ASCII de la estructura del proyecto.

### `utils`

* `utils.py`: Carga de configuraciones, funciones auxiliares.

### `models`

* `FSRCNN_x2.pb`: Modelo preentrenado para superresolución de imágenes.

---

## Requisitos

* [Docker](https://www.docker.com/) instalado en el sistema.
* Python 3.12+
* Dependencias listadas en el entorno Docker (por ejemplo, `PyYAML`, `Pillow`, `opencv-python`, etc.)

---

## Instalación y Ejecución

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tuusuario/ImgProcessingContainer.git
cd ImgProcessingContainer
```

2. **Construir la imagen Docker:**

```bash
docker build -t imgprocessingcontainer .
```

3. **Ejecutar el contenedor:**

```bash
docker run -it --rm -v $(pwd):/workspace imgprocessingcontainer
```

4. **Ejecutar el script principal:**

```bash
python main.py -c config.yml
```

> Puedes personalizar `config.yml` para adaptar el comportamiento del pipeline.

---

## Ejemplo de `config.yml`

```yaml
src: "./00_Imgs"
dst: "./output"

images:
  resize: [1024, 768]
  format: "png"
  quality: 80

icons:
  size: [64, 64]
  color: "#FF0000"
```

---

## Documentación

Consulta el directorio `docs/` para guías de uso, estilo, contribución y más información sobre los pipelines internos.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
