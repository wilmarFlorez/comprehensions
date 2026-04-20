# ============================================================
#  SOLUCIÓN NIVEL 1 - FOR LOOPS
#  Referencia: Cómo resolver los desafíos con for-loops
# ============================================================

import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    docs_dir = tmpdir / "docs"
    docs_dir.mkdir()
    (docs_dir / "report1.txt").write_text("Los agentes de IA\nsimplificar tareas\ncomplexas")
    (docs_dir / "report2.txt").write_text("Automatización inteligente\nimprove productividad")
    (docs_dir / "report3.txt").write_text("Procesamiento de datos\nen tiempo real")
    
    
    def list_txt_files():
        """Listar archivos .txt con for-loop."""
        files = []
        for file_path in docs_dir.iterdir():
            if file_path.is_file() and file_path.suffix == ".txt":
                files.append(file_path.name)
        return files
    
    
    def count_total_words():
        """Contar palabras totales con for-loops anidados."""
        total = 0
        for file_path in docs_dir.iterdir():
            if file_path.is_file() and file_path.suffix == ".txt":
                content = file_path.read_text()
                words = content.split()
                total += len(words)
        return total
    
    
    def documents_to_dict():
        """Crear diccionario archivo->contenido."""
        doc_dict = {}
        for file_path in docs_dir.iterdir():
            if file_path.is_file() and file_path.suffix == ".txt":
                doc_dict[file_path.name] = file_path.read_text()
        return doc_dict
    
    
    def filter_long_documents(min_words=3):
        """Filtrar documentos con más de N palabras."""
        result = []
        for file_path in docs_dir.iterdir():
            if file_path.is_file() and file_path.suffix == ".txt":
                content = file_path.read_text()
                word_count = len(content.split())
                if word_count > min_words:
                    result.append(file_path.name)
        return result
    
    
    def search_in_documents(search_term="agentes"):
        """Buscar término en todos los documentos."""
        results = []
        for file_path in docs_dir.iterdir():
            if file_path.is_file() and file_path.suffix == ".txt":
                content = file_path.read_text()
                for line in content.split('\n'):
                    if search_term in line.lower():
                        results.append((file_path.name, line))
        return results
    
    
    # Ejecutar y verificar
    print("NIVEL 1 - SOLUCIONES")
    print("=" * 50)
    print(f"1. Archivos .txt: {list_txt_files()}")
    print(f"2. Total palabras: {count_total_words()}")
    print(f"3. Diccionario: {len(documents_to_dict())} documentos")
    print(f"4. Documentos largos: {filter_long_documents(3)}")
    print(f"5. Búsqueda 'agentes': {len(search_in_documents('agentes'))} resultados")
