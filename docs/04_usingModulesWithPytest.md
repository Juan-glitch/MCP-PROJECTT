# 📦 Cómo usar módulos con Pytest

Esta guía explica cómo estructurar y utilizar tus módulos de Python para que puedan ser fácilmente testeados con `pytest`.

---

## 📁 Estructura del proyecto

Supongamos que tu proyecto está estructurado así:

```
MCP-PROJECTT/
├── mcp_project/
│   ├── __init__.py
│   ├── cli.py
│   └── core/
│       ├── __init__.py
│       └── tree.py  ← contiene ProjectTree
├── tests/
│   └── test_tree.py ← contiene test_build_tree()
├── pyproject.toml
```

Para usar y testear `ProjectTree`, debes:

1. Definirlo en `mcp_project/core/tree.py`.
2. Importarlo con su ruta completa: `from mcp_project.core import ProjectTree`
3. Colocar los tests dentro de la carpeta `tests/` con archivos llamados `test_*.py`.

---

## 🧪 Escribir módulos testeables

Supón que tu módulo es:

```python
# mcp_project/core/tree.py
class ProjectTree:
    def __init__(self, root_path: str):
        self.root_path = root_path

    def build_tree(self) -> list[str]:
        return ["mocked tree"]
```

Entonces tu test puede ser:

```python
# tests/test_tree.py
from mcp_project.core import ProjectTree

def test_build_tree(tmp_path):
    (tmp_path / "dirA").mkdir()
    (tmp_path / "dirA" / "file.txt").write_text("hi")
    tree = ProjectTree(str(tmp_path))
    lines = tree.build_tree()
    assert any("dirA/" in line for line in lines)
```

---

## 🏃‍♂️ Ejecutar los tests

Una vez escrito el test, desde la raíz del proyecto ejecuta:

```bash
pytest
```

Pytest hará lo siguiente:
- Detectará todos los archivos `test_*.py`
- Importará tus módulos usando el `PYTHONPATH` (configurado al instalar en modo editable)
- Usará automáticamente fixtures como `tmp_path`

---

## 🧠 Cómo funcionan los imports en tests

Para importar tu propio código en los tests:

- El paquete debe estar instalado con `pip install -e .`
- Usa imports completos como:

```python
from mcp_project.core import ProjectTree
```

- No uses imports relativos como `from ..core import ProjectTree` en los tests.

---

## 🛠️ Consejos útiles

- Instala tu paquete en modo editable:

```bash
pip install -e .
```

- Usa una carpeta `tests/` para mantener separados los tests del código fuente.
- Nombra los archivos de test como `test_*.py` y las funciones como `test_*()`.
- Usa fixtures como `tmp_path` para simular sistemas de archivos temporales.

---

## ✅ Resumen

| Tarea              | Qué hacer                                                  |
|--------------------|-------------------------------------------------------------|
| Escribir un módulo | Dentro de `mcp_project/` o sus subcarpetas                 |
| Escribir tests     | Dentro de `tests/` con nombre `test_*.py`                  |
| Importar módulos   | Usa imports completos (`from mcp_project...`)              |
| Ejecutar tests     | Desde raíz: `pytest`                                       |
| Instalar el paquete| `pip install -e .` antes de testear                        |

---

Con esto tus módulos estarán organizados y listos para ser testeados profesionalmente usando `pytest`.

