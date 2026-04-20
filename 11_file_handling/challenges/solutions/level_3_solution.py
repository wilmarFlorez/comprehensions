# ============================================================
#  SOLUCIÓN NIVEL 3 - ONE-LINERS
#  Referencia: Código conciso, sin variables intermedias
# ============================================================

import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    docs_dir = tmpdir / "docs"
    docs_dir.mkdir()
    (docs_dir / "report1.txt").write_text("Los agentes de IA\nsimplificar tareas")
    (docs_dir / "report2.txt").write_text("Automatización inteligente\nimprove productividad")
    (docs_dir / "report3.txt").write_text("Procesamiento de datos")
    
    
    def list_txt_files():
        """One-liner: listar archivos."""
        return [f.name for f in docs_dir.glob("*.txt")]
    
    
    def documents_to_dict():
        """One-liner: diccionario archivo->contenido."""
        return {f.name: f.read_text() for f in docs_dir.glob("*.txt")}
    
    
    def total_words():
        """One-liner: total de palabras en todos los archivos."""
        return sum(len(f.read_text().split()) for f in docs_dir.glob("*.txt"))
    
    
    def files_by_size():
        """One-liner: archivos ordenados por tamaño."""
        return sorted(
            [(f.name, len(f.read_text())) for f in docs_dir.glob("*.txt")],
            key=lambda x: x[1]
        )
    
    
    def search_results(search_term="de"):
        """One-liner: búsqueda global."""
        return [
            (f.name, line) for f in docs_dir.glob("*.txt")
            for line in f.read_text().split('\n')
            if search_term in line.lower()
        ]
    
    
    # Ejecutar
    print("NIVEL 3 - SOLUCIONES (One-liners)")
    print("=" * 50)
    print(f"✓ Lista de archivos: {list_txt_files()}")
    print(f"✓ Total palabras: {total_words()}")
    print(f"✓ Archivos por tamaño: {files_by_size()}")
    print(f"✓ Búsqueda 'de': {len(search_results())} coincidencias")
