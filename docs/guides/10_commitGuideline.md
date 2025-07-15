# Guía de Tipos de Commits y Formato Estándar

Un esquema consistente para tus mensajes de commit facilita la colaboración y el mantenimiento de tus proyectos. Usa esta guía para mantener un historial limpio y comprensible.

---

## Tipos de Commits

Al inicio de cada mensaje, utiliza estas etiquetas para indicar la naturaleza de los cambios:

- **feat:** Adición de una nueva funcionalidad.
- **fix:** Corrección de errores o bugs.
- **docs:** Cambios relacionados con la documentación (README, comentarios, etc.).
- **style:** Ajustes que no afectan el comportamiento del código (formato, espacios, etc.).
- **refactor:** Modificaciones internas sin cambiar la funcionalidad.
- **test:** Incorporación o actualización de pruebas.
- **chore:** Tareas menores o mantenimiento (actualizaciones de dependencias, scripts, etc.).
- **perf:** Mejoras en el rendimiento.
- **ci:** Ajustes en la integración continua (configuraciones o scripts).
- **build:** Cambios que afectan el sistema de construcción o dependencias.

---

## Formato Estándar de un Mensaje de Commit

### Estructura:
```yaml
<Tipo>: <Descripción corta y clara>

Descripción extendida (opcional):
- Explica **qué** se cambió y **por qué**.
- Incluye cualquier detalle adicional relevante.

Referencias (opcional):
- Vincula issues, tickets o pull requests relacionados.
Ejemplos:
```

### Commit breve:

```yaml
feat: Añadir función para registro de usuarios
```

#### Commit con descripción extendida:
```yaml
fix: Arreglar error en el proceso de autenticación

- Se corrigió el error que impedía el cierre de sesión.
- Mejora en la gestión de tokens expirados.
- Relacionado con el issue #123.
```

#### Commit de documentación:

```yaml
docs: Actualizar el README con instrucciones de despliegue
Consejos para un Buen Mensaje de Commit
Escribe en presente (e.g., "Añadir función", "Corregir error").

Usa un lenguaje claro y directo.

Mantén la línea principal con un máximo de 50 caracteres.

Agrega detalles adicionales en el cuerpo si es necesario.
```

#### Plantilla Rápida:

```yaml
<Tipo>: <Descripción corta>

Descripción extendida (si es necesario):
- Más detalles del cambio.
- Razón del cambio.
- Issues relacionados: #<número_de_issue> (opcional).
Adopta este formato para tus proyectos y considera agregar este archivo a tu repositorio como commit-guidelines.md. ¡Te ayudará a mantener un historial organizado y colaborativo! 🚀
```

Espero que esta versión mejorada sea justo lo que necesitas. ¿Hay algo más en l