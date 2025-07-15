# arxiv-fastmcp-server

Este proyecto implementa un servidor FastMCP que permite buscar y extraer información de artículos de arXiv. 

## Estructura del Proyecto

```
arxiv-fastmcp-server
├── src
│   ├── server.py          # Punto de entrada de la aplicación
│   └── types
│       └── index.py      # Definiciones de tipos e interfaces (actualmente vacío)
├── requirements.txt       # Dependencias necesarias para el proyecto
└── README.md              # Documentación del proyecto
```

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener `pip` instalado y ejecuta el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt
```

## Uso

Para ejecutar el servidor, utiliza el siguiente comando:

```
python src/server.py
```

Una vez que el servidor esté en funcionamiento, podrás utilizar las herramientas `search_papers` para buscar artículos en arXiv y `extract_info` para obtener información sobre artículos específicos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.