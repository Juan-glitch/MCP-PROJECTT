#!/usr/bin/env python3
"""Advanced project tree generator.

This module was originally written in Spanish and provides a very feature rich
way to explore a directory. It supports coloured output, markdown generation and
much more. The rest of the file remains mostly unchanged for now.

Below you will find the original documentation in Spanish.

Generador de Árbol de Proyectos Avanzado v2.0

Este script genera un árbol de directorios mejorado con múltiples formatos de salida,
información de debug detallada, y opciones avanzadas de personalización.

Características:
- Múltiples formatos de salida (ASCII, Markdown, Mermaid)
- Información de debug detallada
- Filtrado avanzado de archivos y directorios
- Estadísticas del proyecto
- Soporte para archivos ocultos
- Límite de profundidad configurable
- Información de tamaño de archivos
- Salida colorizada en terminal

Uso:
    python project_tree.py [opciones]

Ejemplos:
    # Generar árbol básico
    python project_tree.py
    
    # Generar con formato markdown
    python project_tree.py --format markdown --output README.md
    
    # Con debug y estadísticas
    python project_tree.py --debug --stats --max-depth 5
    
    # Ignorar archivos específicos
    python project_tree.py --ignore-files "*.log,*.tmp,*.pyc" --ignore-dirs "node_modules,venv"
"""

import os
import sys
import argparse
import fnmatch
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import json


class Colors:
    """Códigos de colores ANSI para output colorizado"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ProjectTreeGenerator:
    """Generador de árbol de proyectos con funcionalidades avanzadas"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.stats = {
            'total_files': 0,
            'total_directories': 0,
            'ignored_items': [],
            'processed_items': [],
            'start_time': time.time(),
            'max_depth_reached': False,
            'total_size': 0
        }
        self.icons = {
            'directory': '📁',
            'file': '📄',
            'hidden': '🔒',
            'executable': '⚡',
            'image': '🖼️',
            'document': '📋',
            'code': '💻',
            'config': '⚙️',
            'data': '📊'
        }
        
    def get_file_icon(self, filename: str, is_dir: bool = False) -> str:
        """Obtiene el icono apropiado para un archivo basado en su extensión"""
        if is_dir:
            return self.icons['directory']
        
        if filename.startswith('.'):
            return self.icons['hidden']
        
        # Extensiones comunes
        ext = Path(filename).suffix.lower()
        
        # Archivos ejecutables
        if ext in ['.exe', '.bat', '.sh', '.cmd']:
            return self.icons['executable']
        
        # Imágenes
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico']:
            return self.icons['image']
        
        # Documentos
        if ext in ['.pdf', '.doc', '.docx', '.txt', '.md', '.rst']:
            return self.icons['document']
        
        # Código
        if ext in ['.py', '.js', '.html', '.css', '.cpp', '.java', '.cs', '.php']:
            return self.icons['code']
        
        # Configuración
        if ext in ['.json', '.yaml', '.yml', '.xml', '.ini', '.cfg', '.toml']:
            return self.icons['config']
        
        # Datos
        if ext in ['.csv', '.xlsx', '.sql', '.db', '.sqlite']:
            return self.icons['data']
        
        return self.icons['file']
    
    def format_size(self, size: int) -> str:
        """Formatea el tamaño de archivo en formato legible"""
        units = ['B', 'KB', 'MB', 'GB', 'TB']
        unit_index = 0
        
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1
        
        return f"{size:.1f} {units[unit_index]}"
    
    def should_ignore(self, name: str, path: str, is_dir: bool) -> bool:
        """Determina si un archivo o directorio debe ser ignorado"""
        # Archivos ocultos
        if name.startswith('.') and not self.config['show_hidden']:
            self.stats['ignored_items'].append(f"🔒 {name} (archivo oculto)")
            return True
        
        # Directorios a ignorar
        if is_dir:
            for pattern in self.config['ignore_dirs']:
                if fnmatch.fnmatch(name, pattern):
                    self.stats['ignored_items'].append(f"📁 {name} (directorio ignorado)")
                    return True
        
        # Archivos a ignorar
        else:
            for pattern in self.config['ignore_files']:
                if fnmatch.fnmatch(name, pattern):
                    self.stats['ignored_items'].append(f"📄 {name} (archivo ignorado)")
                    return True
        
        return False
    
    def get_file_info(self, path: str) -> Dict:
        """Obtiene información detallada de un archivo o directorio"""
        try:
            stat = os.stat(path)
            is_dir = os.path.isdir(path)
            
            return {
                'name': os.path.basename(path),
                'path': path,
                'is_dir': is_dir,
                'size': stat.st_size if not is_dir else 0,
                'modified': datetime.fromtimestamp(stat.st_mtime),
                'icon': self.get_file_icon(os.path.basename(path), is_dir)
            }
        except (OSError, PermissionError) as e:
            if self.config['debug']:
                print(f"{Colors.WARNING}Warning: No se pudo acceder a {path}: {e}{Colors.ENDC}")
            return None
    
    def scan_directory(self, path: str, current_depth: int = 0) -> Optional[Dict]:
        """Escanea un directorio y construye su estructura"""
        if self.config['max_depth'] > 0 and current_depth >= self.config['max_depth']:
            self.stats['max_depth_reached'] = True
            return None
        
        try:
            items = sorted(os.listdir(path))
        except (OSError, PermissionError) as e:
            if self.config['debug']:
                print(f"{Colors.WARNING}Warning: No se pudo listar {path}: {e}{Colors.ENDC}")
            return None
        
        file_info = self.get_file_info(path)
        if not file_info:
            return None
        
        structure = {
            'name': file_info['name'],
            'path': path,
            'type': 'directory',
            'size': 0,
            'icon': file_info['icon'],
            'children': []
        }
        
        self.stats['total_directories'] += 1
        self.stats['processed_items'].append(file_info['name'])
        
        # Procesar elementos del directorio
        for item in items:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            
            if self.should_ignore(item, item_path, is_dir):
                continue
            
            if is_dir:
                child_structure = self.scan_directory(item_path, current_depth + 1)
                if child_structure:
                    structure['children'].append(child_structure)
                    structure['size'] += child_structure['size']
            else:
                file_info = self.get_file_info(item_path)
                if file_info:
                    child_structure = {
                        'name': file_info['name'],
                        'path': item_path,
                        'type': 'file',
                        'size': file_info['size'],
                        'icon': file_info['icon']
                    }
                    structure['children'].append(child_structure)
                    structure['size'] += file_info['size']
                    self.stats['total_files'] += 1
                    self.stats['total_size'] += file_info['size']
                    self.stats['processed_items'].append(file_info['name'])
        
        return structure
    
    def generate_ascii_tree(self, structure: Dict, prefix: str = '', is_last: bool = True) -> str:
        """Genera el árbol en formato ASCII"""
        if not structure:
            return ""
        
        # Construir línea actual
        connector = '└── ' if is_last else '├── '
        icon = structure['icon']
        name = structure['name']
        
        # Información adicional
        size_info = ""
        if self.config['show_sizes'] and structure['type'] == 'file':
            size_info = f" ({self.format_size(structure['size'])})"
        
        line = f"{prefix}{connector}{icon} {name}{size_info}\n"
        
        # Procesar hijos
        result = line
        if structure.get('children'):
            new_prefix = prefix + ('    ' if is_last else '│   ')
            children = structure['children']
            
            for i, child in enumerate(children):
                child_is_last = i == len(children) - 1
                result += self.generate_ascii_tree(child, new_prefix, child_is_last)
        
        return result
    
    def generate_markdown(self, structure: Dict, project_name: str = "") -> str:
        """Genera el árbol en formato Markdown"""
        if not project_name:
            project_name = structure['name'] if structure else "Proyecto"
        
        processing_time = time.time() - self.stats['start_time']
        
        markdown = f"""# 📁 {project_name}

**Ruta:** `{structure['path'] if structure else 'N/A'}`
**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🌳 Estructura del Proyecto

```
{self.generate_ascii_tree(structure)}```

## 📊 Estadísticas del Proyecto

- **Total de archivos:** {self.stats['total_files']}
- **Total de directorios:** {self.stats['total_directories']}
- **Tamaño total:** {self.format_size(self.stats['total_size'])}
- **Elementos procesados:** {len(self.stats['processed_items'])}
- **Elementos ignorados:** {len(self.stats['ignored_items'])}
- **Tiempo de procesamiento:** {processing_time:.2f}s
- **Profundidad máxima alcanzada:** {'Sí' if self.stats['max_depth_reached'] else 'No'}

"""
        
        if self.config['debug'] and self.stats['ignored_items']:
            markdown += """## 🚫 Elementos Ignorados

"""
            for item in self.stats['ignored_items']:
                markdown += f"- {item}\n"
            markdown += "\n"
        
        if self.config['show_config']:
            markdown += f"""## ⚙️ Configuración Utilizada

- **Profundidad máxima:** {self.config['max_depth'] if self.config['max_depth'] > 0 else 'Sin límite'}
- **Mostrar archivos ocultos:** {'Sí' if self.config['show_hidden'] else 'No'}
- **Mostrar tamaños:** {'Sí' if self.config['show_sizes'] else 'No'}
- **Directorios ignorados:** {', '.join(self.config['ignore_dirs'])}
- **Archivos ignorados:** {', '.join(self.config['ignore_files'])}

"""
        
        markdown += f"""---
*Generado automáticamente con ProjectTreeGenerator v2.0*
"""
        
        return markdown
    
    def generate_mermaid(self, structure: Dict) -> str:
        """Genera el árbol en formato Mermaid"""
        if not structure:
            return ""
        
        mermaid = "graph TD\n"
        node_id = 0
        
        def add_node(node: Dict, parent_id: Optional[int] = None) -> int:
            nonlocal node_id
            current_id = node_id
            node_id += 1
            
            # Preparar etiqueta del nodo
            icon = node['icon']
            name = node['name'].replace('"', '\\"')  # Escapar comillas
            size_info = ""
            
            if self.config['show_sizes'] and node['type'] == 'file':
                size_info = f"<br/>{self.format_size(node['size'])}"
            
            label = f'{icon} {name}{size_info}'
            
            # Agregar nodo
            mermaid_line = f'    {current_id}["{label}"]\n'
            mermaid += mermaid_line
            
            # Conectar con padre
            if parent_id is not None:
                mermaid += f'    {parent_id} --> {current_id}\n'
            
            # Procesar hijos
            if node.get('children'):
                for child in node['children']:
                    add_node(child, current_id)
            
            return current_id
        
        add_node(structure)
        return mermaid
    
    def generate_json(self, structure: Dict) -> str:
        """Genera el árbol en formato JSON"""
        return json.dumps(structure, indent=2, ensure_ascii=False)
    
    def print_debug_info(self):
        """Imprime información de debug"""
        if not self.config['debug']:
            return
        
        processing_time = time.time() - self.stats['start_time']
        
        print(f"\n{Colors.HEADER}{'='*50}")
        print(f"  INFORMACIÓN DE DEBUG")
        print(f"{'='*50}{Colors.ENDC}")
        
        print(f"{Colors.OKBLUE}📊 Estadísticas:{Colors.ENDC}")
        print(f"  • Archivos procesados: {self.stats['total_files']}")
        print(f"  • Directorios procesados: {self.stats['total_directories']}")
        print(f"  • Tamaño total: {self.format_size(self.stats['total_size'])}")
        print(f"  • Elementos ignorados: {len(self.stats['ignored_items'])}")
        print(f"  • Tiempo de procesamiento: {processing_time:.2f}s")
        print(f"  • Profundidad máxima alcanzada: {'Sí' if self.stats['max_depth_reached'] else 'No'}")
        
        if self.stats['ignored_items']:
            print(f"\n{Colors.WARNING}🚫 Elementos ignorados:{Colors.ENDC}")
            for item in self.stats['ignored_items'][:10]:  # Mostrar solo los primeros 10
                print(f"  • {item}")
            if len(self.stats['ignored_items']) > 10:
                print(f"  ... y {len(self.stats['ignored_items']) - 10} más")
        
        print(f"\n{Colors.OKCYAN}⚙️ Configuración:{Colors.ENDC}")
        print(f"  • Formato: {self.config['format']}")
        print(f"  • Profundidad máxima: {self.config['max_depth'] if self.config['max_depth'] > 0 else 'Sin límite'}")
        print(f"  • Mostrar archivos ocultos: {'Sí' if self.config['show_hidden'] else 'No'}")
        print(f"  • Mostrar tamaños: {'Sí' if self.config['show_sizes'] else 'No'}")
        
        print(f"{Colors.HEADER}{'='*50}{Colors.ENDC}")
    
    def generate(self, root_path: str) -> str:
        """Genera el árbol del proyecto"""
        if not os.path.exists(root_path):
            raise FileNotFoundError(f"La ruta {root_path} no existe")
        
        if not os.path.isdir(root_path):
            raise NotADirectoryError(f"La ruta {root_path} no es un directorio")
        
        if self.config['debug']:
            print(f"{Colors.OKGREEN}🌳 Generando árbol del proyecto...{Colors.ENDC}")
            print(f"📁 Ruta: {root_path}")
            print(f"📝 Formato: {self.config['format']}")
        
        # Escanear estructura
        structure = self.scan_directory(root_path)
        
        if not structure:
            raise RuntimeError("No se pudo generar la estructura del proyecto")
        
        # Generar salida según el formato
        if self.config['format'] == 'ascii':
            result = self.generate_ascii_tree(structure)
        elif self.config['format'] == 'markdown':
            result = self.generate_markdown(structure, self.config.get('project_name', ''))
        elif self.config['format'] == 'mermaid':
            result = self.generate_mermaid(structure)
        elif self.config['format'] == 'json':
            result = self.generate_json(structure)
        else:
            raise ValueError(f"Formato no soportado: {self.config['format']}")
        
        # Mostrar información de debug
        if self.config['debug']:
            self.print_debug_info()
        
        return result


def parse_arguments():
    """Parsea los argumentos de línea de comandos"""
    parser = argparse.ArgumentParser(
        description='Generador de Árbol de Proyectos Avanzado v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s                                    # Árbol básico en ASCII
  %(prog)s --format markdown --output README.md  # Generar markdown
  %(prog)s --debug --stats --max-depth 5      # Con debug y límite de profundidad
  %(prog)s --ignore-files "*.log,*.tmp"       # Ignorar archivos específicos
  %(prog)s --project-name "Mi Proyecto"       # Nombre personalizado
        """
    )
    
    # Argumentos básicos
    parser.add_argument('path', nargs='?', default='.', 
                       help='Ruta del proyecto (por defecto: directorio actual)')
    parser.add_argument('--format', choices=['ascii', 'markdown', 'mermaid', 'json'], 
                       default='ascii', help='Formato de salida')
    parser.add_argument('--output', '-o', help='Archivo de salida')
    
    # Filtros
    parser.add_argument('--ignore-dirs', default='.git,__pycache__,venv,.pytest_cache,node_modules,dist,build',
                       help='Directorios a ignorar (separados por comas)')
    parser.add_argument('--ignore-files', default='*.pyc,*.tmp,*.log,*.DS_Store,Thumbs.db',
                       help='Archivos a ignorar (separados por comas)')
    parser.add_argument('--max-depth', type=int, default=0,
                       help='Profundidad máxima (0 = sin límite)')
    
    # Opciones de visualización
    parser.add_argument('--show-hidden', action='store_true',
                       help='Mostrar archivos ocultos')
    parser.add_argument('--show-sizes', action='store_true', default=True,
                       help='Mostrar tamaños de archivos')
    parser.add_argument('--no-sizes', dest='show_sizes', action='store_false',
                       help='No mostrar tamaños de archivos')
    
    # Opciones de debug y personalización
    parser.add_argument('--debug', action='store_true',
                       help='Mostrar información de debug')
    parser.add_argument('--stats', action='store_true',
                       help='Mostrar estadísticas del proyecto')
    parser.add_argument('--show-config', action='store_true',
                       help='Incluir configuración en la salida')
    parser.add_argument('--project-name',
                       help='Nombre del proyecto (para formato markdown)')
    
    return parser.parse_args()


def main():
    """Función principal"""
    try:
        args = parse_arguments()
        
        # Configurar generador
        config = {
            'format': args.format,
            'ignore_dirs': [d.strip() for d in args.ignore_dirs.split(',')],
            'ignore_files': [f.strip() for f in args.ignore_files.split(',')],
            'max_depth': args.max_depth,
            'show_hidden': args.show_hidden,
            'show_sizes': args.show_sizes,
            'debug': args.debug,
            'stats': args.stats,
            'show_config': args.show_config,
            'project_name': args.project_name
        }
        
        # Crear generador
        generator = ProjectTreeGenerator(config)
        
        # Generar árbol
        result = generator.generate(args.path)
        
        # Guardar o mostrar resultado
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"{Colors.OKGREEN}✅ Árbol generado exitosamente en: {args.output}{Colors.ENDC}")
        else:
            print(result)
        
        # Mostrar estadísticas si se solicitó
        if args.stats and not args.debug:
            processing_time = time.time() - generator.stats['start_time']
            print(f"\n{Colors.OKCYAN}📊 Estadísticas:{Colors.ENDC}")
            print(f"  • Archivos: {generator.stats['total_files']}")
            print(f"  • Directorios: {generator.stats['total_directories']}")
            print(f"  • Tamaño total: {generator.format_size(generator.stats['total_size'])}")
            print(f"  • Tiempo: {processing_time:.2f}s")
    
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}❌ Operación cancelada por el usuario{Colors.ENDC}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.FAIL}❌ Error: {e}{Colors.ENDC}")
        sys.exit(1)


if __name__ == '__main__':
    main()
