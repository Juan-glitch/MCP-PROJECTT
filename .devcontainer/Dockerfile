#######################################################
# BLOCK 1: Base Image & Environment Setup             #
#######################################################

FROM python:3.13.5-slim-bookworm
ENV DEBIAN_FRONTEND=noninteractive

# -----------------------------------------------------
# Explanation:
# - Uses the latest patched Python 3.13.5 on Debian Bookworm (slim).
# - Debian Bookworm is regularly updated to patch critical CVEs.
# - 'DEBIAN_FRONTEND=noninteractive' ensures non-interactive apt installs.
# -----------------------------------------------------

#########################################################
# BLOCK 2: Install & Upgrade System-Level Dependencies  #
#########################################################

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    sudo \
    git \
    wget \
    curl \
    xvfb \
    ca-certificates \
    gnupg \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------
# Explanation:
# - 'apt-get update': refreshes package index
# - 'apt-get upgrade -y': ensures critical CVEs are patched
# - '--no-install-recommends': avoids installing optional (unused) packages
# - 'ca-certificates': ensures HTTPS-based connections work securely
# - 'gnupg': sometimes needed for package verification
# - 'rm -rf /var/lib/apt/lists/*': deletes cached metadata to reduce image size
# -----------------------------------------------------

#######################################################
# BLOCK 2.5: Install `uv` (pip replacement by Astral) #
#######################################################

# 1. Instala uv usando el instalador oficial (binarios precompilados)
ENV UV_VERSION=0.7.21
RUN curl -LsSf https://astral.sh/uv/${UV_VERSION}/install.sh | sh

# 2. Instala uv desde PyPI como fallback
RUN pip install --no-cache-dir uv

# 3. (Opcional) Fija el modo de enlace para evitar warnings en Docker
ENV UV_LINK_MODE=copy

# Asegura que uv esté en PATH durante el build
ENV PATH="/root/.local/bin:${PATH}"

# -----------------------------------------------------
# Explanation:
# - Se instala uv vía script ‘curl | sh’ para evitar depender de Python o cargo.
# - Añade instalación desde PyPI por si prefieres gestionarlo con pip/pipx.
# - ENV UV_LINK_MODE=copy evita warnings de hardlink en entornos Docker.
# - Añadir a PATH garantiza disponibilidad durante los posteriores RUN.
# -----------------------------------------------------

    @@
 # -----------------------------------------------------
 # - 'rm -rf /var/lib/apt/lists/*': deletes cached metadata to reduce image size
 # -----------------------------------------------------
    
##########################################################
# BLOCK 2.6: Install Node.js and npm (via NodeSource)    #
##########################################################

# Node.js LTS setup for Debian-based image (via NodeSource)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Verify installation
RUN node -v && npm -v

# -----------------------------------------------------
# Explanation:
# - Installs latest Node.js 18.x LTS (stable) from NodeSource
# - Installs both node and npm
# - Adds version checks to confirm success
# -----------------------------------------------------

##############################################
# BLOCK 3: Create Non-Root Developer User    #
##############################################

ARG USERNAME=devuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# -----------------------------------------------------
# Explanation:
# - Security best practice: Avoid running as root in containers
# - 'sudo' access is granted so developer can install/modify things if needed
# - We store the sudo rule in a dedicated file and restrict its permissions
# -----------------------------------------------------

#########################################################
# BLOCK 4: Install Python Dependencies via uv           #
#########################################################

WORKDIR /home/$USERNAME/workspace

# Copiamos solo pyproject.toml para aprovechar cache
COPY pyproject.toml ./

USER $USERNAME
RUN uv pip install

# -----------------------------------------------------
# Explanation:
# - Instala dependencias usando uv a partir de pyproject.toml
# - Crea .venv y lo usa automáticamente
# -----------------------------------------------------

#########################################################
# BLOCK 5: Copy Application Code & Install debugpy      #
#########################################################

COPY --chown=$USERNAME:$USERNAME . .

RUN uv pip install debugpy

# -----------------------------------------------------
# Explanation:
# - Se copia el código después para evitar invalidar la cache previa.
# - debugpy habilita depuración remota desde VS Code.
# -----------------------------------------------------

##############################################
# BLOCK 6: Final Setup                        #
##############################################

USER $USERNAME
ENV PATH="/home/${USERNAME}/.local/bin:/home/${USERNAME}/workspace/.venv/bin:${PATH}"
WORKDIR /home/$USERNAME/workspace

# -----------------------------------------------------
# Explanation:
# - PATH incluye binarios instalados por uv y el entorno virtual .venv.
# - Se establece el directorio de trabajo como workspace del usuario final.
# -----------------------------------------------------
