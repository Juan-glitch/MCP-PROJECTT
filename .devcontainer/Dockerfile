# Dockerfile
FROM python:3.13-slim

# ───────────────────────────────────────────────────────────────
# ENTORNOS Y VARIABLES DE CONFIGURACIÓN
# ───────────────────────────────────────────────────────────────
ENV DEBIAN_FRONTEND=noninteractive \
    PATH="/workspace/MCP-PROJECTT/.venv/bin:$PATH" \
    VIRTUAL_ENV="/workspace/MCP-PROJECTT/.venv"

# ───────────────────────────────────────────────────────────────
# DEPENDENCIAS DEL SISTEMA
# ───────────────────────────────────────────────────────────────
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    git \
    build-essential \
 && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
 && apt-get install -y --no-install-recommends nodejs \
 && rm -rf /var/lib/apt/lists/*

# ───────────────────────────────────────────────────────────────
# INSTALAR uv
# ───────────────────────────────────────────────────────────────
RUN pip install --no-cache-dir uv

# ───────────────────────────────────────────────────────────────
# DIRECTORIO DE TRABAJO
# ───────────────────────────────────────────────────────────────
WORKDIR /workspace/MCP-PROJECTT

# ───────────────────────────────────────────────────────────────
# CACHÉ INTELIGENTE: primero manifiestos y README
# ───────────────────────────────────────────────────────────────
COPY pyproject.toml uv.lock* README.md ./

# Crear entorno virtual e instalar dependencias
RUN uv venv && uv sync --frozen

# ───────────────────────────────────────────────────────────────
# Copiar el resto del código del proyecto
# ───────────────────────────────────────────────────────────────
COPY . .

# Instalar en modo editable (requiere código ya copiado)
RUN uv pip install -e .

# ───────────────────────────────────────────────────────────────
# Configurar entorno interactivo con bash
# ───────────────────────────────────────────────────────────────
RUN echo '[ -f "$VIRTUAL_ENV/bin/activate" ] && source "$VIRTUAL_ENV/bin/activate"' >> /root/.bashrc \
 && echo 'cd /workspace/MCP-PROJECTT' >> /root/.bashrc

# ───────────────────────────────────────────────────────────────
# EXPONER PUERTOS
# ───────────────────────────────────────────────────────────────
EXPOSE 6274 6277

# ───────────────────────────────────────────────────────────────
# SHELL INTERACTIVO POR DEFECTO
# ───────────────────────────────────────────────────────────────
CMD ["bash"]
