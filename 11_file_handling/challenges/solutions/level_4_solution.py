# ============================================================
#  SOLUCIÓN NIVEL 4 - SIN IMPORTACIONES (solo built-ins)
#  Referencia: Código portable sin Path, functools, etc.
# ============================================================

import tempfile  # Solo para setup
from pathlib import Path  # Solo para setup

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    docs_dir = tmpdir / "docs"
    docs_dir.mkdir()
    (docs_dir / "report1.txt").write_text("Los agentes\ninteligentes")
    (docs_dir / "report2.txt").write_text("Automatización")
    (docs_dir / "report3.txt").write_text("Datos procesados")
    
    docs_path = str(docs_dir)
    
    
    def list_txt_files():
        """Listar .txt usando os (built-in)."""
        import os
        return [
            f for f in os.listdir(docs_path)
            if f.endswith('.txt')
        ]
    
    
    def total_file_size():
        """Tamaño total de archivos usando os."""
        import os
        total = 0
        for f in os.listdir(docs_path):
            if f.endswith('.txt'):
                filepath = os.path.join(docs_path, f)
                total += os.path.getsize(filepath)
        return total
    
    
    def search_term_basic(term="agentes"):
        """Búsqueda usando solo built-ins."""
        import os
        results = []
        for f in os.listdir(docs_path):
            if f.endswith('.txt'):
                filepath = os.path.join(docs_path, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    for line in file:
                        if term.lower() in line.lower():
                            results.append((f, line.strip()))
        return results
    
    
    # Ejecutar
    print("NIVEL 4 - SOLUCIONES (Sin importaciones extra)")
    print("=" * 50)
    print(f"✓ Archivos .txt: {list_txt_files()}")
    print(f"✓ Tamaño total: {total_file_size()} bytes")
    print(f"✓ Búsqueda 'agentes': {len(search_term_basic('agentes'))} resultados")
