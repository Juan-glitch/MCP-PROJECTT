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
# BLOCK 4: Install Python Dependencies from requirements #
#########################################################

WORKDIR /home/$USERNAME/workspace

# Copy only requirements.txt first to optimize build cache :contentReference[oaicite:1]{index=1}
COPY requirements.txt ./

USER $USERNAME
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Explanation:
# - Installing dependencies early improves caching.
# - Using '--no-cache-dir' avoids pip cache in final image.
#########################################################
# BLOCK 5: Copy Application Code & Install debugpy     #
#########################################################

COPY . .

RUN pip install debugpy

# Explanation:
# - Application code is added after dependencies to avoid cache bust.
# - 'debugpy' enables VS Code remote debugging.
##############################################
# BLOCK 6: Final Setup                        #
##############################################

USER $USERNAME
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
WORKDIR /home/$USERNAME/workspace

# Explanation:
# - Ensures any scripts installed via pip are in PATH.
# - Starts in the workspace directory as non-root user.
