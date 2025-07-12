# 🛠️ Guía Completa: Entorno de Desarrollo con DevContainers en Windows

## 🤔 ¿Por qué necesitamos esto? (La historia detrás de la tecnología)

Imagina que cada desarrollador en tu equipo tiene una computadora diferente. Uno usa Windows 10, otro Windows 11, algunos tienen versiones diferentes de Python instaladas, otros tienen Node.js versión 16 mientras que algunos tienen la versión 18. Cuando uno de ellos dice "en mi computadora funciona perfectamente", pero en la tuya no funciona, estás experimentando el clásico problema de "funciona en mi máquina".

Los **contenedores de desarrollo** (DevContainers) solucionan este problema creando un "ambiente virtual" idéntico para todos. Es como si cada desarrollador tuviera exactamente la misma computadora con las mismas herramientas instaladas, sin importar qué computadora física esté usando.

## 🧠 Conceptos fundamentales que necesitas entender

### ¿Qué es Docker?
Docker es como una "máquina virtual muy ligera". Piensa en ello como crear una caja completamente aislada dentro de tu computadora donde puedes instalar un sistema operativo diferente y todas las herramientas que necesitas, sin que esto afecte tu computadora principal. Esta "caja" se llama **contenedor**.

La gran ventaja es que esta caja es portátil: la puedes compartir con otros desarrolladores y funcionará exactamente igual en sus computadoras.

### ¿Qué es WSL 2?
WSL significa "Windows Subsystem for Linux". Es una tecnología de Microsoft que te permite ejecutar Linux dentro de Windows de manera nativa y eficiente. WSL 2 es la versión mejorada que es mucho más rápida y compatible.

¿Por qué necesitamos Linux? Porque Docker originalmente fue diseñado para Linux, y muchas herramientas de desarrollo funcionan mejor en este sistema operativo.

### ¿Qué son los DevContainers?
Los DevContainers son contenedores Docker especialmente configurados para desarrollo. Visual Studio Code puede "conectarse" a estos contenedores y trabajar como si estuvieras programando directamente en esa máquina virtual, pero con toda la comodidad de tu editor favorito.

---

## ✅ Requisitos Previos

Antes de comenzar, verifica que tu computadora cumple con estos requisitos:

**Sistema Operativo**: Windows 10 versión 22H2 o superior, o Windows 11. Para verificar tu versión, presiona las teclas Windows + R, escribe `winver` y presiona Enter.

**Virtualización habilitada**: Esta es una característica del procesador que debe estar activada en la BIOS. Para verificar si ya está habilitada, abre el Administrador de tareas (Ctrl + Shift + Esc), ve a la pestaña "Rendimiento", selecciona "CPU" y busca donde dice "Virtualización". Debe aparecer como "Habilitada".

Si la virtualización no está habilitada, necesitarás entrar a la BIOS de tu computadora al reiniciar. Esto varía según el fabricante, pero generalmente se hace presionando F2, F12, o Delete durante el arranque.

---

## 📋 Paso 1: Instalar WSL 2 (El puente entre Windows y Linux)

WSL 2 es la base que permitirá que Docker funcione correctamente en Windows.

### Instalación automática (método recomendado):

Abre PowerShell como administrador. Para hacer esto, busca "PowerShell" en el menú de inicio, haz clic derecho sobre "Windows PowerShell" y selecciona "Ejecutar como administrador".

Una vez abierto, ejecuta este comando y presiona Enter:

```powershell
wsl --install
```

Este comando hará varias cosas automáticamente:
- Habilitará las características necesarias de Windows
- Descargará e instalará el kernel de Linux para WSL 2
- Instalará Ubuntu como distribución predeterminada de Linux

Después de que termine la instalación, **debes reiniciar tu computadora**. Este paso es crucial y no opcional.

### Configuración inicial después del reinicio:

Cuando reinicies, se abrirá automáticamente una ventana de Ubuntu pidiendo que crees un usuario y contraseña para tu sistema Linux. Este usuario es completamente independiente de tu usuario de Windows.

Elige un nombre de usuario sencillo (sin espacios ni caracteres especiales) y una contraseña que puedas recordar. Esta información la necesitarás ocasionalmente.

### Verificación de la instalación:

Para confirmar que todo funcionó correctamente, abre una nueva ventana de PowerShell y ejecuta:

```powershell
wsl --list --verbose
```

Deberías ver algo como:
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

Si aparece "VERSION 2", estás listo para continuar.

---

## 📋 Paso 2: Instalar Docker Desktop

Docker Desktop es la aplicación que te permitirá crear y manejar contenedores de manera visual y sencilla.

### Descargar Docker Desktop:

Ve al sitio web oficial de Docker: https://www.docker.com/products/docker-desktop/

Haz clic en "Download for Windows" y descarga el instalador. El archivo será algo como "Docker Desktop Installer.exe".

### Instalar Docker Desktop:

Ejecuta el instalador descargado con permisos de administrador (clic derecho → "Ejecutar como administrador").

Durante la instalación, asegúrate de que estén marcadas estas opciones:
- "Use WSL 2 instead of Hyper-V" (Usar WSL 2 en lugar de Hyper-V)
- "Add shortcut to desktop" (Agregar acceso directo al escritorio)

La instalación tomará varios minutos porque descargará componentes adicionales de internet.

### Configuración inicial de Docker Desktop:

Después de la instalación, **reinicia tu computadora nuevamente**.

Al reiniciar, Docker Desktop debería iniciarse automáticamente. Si no lo hace, búscalo en el menú de inicio y ábrelo.

La primera vez que se ejecute, puede tardar unos minutos en inicializar todos los servicios. Verás un ícono de Docker en la barra de tareas (esquina inferior derecha). Cuando esté listo, el ícono dejará de parpadear.

### Verificar que Docker está funcionando:

Abre PowerShell y ejecuta:

```powershell
docker --version
```

Deberías ver algo como: `Docker version 24.0.6, build ed223bc`

También puedes probar ejecutar un contenedor de prueba:

```powershell
docker run hello-world
```

Este comando descargará una imagen pequeña de prueba y ejecutará un contenedor que imprimirá un mensaje de bienvenida. Si ves el mensaje "Hello from Docker!", significa que todo está funcionando correctamente.

---

## 📋 Paso 3: Instalar Visual Studio Code

Visual Studio Code (VS Code) será tu editor de código principal, y tiene una integración excelente con Docker.

### Descargar e instalar VS Code:

Ve a https://code.visualstudio.com/ y descarga la versión para Windows.

Ejecuta el instalador y durante la instalación, asegúrate de marcar estas opciones importantes:
- "Add to PATH" (Agregar al PATH) - esto te permitirá abrir VS Code desde la línea de comandos
- "Register Code as an editor for supported file types" (Registrar Code como editor para tipos de archivo compatibles)
- "Add 'Open with Code' action to Windows Explorer file context menu" (Agregar acción 'Abrir con Code' al menú contextual del explorador)

### Primera configuración:

Cuando abras VS Code por primera vez, te sugerirá instalar extensiones según el tipo de archivos que detecte. Por ahora, no instales nada adicional hasta completar esta guía.

---

## 📋 Paso 4: Instalar la extensión Dev Containers

Esta extensión es la que hace toda la magia de conectar VS Code con los contenedores Docker.

### Instalar la extensión:

En VS Code, haz clic en el ícono de extensiones en la barra lateral izquierda (parece cuatro cuadrados con uno separado).

En el cuadro de búsqueda, escribe: `Dev Containers`

Busca la extensión oficial de Microsoft que se llama "Dev Containers" (el autor debe aparecer como "Microsoft").

Haz clic en "Install" (Instalar).

### Verificar la instalación:

Después de instalar la extensión, deberías ver un nuevo ícono en la esquina inferior izquierda de VS Code que parece dos flechas enfrentadas `><`. Este es el indicador de conexión remota.

---

## 📋 Paso 5: Configurar tu primer proyecto con DevContainers

Ahora viene la parte emocionante: configurar un proyecto para que use contenedores de desarrollo.

### Crear o abrir un proyecto:

Si ya tienes un proyecto, ábrelo en VS Code (File → Open Folder).

Si estás empezando desde cero, crea una carpeta nueva para tu proyecto y ábrela en VS Code.

### Crear la configuración del contenedor:

VS Code puede generar automáticamente la configuración del contenedor. Sigue estos pasos:

1. Presiona `Ctrl + Shift + P` para abrir la paleta de comandos
2. Escribe: `Dev Containers: Add Dev Container Configuration Files`
3. Selecciona esta opción de la lista

Se abrirá un menú con plantillas predefinidas. Algunas opciones populares son:
- **Python**: Si vas a desarrollar en Python
- **Node.js**: Para proyectos de JavaScript/TypeScript
- **PHP**: Para desarrollo web con PHP
- **Universal**: Una configuración general que incluye varias herramientas

Selecciona la plantilla que mejor se adapte a tu proyecto.

### Abrir el proyecto en el contenedor:

Después de crear la configuración, VS Code te preguntará si quieres reabrir el proyecto en el contenedor. Haz clic en "Reopen in Container" (Reabrir en contenedor).

La primera vez tardará varios minutos porque Docker necesita descargar la imagen base y instalar todas las herramientas. Puedes ver el progreso en la parte inferior de VS Code.

### ¡Listo para desarrollar!

Una vez que el contenedor esté listo, notarás algunos cambios:
- En la esquina inferior izquierda aparecerá el nombre de tu contenedor
- La terminal integrada de VS Code ahora está conectada al contenedor Linux
- Todas las herramientas de desarrollo están instaladas y listas para usar

---

## 🎯 ¿Cómo funciona todo junto?

Permíteme explicarte qué está pasando detrás de escenas para que entiendas completamente el sistema:

**Tu computadora física** ejecuta Windows y tiene Docker Desktop instalado. Docker Desktop usa WSL 2 para crear un ambiente Linux ligero donde pueden ejecutarse los contenedores.

**El contenedor de desarrollo** es como una computadora virtual completamente configurada con todas las herramientas que tu proyecto necesita. Esta "computadora virtual" ejecuta Linux y tiene instalado exactamente el mismo software que tendrán todos los miembros de tu equipo.

**Visual Studio Code** se conecta a este contenedor de manera inteligente. Cuando abres archivos, realmente los estás editando dentro del contenedor. Cuando ejecutas comandos en la terminal, se ejecutan dentro del contenedor. Pero toda la interfaz gráfica sigue ejecutándose en tu Windows.

**Los archivos de tu proyecto** se sincronizan automáticamente entre tu computadora Windows y el contenedor Linux, por lo que no pierdes nada si el contenedor se detiene o se reinicia.

---

## 🔧 Comandos útiles que deberías conocer

Una vez que tengas todo configurado, estos comandos te serán útiles:

**Para ver qué contenedores están ejecutándose:**
```powershell
docker ps
```

**Para detener todos los contenedores:**
```powershell
docker stop $(docker ps -q)
```

**Para ver cuánto espacio están usando los contenedores:**
```powershell
docker system df
```

**Para limpiar contenedores, imágenes y datos no utilizados:**
```powershell
docker system prune
```

---

## ❓ Preguntas frecuentes

**¿Necesito conocer Docker para usar DevContainers?**
No necesitas ser un experto en Docker, pero entender los conceptos básicos que expliqué en esta guía te ayudará mucho. Los DevContainers están diseñados para que los desarrolladores puedan enfocarse en programar sin preocuparse por la configuración del ambiente.

**¿Qué pasa si mi computadora se reinicia?**
Docker Desktop debería iniciarse automáticamente, pero es posible que necesites reabrir tu proyecto en VS Code y seleccionar "Reopen in Container" nuevamente.

**¿Los archivos se guardan en mi computadora o en el contenedor?**
Los archivos se guardan en tu computadora Windows, pero se sincronizan automáticamente con el contenedor. Esto significa que no los perderás si algo pasa con el contenedor.

**¿Puedo usar GitHub o Git normalmente?**
Sí, Git funciona normalmente dentro del contenedor. De hecho, muchas veces funciona mejor porque el contenedor ya tiene Git configurado correctamente.

**¿Qué hago si algo no funciona?**
Primero, intenta reiniciar Docker Desktop y VS Code. Si el problema persiste, puedes "reconstruir" el contenedor abriendo la paleta de comandos (`Ctrl + Shift + P`) y ejecutando "Dev Containers: Rebuild Container".

**¿Esto consume muchos recursos de mi computadora?**
Los contenedores son más eficientes que las máquinas virtuales tradicionales, pero sí consumen memoria RAM adicional. Para desarrollo típico, necesitarás al menos 8GB de RAM, siendo 16GB lo recomendado.

**¿Puedo trabajar sin conexión a internet?**
Una vez que el contenedor esté configurado y las imágenes descargadas, puedes trabajar sin conexión. Solo necesitas internet para la configuración inicial y para descargar nuevas herramientas o dependencias.

---

## 🎉 ¡Felicidades!

Has configurado exitosamente un entorno de desarrollo moderno y profesional. Ahora tú y tu equipo pueden trabajar con la confianza de que todos tienen exactamente el mismo ambiente de desarrollo, sin importar qué computadora esté usando cada uno.

Esta configuración te permitirá enfocarte en lo que realmente importa: crear software increíble, sin perder tiempo en problemas de configuración o en el famoso "en mi computadora sí funciona".

El siguiente paso es compartir la configuración de tu contenedor (los archivos `.devcontainer`) con tu equipo a través de tu repositorio de código. Cuando ellos clonen el proyecto y lo abran en VS Code, automáticamente tendrán acceso al mismo ambiente de desarrollo que tú.