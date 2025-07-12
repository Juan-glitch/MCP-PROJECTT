# Guía Rápida: ¿Cómo interactuar con Codex?

Codex es tu asistente de IA para automatizar tareas de programación. Imagina a Codex como un compañero que puede leer, modificar y probar tu código por ti. Para que el proceso sea fluido, sigue estas pautas:

## 1. Trabaja siempre en ramas

Cuando necesites un cambio, indícale a Codex en qué rama deseas que trabaje. Él creará una rama local, aplicará los cambios y abrirá un Pull Request (PR) para que lo revises. Así mantienes el control sobre el repositorio.

## 2. Explica con claridad

Describe tu solicitud con el mayor detalle posible: archivos, funciones o comportamientos específicos. Cuanta más información proporciones, más precisos serán los cambios que Codex realice.

## 3. La carpeta `.codex`

Aquí puedes agregar archivos que ayuden a Codex a entender mejor tu proyecto. Por ejemplo, `memory.txt` sirve para guardar notas persistentes que quieras que Codex tenga en cuenta en futuras sesiones.

## 4. Revisión y pruebas

Codex intentará ejecutar las pruebas definidas en `tests/`. Si alguna falla, te avisará en el PR. Revisa siempre el resultado antes de fusionar.

---

**En resumen:** comunica claramente tus cambios, usa ramas, revisa el PR y aprovecha la carpeta `.codex` para compartir contexto adicional.



# 📚 .codex — Centro de Memoria y Preferencias Personales

Este directorio sirve como espacio estructurado para guardar información persistente que mejora la interacción con Codex y el entorno de trabajo.

## ¿Para qué sirve?

- Guardar preferencias personales de comunicación y estilo.
- Anotar ideas, aprendizajes y decisiones de diseño.
- Evolucionar la colaboración con sistemas como Codex o asistentes inteligentes.
- Permitir a herramientas automatizadas acceder a contexto relevante sin invadir la lógica del proyecto.

## Estructura propuesta

- `preferences.yml` — Preferencias personales y técnicas para adaptar respuestas.
- `notes.txt` — Bitácora libre de ideas, pruebas, decisiones y aprendizajes.
- `history.md` — Registro de cambios importantes o hitos personales/técnicos.
- `codex.meta.json` — (opcional) Estructura legible por máquina si se desea integrar procesamiento automático.

