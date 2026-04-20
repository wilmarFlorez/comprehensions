# ============================================================
#  DESAFÍO NIVEL 1 - FOR LOOPS
#  Resuelve usando for-loops tradicionales
#  Contexto: Un agente necesita procesar documentos
# ============================================================

import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    # Crear datos de prueba
    docs_dir = tmpdir / "docs"
    docs_dir.mkdir()
    (docs_dir / "report1.txt").write_text("Los agentes de IA\nsimplificar tareas\ncomplexas")
    (docs_dir / "report2.txt").write_text("Automatización inteligente\nimprove productividad")
    (docs_dir / "report3.txt").write_text("Procesamiento de datos\nen tiempo real")
    
    # ============================================================
    # DESAFÍO 1: Listar todos los archivos .txt
    # ============================================================
    # Retorna una lista con los nombres de todos los archivos .txt
    
    def list_txt_files():
        files = []
        # Tu solución aquí (usa for-loop)
        ___
        return files
    
    result = list_txt_files()
    assert len(result) == 3, f"Esperado 3 archivos, obtenido {len(result)}"
    assert all(f.endswith('.txt') for f in result), "Todos deben ser .txt"
    print("✓ Desafío 1: Listar archivos .txt")
    
    
    # ============================================================
    # DESAFÍO 2: Contar palabras en todos los documentos
    # ============================================================
    # Lee todos los archivos y cuenta el total de palabras
    
    def count_total_words():
        total = 0
        # Tu solución aquí (usa for-loop anidado)
        ___
        return total
    
    result = count_total_words()
    assert result == 11, f"Esperado 11 palabras, obtenido {result}"
    print("✓ Desafío 2: Contar palabras totales")
    
    
    # ============================================================
    # DESAFÍO 3: Crear diccionario archivo->contenido
    # ============================================================
    # Retorna un diccionario donde key=nombre archivo, value=contenido
    
    def documents_to_dict():
        doc_dict = {}
        # Tu solución aquí (usa for-loop)
        ___
        return doc_dict
    
    result = documents_to_dict()
    assert len(result) == 3, "Esperado 3 entradas en dict"
    assert "report1.txt" in result, "Debe contener report1.txt"
    print("✓ Desafío 3: Crear diccionario de documentos")
    
    
    # ============================================================
    # DESAFÍO 4: Filtrar documentos con más de N palabras
    # ============================================================
    # Retorna lista de archivos que tienen más de 3 palabras
    
    def filter_long_documents(min_words=3):
        result = []
        # Tu solución aquí (usa for-loop con if)
        ___
        return result
    
    result = filter_long_documents(min_words=3)
    assert len(result) >= 1, f"Esperado al menos 1, obtenido {len(result)}"
    print("✓ Desafío 4: Filtrar documentos largos")
    
    
    # ============================================================
    # DESAFÍO 5: Buscar término en todos los documentos
    # ============================================================
    # Busca "agentes" en todos los archivos
    # Retorna lista de tuplas (archivo, línea_encontrada)
    
    def search_in_documents(search_term="agentes"):
        results = []
        # Tu solución aquí (usa for-loops anidados)
        ___
        return results
    
    result = search_in_documents("agentes")
    assert len(result) > 0, "Debe encontrar al menos 1 coincidencia"
    print("✓ Desafío 5: Buscar término en documentos")


print("\n" + "=" * 50)
print("NIVEL 1 - COMPLETADO ✓")
print("Todos los desafíos con for-loops tradicionales pasaron.")
print("\nPróximo: Intenta NIVEL 2 para resolver con comprehensions")
print("=" * 50)
