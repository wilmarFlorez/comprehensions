# ============================================================
#  SOLUCIÓN NIVEL 5 - PROGRAMACIÓN FUNCIONAL
#  Referencia: map(), filter(), lambda, reduce()
# ============================================================

import tempfile
from functools import reduce
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    docs_dir = tmpdir / "docs"
    docs_dir.mkdir()
    (docs_dir / "report1.txt").write_text("Los agentes\ninteligentes\nautónomos")
    (docs_dir / "report2.txt").write_text("Automatización\ninteligente")
    (docs_dir / "report3.txt").write_text("Datos")
    
    
    def uppercase_filenames():
        """Usar map() + lambda para mayúsculas."""
        files = [f.name for f in docs_dir.glob("*.txt")]
        return list(map(lambda x: x.upper(), files))
    
    
    def filter_by_pattern():
        """Usar filter() + lambda para filtrar."""
        files = [f.name for f in docs_dir.glob("*.txt")]
        return list(filter(lambda x: "report" in x, files))
    
    
    def size_info():
        """Combinar filter() + map()."""
        files = [f for f in docs_dir.glob("*.txt")]
        file_data = list(map(lambda f: (f.name, len(f.read_text())), files))
        return list(filter(lambda x: x[1] > 10, file_data))
    
    
    def total_words_with_reduce():
        """Usar reduce() para suma funcional."""
        files = [f for f in docs_dir.glob("*.txt")]
        word_counts = list(map(lambda f: len(f.read_text().split()), files))
        return reduce(lambda x, y: x + y, word_counts, 0)
    
    
    def functional_pipeline():
        """Tubería funcional completa."""
        # Paso 1: listar archivos .txt
        files = list(docs_dir.glob("*.txt"))
        
        # Paso 2: mapear a (nombre, tamaño)
        file_data = list(map(lambda f: (f.name, len(f.read_text())), files))
        
        # Paso 3: filtrar .txt (ya lo está, pero para demostrar)
        filtered = list(filter(lambda x: x[0].endswith('.txt'), file_data))
        
        # Paso 4: extraer solo tamaños
        sizes = list(map(lambda x: x[1], filtered))
        
        return sizes
    
    
    # Ejecutar
    print("NIVEL 5 - SOLUCIONES (Programación Funcional)")
    print("=" * 50)
    print(f"✓ Mayúsculas (map): {uppercase_filenames()}")
    print(f"✓ Filtro (filter): {filter_by_pattern()}")
    print(f"✓ map + filter: {size_info()}")
    print(f"✓ reduce: {total_words_with_reduce()} palabras")
    print(f"✓ Pipeline: {functional_pipeline()} (tamaños)")
    
    print("\n" + "=" * 50)
    print("COMPARACIÓN DE ESTILOS")
    print("=" * 50)
    print("""
    Nivel 1 (for-loops): Imperativo, verbose, pero claro
    Nivel 2 (comprehensions): Pythonic, conciso, readable
    Nivel 3 (one-liners): Extremadamente conciso
    Nivel 4 (sin imports): Portable, solo built-ins
    Nivel 5 (funcional): Composición, sin estado
    
    RECOMENDACIÓN: Usa Nivel 2 (comprehensions) en código real.
    Es el mejor balance entre claridad y concisión.
    """)
