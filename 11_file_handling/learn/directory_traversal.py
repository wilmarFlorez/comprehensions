"""
Traversal de directorios - Procesar múltiples archivos.
Contexto: Un agente RAG necesita indexar todos los documentos en una carpeta.
"""

import tempfile
from pathlib import Path
from typing import Generator, list

# ============================================================================
# 1. LISTAR ARCHIVOS EN UN DIRECTORIO
# ============================================================================

def list_files_in_directory(directory: str) -> list[str]:
    """Lista todos los archivos en un directorio (no recursivo)."""
    return [f.name for f in Path(directory).glob('*') if f.is_file()]


def list_files_recursive(directory: str) -> list[str]:
    """Lista todos los archivos recursivamente en subdirectorios."""
    dir_path = Path(directory)
    return [str(f.relative_to(dir_path)) for f in dir_path.rglob('*') if f.is_file()]


# ============================================================================
# 2. FILTRAR POR EXTENSIÓN
# ============================================================================

def find_files_by_extension(directory: str, extension: str) -> list[str]:
    """Encuentra todos los archivos con una extensión específica."""
    dir_path = Path(directory)
    pattern = f'**/*.{extension}' if not extension.startswith('.') else f'**/*{extension}'
    return [str(f.relative_to(dir_path)) for f in dir_path.glob(pattern)]


def find_markdown_files(directory: str) -> list[str]:
    """Caso específico: encontrar archivos .md (común en documentación de agentes)."""
    return find_files_by_extension(directory, 'md')


# ============================================================================
# 3. PROCESAR TODOS LOS ARCHIVOS (GENERADOR - Memory efficient)
# ============================================================================

def process_all_files(directory: str, extension: str = None) -> Generator[tuple[str, str], None, None]:
    """
    Generador que carga archivos uno por uno.
    Eficiente para procesar muchos archivos sin cargar todos en memoria.
    Ideal para indexación de documentos en agentes RAG.
    """
    dir_path = Path(directory)
    
    if extension:
        pattern = f'**/*.{extension}'
        files = dir_path.glob(pattern)
    else:
        files = dir_path.rglob('*')
    
    for file_path in files:
        if file_path.is_file():
            try:
                content = file_path.read_text(encoding='utf-8')
                yield (str(file_path.relative_to(dir_path)), content)
            except UnicodeDecodeError:
                # Saltar archivos que no sean texto
                continue


# ============================================================================
# 4. ESTADÍSTICAS DE DOCUMENTOS
# ============================================================================

def document_statistics(directory: str, extension: str = None) -> dict:
    """
    Calcula estadísticas sobre los documentos en un directorio.
    Útil para RAG: contar tokens, tamaño total, etc.
    """
    stats = {
        'total_files': 0,
        'total_size_bytes': 0,
        'files_by_extension': {},
        'files': [],
    }
    
    for filepath, content in process_all_files(directory, extension):
        stats['total_files'] += 1
        file_size = len(content.encode('utf-8'))
        stats['total_size_bytes'] += file_size
        
        file_ext = Path(filepath).suffix or 'no_extension'
        stats['files_by_extension'][file_ext] = stats['files_by_extension'].get(file_ext, 0) + 1
        
        stats['files'].append({
            'path': filepath,
            'size_bytes': file_size,
            'lines': len(content.split('\n')),
        })
    
    return stats


# ============================================================================
# 5. INDEXAR DOCUMENTOS (Simulando RAG)
# ============================================================================

def index_documents(directory: str, extension: str = 'txt') -> dict:
    """
    Crea un índice simple de documentos.
    Simula lo que hace un RAG (Retrieval-Augmented Generation):
    1. Cargar documentos
    2. Dividir en chunks
    3. Indexar para búsqueda rápida
    """
    index = {}
    
    for filepath, content in process_all_files(directory, extension):
        # Simular división en chunks (líneas)
        chunks = content.split('\n')
        index[filepath] = {
            'raw_content': content,
            'chunks': [c for c in chunks if c.strip()],
            'chunk_count': len([c for c in chunks if c.strip()]),
        }
    
    return index


# ============================================================================
# 6. BUSCAR EN MÚLTIPLES DOCUMENTOS
# ============================================================================

def search_in_documents(directory: str, search_term: str, extension: str = 'txt') -> list[dict]:
    """Busca un término en todos los documentos de un directorio."""
    results = []
    
    for filepath, content in process_all_files(directory, extension):
        if search_term.lower() in content.lower():
            # Encontrar líneas que contienen el término
            lines = content.split('\n')
            matching_lines = [
                (i + 1, line) for i, line in enumerate(lines)
                if search_term.lower() in line.lower()
            ]
            
            results.append({
                'file': filepath,
                'matches': len(matching_lines),
                'lines': matching_lines[:3],  # Primeras 3 coincidencias
            })
    
    return results


# ============================================================================
# EJEMPLO PRÁCTICO
# ============================================================================

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Crear estructura de ejemplo (simulando carpeta de documentos)
        docs_dir = tmpdir / "documents"
        docs_dir.mkdir()
        
        # Crear algunos archivos de ejemplo
        (docs_dir / "guia_agentes.txt").write_text(
            "Los agentes autónomos pueden realizar tareas complejas.\n"
            "Usan herramientas externas para expandir capacidades.\n"
            "Requieren buena estructuración de prompts."
        )
        
        (docs_dir / "langchain_intro.txt").write_text(
            "LangChain es un framework para agentes de IA.\n"
            "Facilita la integración con modelos de lenguaje.\n"
            "Proporciona abstracciones para chains y agentes."
        )
        
        (docs_dir / "rag_explicado.txt").write_text(
            "RAG significa Retrieval-Augmented Generation.\n"
            "Combina recuperación de documentos con generación.\n"
            "Mejora la precisión de agentes de IA."
        )
        
        (docs_dir / "config.json").write_text('{"model": "gpt-4"}')
        
        # 1. Listar archivos
        print("1️⃣ LISTAR ARCHIVOS")
        print("=" * 50)
        files = list_files_in_directory(str(docs_dir))
        for f in files:
            print(f"  - {f}")
        
        # 2. Estadísticas
        print("\n2️⃣ ESTADÍSTICAS DE DOCUMENTOS")
        print("=" * 50)
        stats = document_statistics(str(docs_dir), extension='txt')
        print(f"  Total archivos: {stats['total_files']}")
        print(f"  Tamaño total: {stats['total_size_bytes']} bytes")
        print(f"  Archivos por extensión: {stats['files_by_extension']}")
        
        # 3. Procesamiento eficiente con generador
        print("\n3️⃣ PROCESAR DOCUMENTOS (con generador)")
        print("=" * 50)
        for filepath, content in process_all_files(str(docs_dir), extension='txt'):
            word_count = len(content.split())
            print(f"  {filepath}: {word_count} palabras")
        
        # 4. Indexación tipo RAG
        print("\n4️⃣ INDEXACIÓN DE DOCUMENTOS (RAG)")
        print("=" * 50)
        index = index_documents(str(docs_dir), extension='txt')
        for filepath, info in index.items():
            print(f"  {filepath}: {info['chunk_count']} chunks")
        
        # 5. Búsqueda en múltiples documentos
        print("\n5️⃣ BÚSQUEDA EN MÚLTIPLES DOCUMENTOS")
        print("=" * 50)
        search_results = search_in_documents(str(docs_dir), "agentes", extension='txt')
        print(f"  Encontrado en {len(search_results)} archivo(s):")
        for result in search_results:
            print(f"    - {result['file']}: {result['matches']} coincidencia(s)")
            for line_num, line in result['lines']:
                print(f"      L{line_num}: {line[:50]}...")
