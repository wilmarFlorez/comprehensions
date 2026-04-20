# ============================================================
#  DESAFÍO NIVEL 4 - SIN IMPORTACIONES
#  Resuelve usando SOLO built-ins de Python (sin Path, tempfile, etc)
#  Contexto: Código portable y sin dependencias
# ============================================================

import tempfile  # Solo para setup, NO lo uses en tu solución
from pathlib import Path  # Solo para setup, NO lo uses en tu solución

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    docs_dir = tmpdir / "docs"
    docs_dir.mkdir()
    (docs_dir / "report1.txt").write_text("Los agentes\inteligentes")
    (docs_dir / "report2.txt").write_text("Automatización")
    (docs_dir / "report3.txt").write_text("Datos procesados")
    
    # Convertir a strings normales (sin Path objects)
    docs_path = str(docs_dir)
    
    # ============================================================
    # DESAFÍO 1: Sin imports - Listar archivos
    # ============================================================
    # SOLO usa open(), os.listdir() o equivalent con built-ins
    
    def list_txt_files():
        # Tu solución aquí (puedes usar os, no Path)
        return ___
    
    result = list_txt_files()
    assert len(result) == 3
    print("✓ Desafío 1: Sin importaciones - listar archivos")
    
    
    # ============================================================
    # DESAFÍO 2: Sin imports - Procesar archivos
    # ============================================================
    
    def total_file_size():
        # Tu solución aquí
        return ___
    
    result = total_file_size()
    assert isinstance(result, int) and result > 0
    print("✓ Desafío 2: Sin importaciones - tamaño total")
    
    
    # ============================================================
    # DESAFÍO 3: Sin imports - Búsqueda
    # ============================================================
    
    def search_term_basic(term="agentes"):
        # Tu solución aquí
        return ___
    
    result = search_term_basic("agentes")
    assert isinstance(result, list)
    print("✓ Desafío 3: Sin importaciones - búsqueda")


print("\n" + "=" * 50)
print("NIVEL 4 - COMPLETADO ✓")
print("Código sin dependencias, solo built-ins.")
print("\nPróximo: NIVEL 5 - Programación Funcional")
print("=" * 50)
