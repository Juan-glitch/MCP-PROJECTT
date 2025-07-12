## Development workflow

Active work happens on the `dev` branch. Changes are merged into `main` when they are ready for release.

## Directory layout

- `mcp_project/` – source code for the package.
- `requirements.txt` – project dependencies.
- `pyproject.toml` – build configuration.
- `tests/` – unit tests.
- `docs/02_codex.md` – guía para colaborar con **Codex**.
- `.codex/` – almacén de notas persistentes para Codex.

### Show the project tree

Display the folder structure using:

```bash
python -m mcp_project.tree
# or
python -m mcp_project tree
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

Consulta el directorio `docs/` para guías de uso, estilo, contribución y más información sobre los pipelines internos.
En particular, `docs/02_codex.md` describe cómo colaborar con Codex y usar la carpeta `.codex` para compartir contexto.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

