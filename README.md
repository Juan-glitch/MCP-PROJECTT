## Development workflow

Active work happens on the `dev` branch. Changes are merged into `main` when they are ready for release.

## Directory layout

- `mcp_project/` – source code for the package.
- `requirements.txt` – project dependencies.
- `pyproject.toml` – build configuration.
- `tests/` – unit tests.

### Show the project tree

Display the folder structure using:

```bash
python -m mcp_project.tree
# or
python -m mcp_project tree
```

### Use ``ProjectTree`` in your code

You can also build the listing programmatically:

```python
from mcp_project import ProjectTree

tree = ProjectTree(".")
for line in tree.build_tree():
    print(line)
```

### Run tests

Execute the test suite with:

```bash
python -m pytest
```
=======
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

Consulta el directorio `docs/guides/` para guias de uso y estilo. Los materiales del curso MCP estan en `docs/course/`.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.


## Course Materials

This repository now focuses on the "MCP: Build Rich-Context AI Apps with Anthropic" course. See `docs/course/mcp_course_overview.md` for details and future steps.
