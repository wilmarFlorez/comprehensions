# ============================================================
#  DESAFÍO NIVEL 2 - COMPREHENSIONS
#  Resuelve usando list/dict comprehensions
#  Contexto: Un agente RAG necesita procesar documentos eficientemente
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
    # DESAFÍO 1: List comprehension - Listar archivos .txt
    # ============================================================
    # Retorna lista de nombres de archivos usando list comprehension
    
    def list_txt_files():
        # Tu solución: usa list comprehension
        return ___
    
    result = list_txt_files()
    assert len(result) == 3, f"Esperado 3, obtenido {len(result)}"
    assert all(f.endswith('.txt') for f in result)
    print("✓ Desafío 1: List comprehension - archivos .txt")
    
    
    # ============================================================
    # DESAFÍO 2: Dict comprehension - Mapear archivo->contenido
    # ============================================================
    # Retorna diccionario {filename: content} usando dict comprehension
    
    def documents_to_dict():
        # Tu solución: usa dict comprehension
        return ___
    
    result = documents_to_dict()
    assert len(result) == 3
    assert "report1.txt" in result
    print("✓ Desafío 2: Dict comprehension - archivo->contenido")
    
    
    # ============================================================
    # DESAFÍO 3: List comprehension con filtro
    # ============================================================
    # Retorna lista de archivos con más de 3 palabras
    
    def filter_long_documents(min_words=3):
        # Tu solución: usa list comprehension con if
        # Necesitas calcular palabras para cada archivo
        return ___
    
    result = filter_long_documents(3)
    assert isinstance(result, list)
    print("✓ Desafío 3: List comprehension con filtro")
    
    
    # ============================================================
    # DESAFÍO 4: Dict comprehension - Contar palabras por archivo
    # ============================================================
    # Retorna {filename: word_count}
    
    def word_count_per_file():
        # Tu solución: usa dict comprehension
        return ___
    
    result = word_count_per_file()
    assert len(result) == 3
    assert all(isinstance(v, int) for v in result.values())
    print("✓ Desafío 4: Dict comprehension - contar palabras")
    
    
    # ============================================================
    # DESAFÍO 5: List comprehension anidado
    # ============================================================
    # Retorna lista de tuplas (archivo, línea) para todas las líneas
    
    def all_lines_with_files():
        # Tu solución: usa list comprehension anidado
        # Resultado: [(archivo1, línea1), (archivo1, línea2), ...]
        return ___
    
    result = all_lines_with_files()
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)
    print("✓ Desafío 5: List comprehension anidado")
    
    
    # ============================================================
    # DESAFÍO 6: Buscar con comprehension
    # ============================================================
    # Retorna lista de (archivo, línea) donde línea contiene "agentes"
    
    def search_with_comprehension(search_term="agentes"):
        # Tu solución: usa list comprehension anidado con if
        return ___
    
    result = search_with_comprehension("agentes")
    assert len(result) > 0, "Debe encontrar coincidencias"
    print("✓ Desafío 6: Búsqueda con comprehension")


print("\n" + "=" * 50)
print("NIVEL 2 - COMPLETADO ✓")
print("Todos los desafíos con comprehensions pasaron.")
print("\nPróximo: Intenta NIVEL 3 para ser más conciso")
print("=" * 50)
