"""
Procesamiento de archivos línea por línea.
Contexto: Un agente procesa documentos grandes para crear embeddings sin cargar todo en memoria.
"""

import tempfile
from pathlib import Path

# ============================================================================
# 1. PROCESAR LÍNEA POR LÍNEA (Memory efficient para documentos grandes)
# ============================================================================

def process_document_lines(filename: str, processor_func) -> list:
    """
    Procesa un archivo línea por línea.
    Ideal para documentos grandes que no caben en memoria.
    """
    results = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')  # Elimina salto de línea
            if line.strip():  # Ignora líneas vacías
                results.append(processor_func(line))
    return results


# ============================================================================
# 2. TRANSFORMACIÓN DE CONTENIDO
# ============================================================================

def uppercase_processor(line: str) -> str:
    """Procesa una línea convirtiéndola a mayúsculas."""
    return line.upper()


def add_line_numbers(line: str, line_num: int) -> str:
    """Procesa una línea agregando número."""
    return f"[{line_num}] {line}"


def extract_sentences(line: str) -> list[str]:
    """Procesa una línea dividiendo en oraciones."""
    return [s.strip() + '.' for s in line.split('.') if s.strip()]


# ============================================================================
# 3. PROCESAR CON ESTADO (ej: contador de palabras)
# ============================================================================

def count_words_in_document(filename: str) -> dict:
    """
    Cuenta palabras en el documento mientras lo procesa línea por línea.
    Importante para análisis de documentos en agentes.
    """
    word_count = {}
    total_lines = 0
    total_words = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            total_lines += 1
            words = line.split()
            total_words += len(words)
            
            for word in words:
                word_lower = word.lower()
                word_count[word_lower] = word_count.get(word_lower, 0) + 1
    
    return {
        'total_lines': total_lines,
        'total_words': total_words,
        'unique_words': len(word_count),
        'word_frequency': word_count,
    }


# ============================================================================
# 4. FILTRAR LÍNEAS RELEVANTES (Ej: buscar en documento)
# ============================================================================

def search_in_document(filename: str, search_term: str, context_lines: int = 0) -> list[dict]:
    """
    Busca un término en el documento y retorna resultado con contexto.
    Común en RAG (Retrieval-Augmented Generation) de agentes.
    """
    results = []
    lines = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    for idx, line in enumerate(lines):
        if search_term.lower() in line.lower():
            start = max(0, idx - context_lines)
            end = min(len(lines), idx + context_lines + 1)
            
            results.append({
                'line_number': idx + 1,
                'match': line,
                'context': lines[start:end],
            })
    
    return results


# ============================================================================
# 5. PROCESAR Y GUARDAR RESULTADOS
# ============================================================================

def process_and_save(input_file: str, output_file: str, transforms: list) -> None:
    """
    Procesa archivo aplicando transformaciones y guarda resultado.
    """
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            line = line.rstrip('\n')
            
            # Aplicar todas las transformaciones
            for transform in transforms:
                line = transform(line)
            
            f_out.write(line + '\n')


# ============================================================================
# EJEMPLO PRÁCTICO
# ============================================================================

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        input_file = tmpdir / "document.txt"
        output_file = tmpdir / "processed_document.txt"
        
        # Crear documento de ejemplo
        sample_text = """Los agentes de IA pueden procesar documentos automáticamente.
Este es un sistema para análisis de textos.
La inteligencia artificial mejora cada día.
Los agentes LangChain utilizan herramientas externas.
Procesar archivos línea por línea es eficiente.
Este documento contiene información de ejemplo."""
        
        input_file.write_text(sample_text, encoding='utf-8')
        
        # 1. Procesar línea por línea
        print("1️⃣ PROCESAR LÍNEA POR LÍNEA")
        print("=" * 50)
        results = process_document_lines(str(input_file), uppercase_processor)
        for result in results[:3]:
            print(f"  {result[:60]}...")
        
        # 2. Contar palabras
        print("\n2️⃣ ANÁLISIS DE PALABRAS")
        print("=" * 50)
        analysis = count_words_in_document(str(input_file))
        print(f"  Total líneas: {analysis['total_lines']}")
        print(f"  Total palabras: {analysis['total_words']}")
        print(f"  Palabras únicas: {analysis['unique_words']}")
        print("  Top 5 palabras:")
        top_5 = sorted(analysis['word_frequency'].items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_5:
            print(f"    - {word}: {count}")
        
        # 3. Buscar en documento
        print("\n3️⃣ BÚSQUEDA EN DOCUMENTO")
        print("=" * 50)
        search_results = search_in_document(str(input_file), "agentes", context_lines=1)
        print(f"  Encontradas {len(search_results)} coincidencias de 'agentes':")
        for match in search_results:
            print(f"    Línea {match['line_number']}: {match['match']}")
        
        # 4. Procesar y guardar
        print("\n4️⃣ PROCESAR Y GUARDAR")
        print("=" * 50)
        process_and_save(
            str(input_file),
            str(output_file),
            [str.upper, lambda x: f">> {x}"]
        )
        print(f"  ✓ Archivo procesado guardado: {output_file.name}")
        print("  Primeras 2 líneas:")
        processed = output_file.read_text(encoding='utf-8').split('\n')
        for line in processed[:2]:
            print(f"    {line}")
