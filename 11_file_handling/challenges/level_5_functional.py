# ============================================================
#  DESAFÍO NIVEL 5 - PROGRAMACIÓN FUNCIONAL
#  Resuelve usando map(), filter(), lambda
#  Contexto: Estilo funcional y composición de funciones
# ============================================================

import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    docs_dir = tmpdir / "docs"
    docs_dir.mkdir()
    (docs_dir / "report1.txt").write_text("Los agentes\ninteligentes\nautónomos")
    (docs_dir / "report2.txt").write_text("Automatización\ninteligente")
    (docs_dir / "report3.txt").write_text("Datos")
    
    
    # ============================================================
    # DESAFÍO 1: map + lambda - Procesar nombres
    # ============================================================
    # Retorna lista de nombres en MAYÚSCULAS usando map()
    
    def uppercase_filenames():
        files = [f.name for f in Path(tmpdir / "docs").glob("*.txt")]
        # Tu solución: usa map() y lambda
        return ___
    
    result = uppercase_filenames()
    assert all(name.isupper() for name in result)
    print("✓ Desafío 1: map + lambda - mayúsculas")
    
    
    # ============================================================
    # DESAFÍO 2: filter + lambda - Filtrar por condición
    # ============================================================
    # Retorna lista de nombres que contienen "report" usando filter()
    
    def filter_by_pattern():
        files = [f.name for f in Path(tmpdir / "docs").glob("*.txt")]
        # Tu solución: usa filter() y lambda
        return ___
    
    result = filter_by_pattern()
    assert len(result) >= 2
    print("✓ Desafío 2: filter + lambda - filtrar por patrón")
    
    
    # ============================================================
    # DESAFÍO 3: map + filter combinados
    # ============================================================
    # Retorna tuplas (nombre, tamaño) para archivos con tamaño > 10 bytes
    
    def size_info():
        # Tu solución: combina filter() y map() con lambdas
        return ___
    
    result = size_info()
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) for item in result)
    print("✓ Desafío 3: map + filter combinados")
    
    
    # ============================================================
    # DESAFÍO 4: reduce (avec functools)
    # ============================================================
    # Usa reduce() para sumar el total de palabras en todos los archivos
    
    def total_words_with_reduce():
        # Tu solución: usa reduce() con lambda
        return ___
    
    result = total_words_with_reduce()
    assert isinstance(result, int) and result > 0
    print("✓ Desafío 4: reduce - suma funcional")
    
    
    # ============================================================
    # DESAFÍO 5: Composición funcional
    # ============================================================
    # Crea tubería: listar → filtrar .txt → mapear tamaño
    
    def functional_pipeline():
        # Tu solución: cadena de map/filter/lambda
        # Retorna lista de tamaños de archivos .txt
        return ___
    
    result = functional_pipeline()
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)
    print("✓ Desafío 5: Composición funcional")


print("\n" + "=" * 50)
print("NIVEL 5 - COMPLETADO ✓")
print("Programación funcional con map/filter/lambda.")
print("\nFelicidades! Has completado los 5 niveles.")
print("Verifica las soluciones en solutions/")
print("=" * 50)
