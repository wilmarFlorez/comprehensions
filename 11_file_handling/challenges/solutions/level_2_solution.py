# ============================================================
#  SOLUCIÓN NIVEL 2 - COMPREHENSIONS
#  Referencia: Cómo resolver con comprehensions (conciso)
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
        """List comprehension para obtener archivos .txt."""
        return [f.name for f in docs_dir.glob("*.txt")]
    
    
    def documents_to_dict():
        """Dict comprehension para mapear archivo->contenido."""
        return {f.name: f.read_text() for f in docs_dir.glob("*.txt")}
    
    
    def filter_long_documents(min_words=3):
        """List comprehension con filtro."""
        return [
            f.name for f in docs_dir.glob("*.txt")
            if len(f.read_text().split()) > min_words
        ]
    
    
    def word_count_per_file():
        """Dict comprehension para contar palabras."""
        return {f.name: len(f.read_text().split()) for f in docs_dir.glob("*.txt")}
    
    
    def all_lines_with_files():
        """List comprehension anidado para obtener (archivo, línea)."""
        return [
            (f.name, line)
            for f in docs_dir.glob("*.txt")
            for line in f.read_text().split('\n')
        ]
    
    
    def search_with_comprehension(search_term="agentes"):
        """Búsqueda con comprehension anidado."""
        return [
            (f.name, line)
            for f in docs_dir.glob("*.txt")
            for line in f.read_text().split('\n')
            if search_term.lower() in line.lower()
        ]
    
    
    # Ejecutar y verificar
    print("NIVEL 2 - SOLUCIONES (Comprehensions)")
    print("=" * 50)
    print(f"✓ List comprehension: {len(list_txt_files())} archivos")
    print(f"✓ Dict comprehension: {len(documents_to_dict())} documentos")
    print(f"✓ Con filtro: {filter_long_documents(3)}")
    print(f"✓ Contar palabras: {word_count_per_file()}")
    print(f"✓ Líneas totales: {len(all_lines_with_files())}")
    print(f"✓ Búsqueda 'agentes': {len(search_with_comprehension('agentes'))} resultados")
