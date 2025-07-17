#######################################################
# BLOCK 1: Base Image & Environment Setup             #
#######################################################
FROM python:3.13.5-slim-bookworm
ENV DEBIAN_FRONTEND=noninteractive

#########################################################
# BLOCK 2: Install & Upgrade System-Level Dependencies  #
#########################################################
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
      sudo git wget curl xvfb ca-certificates gnupg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

#######################################################
# BLOCK 2.5: Install `uv` (pip replacement by Astral) #
#######################################################
ENV UV_VERSION=0.7.21 \
    UV_LINK_MODE=copy \
    UV_CONFIG_FILE=/dev/null \
    PATH="/root/.local/bin:${PATH}"

RUN curl -LsSf https://astral.sh/uv/${UV_VERSION}/install.sh | sh && \
    pip install --no-cache-dir uv

##########################################################
# BLOCK 2.6: Install Node.js and npm (via NodeSource)    #
##########################################################
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN node -v && npm -v

#########################################################
# BLOCK 3: Copy & Install Python Dependencies as root   #
#########################################################
WORKDIR /workspace
COPY . .

# Instalación de tu paquete y debugpy en /usr/local
RUN uv pip install --system --link-mode copy -e . && \
    uv pip install --system debugpy

#########################################################
# BLOCK 4: Create Non-Root Developer User (secure)      #
#########################################################
ENV USERNAME=devuser \
    USER_UID=1000 \
    USER_GID=1000

RUN if ! getent group "${USERNAME}" >/dev/null; then \
      groupadd --gid "${USER_GID}" "${USERNAME}"; \
    fi && \
    if ! id -u "${USERNAME}" >/dev/null 2>&1; then \
      useradd --uid "${USER_UID}" --gid "${USER_GID}" -m "${USERNAME}"; \
    fi && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME} && \
    chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}

#########################################################
# BLOCK 5: Final Setup for Non-Root Workflow           #
#########################################################
USER ${USERNAME}
WORKDIR /home/${USERNAME}/workspace
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
