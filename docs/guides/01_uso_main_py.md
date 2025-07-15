# Documentación del Script Principal (`main.py`)

## Propósito

Este script ejecuta un procesamiento por lotes de archivos de imagen (imágenes ráster y SVGs) según una configuración definida en un archivo YAML. El objetivo es automatizar la transformación o manipulación de estos archivos con parámetros personalizables.

## Uso

```bash
python main.py -c config.yml
```

### Argumentos

* `-c, --config`: Ruta al archivo de configuración YAML. Este argumento es obligatorio.

> Nota: Actualmente, el script fuerza por defecto el uso de `config.yml` mediante `sys.argv += ["-c", "config.yml"]`.

## Estructura General

### 1. Importaciones

Importa librerías necesarias del sistema y módulos locales:

* `argparse`, `os`, `sys`, `typing`, `pathlib`
* `batch_process_images`, `batch_process_svgs`: Funciones que ejecutan el procesamiento de imágenes y SVGs respectivamente.
* `load_config`: Función para cargar y parsear el archivo YAML de configuración.

### 2. Carga de Configuración

Lee el archivo YAML especificado por el usuario y lo interpreta como un diccionario Python.

```python
cfg: Dict[str, Any] = load_config(args.config)
```

### 3. Configuración de Directorios

* `src_root`: Ruta de entrada de archivos (por defecto `./00_Imgs`)
* `dst_root`: Ruta de salida de archivos (por defecto `./output`)

Se crean los directorios de salida si no existen.

### 4. Procesamiento por Lotes

* Si existe la sección `images` en el YAML, se llama a `batch_process_images()`.
* Si existe la sección `icons`, se llama a `batch_process_svgs()`.
* Se muestra un mensaje si alguna de las secciones está ausente.

## Ejemplo de Archivo `config.yml`

```yaml
src: "./imagenes"
dst: "./procesadas"

images:
  resize: [800, 600]
  format: "JPEG"
  quality: 85

icons:
  color: "#000000"
  size: [128, 128]
```

## Estructura de Carpetas

```
project_root/
├── main.py
├── config.yml
├── modules/
│   ├── images/
│   │   └── imgPipeline.py
│   ├── icons/
│   │   └── iconPipeline.py
│   └── utils.py
├── 00_Imgs/  # Carpeta por defecto para archivos de entrada
└── output/   # Carpeta de salida
```

## Dependencias

* Python 3.7+
* PyYAML u otra librería para parsear YAML (según implementación de `load_config`)

## Licencia

Este proyecto está licenciado bajo los términos especificados en el archivo `LICENSE` adjunto.

## Autoría y Mantenimiento

El script está diseñado para ser modular, facilitando el mantenimiento y ampliación mediante `imgPipeline` e `iconPipeline`. Para colaborar o sugerir mejoras, revisa las instrucciones del repositorio correspondiente.
