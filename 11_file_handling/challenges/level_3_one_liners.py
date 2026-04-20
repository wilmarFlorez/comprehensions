# ============================================================
#  DESAFÍO NIVEL 3 - ONE-LINERS
#  Resuelve como one-liner (sin variables intermedias).
#  Contexto: Código conciso y Pythonic para agentes
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
    
    
    # ============================================================
    # DESAFÍO 1: One-liner - Listar archivos
    # ============================================================
    # Sin variables intermedias
    
    def list_txt_files():
        return ___
    
    result = list_txt_files()
    assert len(result) == 3
    print("✓ Desafío 1: One-liner - listar archivos")
    
    
    # ============================================================
    # DESAFÍO 2: One-liner - Diccionario archivo->contenido
    # ============================================================
    
    def documents_to_dict():
        return ___
    
    result = documents_to_dict()
    assert len(result) == 3 and "report1.txt" in result
    print("✓ Desafío 2: One-liner - dict archivo->contenido")
    
    
    # ============================================================
    # DESAFÍO 3: One-liner - Total de palabras
    # ============================================================
    
    def total_words():
        return ___
    
    result = total_words()
    assert isinstance(result, int) and result > 0
    print("✓ Desafío 3: One-liner - total de palabras")
    
    
    # ============================================================
    # DESAFÍO 4: One-liner - Archivos ordenados por tamaño
    # ============================================================
    # Retorna lista de (nombre, tamaño) ordenada por tamaño
    
    def files_by_size():
        return ___
    
    result = files_by_size()
    assert len(result) == 3
    assert all(len(item) == 2 for item in result)
    print("✓ Desafío 4: One-liner - archivos por tamaño")
    
    
    # ============================================================
    # DESAFÍO 5: One-liner - Búsqueda global
    # ============================================================
    # Retorna lista (archivo, línea) que contiene "de"
    
    def search_results():
        return ___
    
    result = search_results()
    assert len(result) > 0
    print("✓ Desafío 5: One-liner - búsqueda global")


print("\n" + "=" * 50)
print("NIVEL 3 - COMPLETADO ✓")
print("Código conciso y efectivo como one-liners.")
print("\nPróximo: NIVEL 4 - Sin importaciones")
print("=" * 50)
