# 📚 Tutorial: Qué es un paquete de Python y cómo se usa

Este documento sirve como referencia wiki para entender qué es un paquete de Python, cómo se estructura y cómo se ha implementado en este proyecto (`MCP-PROJECTT`).

---

## ✨ ¿Qué es un paquete de Python?

Un **paquete de Python** es una forma de organizar y distribuir módulos de código para que puedan ser **instalados**, **importados** y **reutilizados** fácilmente.

A diferencia de un simple script `.py`, un paquete:

- Puede tener **estructura jerárquica** de módulos.
- Puede ser **instalado con pip** (`pip install .` o `pip install -e .`).
- Puede ofrecer un **CLI (Command Line Interface)**.
- Puede ser **publicado en PyPI** para compartir con la comunidad.

---

## 🔹 Cuándo usar un paquete

| Caso                          | ¿Usar paquete?      | Por qué                                             |
| ----------------------------- | ------------------- | --------------------------------------------------- |
| Proyecto de 1 script          | ❌ No necesariamente | Un solo archivo puede ser suficiente.               |
| Herramienta reutilizable      | ✅ Sí                | Se puede instalar e importar desde otros proyectos. |
| Proyecto con submódulos o CLI | ✅ Sí                | Mejora organización, pruebas y mantenibilidad.      |
| Script rápido y puntual       | ❌ No                | No vale la pena estructurarlo como paquete.         |

---

## 📂 Estructura típica de un paquete Python

```
miproyecto/
├── pyproject.toml        # Metadatos y configuración de build
├── README.md             # Descripción del proyecto
├── miproyecto/           # Paquete principal
│   ├── __init__.py       # Hace que sea un paquete
│   ├── __main__.py       # Entrada para `python -m miproyecto`
│   ├── cli.py            # CLI del paquete
│   └── core/             # Submódulos
│       ├── __init__.py
│       └── tree.py       # Clase interna por ejemplo
└── py.typed              # (opcional) Para indicar que incluye tipado
```

---

## ⚖️ pyproject.toml básico

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "mcp_project"
version = "0.1.0"
description = "Example project skeleton"
readme = "README.md"
requires-python = ">=3.11"

[project.scripts]
mcp-project = "mcp_project.cli:main"

[tool.setuptools.packages.find]
where = ["."]

[tool.setuptools.package-data]
"mcp_project" = ["py.typed"]
```

---

## ▶️ Comandos últiles

### Instalación editable (desarrollo)

```bash
pip install -e .
```

Permite editar el código sin reinstalar.

### Ejecutar el paquete directamente

```bash
python -m mcp_project
```

Ejecuta `__main__.py` del paquete.

### Ejecutar el CLI personalizado

```bash
mcp-project
```

Ejecuta `cli.py` a través del entrypoint definido.

### Verificar instalación del paquete

```bash
pip list | grep mcp
```

### Importar desde otro proyecto/script

```python
from mcp_project.cli import main
```

---

## 🚀 Ventajas de usar paquetes

- Reutilización de código y organización módular
- CLI reutilizable y accesible desde terminal
- Facilidad para testing y distribución
- Compatible con herramientas modernas (pytest, linters, MyPy, etc.)
- Listo para publicarse en PyPI si se desea

---

## ✉️ Recomendaciones

- Usa `pip install -e .` durante el desarrollo.
- Mantén una estructura clara del paquete.
- Usa `__main__.py` solo para redirigir a tu CLI.
- Agrega un `py.typed` si quieres que herramientas de tipado funcionen bien.
- Considera usar DevContainers si necesitas entornos portables o multiplataforma.

---

## 📚 Recursos

- [Documentación oficial de paquetes Python](https://packaging.python.org/en/latest/)
- [PEP 621 – pyproject.toml specification](https://peps.python.org/pep-0621/)
- [Setuptools documentation](https://setuptools.pypa.io/en/latest/)

---

Este documento forma parte del repositorio `MCP-PROJECTT` como referencia interna de aprendizaje y desarrollo.

