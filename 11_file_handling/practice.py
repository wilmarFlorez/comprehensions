# ============================================================
#  PRÁCTICA — MANEJO DE ARCHIVOS EN AGENTES DE IA
#  Escribe tu solución donde dice ... y ejecuta el archivo.
#  Los asserts te dirán si acertaste o no.
# ============================================================

import json
import tempfile
from pathlib import Path

passed = 0
total = 10


def ejercicio(num, descripcion, solucion, esperado):
    """Evalúa un ejercicio individual sin detener el resto."""
    global passed
    try:
        resultado = solucion()
        if resultado is ...:
            print(f"- Ejercicio {num}: {descripcion} — pendiente")
            return
        assert resultado == esperado, f"Esperado {esperado}, obtenido {resultado}"
        passed += 1
        print(f"✓ Ejercicio {num}: {descripcion} — OK")
    except AssertionError as e:
        print(f"✗ Ejercicio {num}: {descripcion} — FALLÓ: {e}")
    except Exception as e:
        print(f"✗ Ejercicio {num}: {descripcion} — ERROR: {e}")


# ============================================================
# PREPARAR ARCHIVOS TEMPORALES PARA LOS EJERCICIOS
# ============================================================

tmpdir = Path(tempfile.mkdtemp())

# Archivo 1: Conversación simple
conv_file = tmpdir / "conversation.txt"
conv_file.write_text("""Usuario: Hola agente
Agente: Hola, ¿cómo te puedo ayudar?
Usuario: ¿Cuál es la capital de Francia?
Agente: La capital es París.""")

# Archivo 2: Configuración JSON
config_file = tmpdir / "config.json"
config_file.write_text(json.dumps({
    "model": "gpt-4",
    "temperature": 0.7,
    "tools": ["search", "calculate"]
}))

# Archivo 3: Documento con múltiples líneas
doc_file = tmpdir / "document.txt"
doc_file.write_text("""Los agentes de IA revolucionan el desarrollo.
Pueden automatizar tareas complejas.
Requieren buena estructuración de prompts.
Los agentes inteligentes mejoran con feedback.""")

# Archivo 4: Múltiples archivos en carpeta
docs_dir = tmpdir / "documents"
docs_dir.mkdir()
(docs_dir / "file1.txt").write_text("Primer archivo")
(docs_dir / "file2.txt").write_text("Segundo archivo")
(docs_dir / "file3.txt").write_text("Tercer archivo")

# ============================================================
# EJERCICIO 1: Lectura básica
# Lee el archivo conversation.txt y retorna el número de líneas.
# ============================================================

def ex1():
    """Lee conversation.txt y cuenta líneas."""
    with open(str(conv_file), 'r', encoding='utf-8') as f:
        lines = ...
    return len(lines)

ejercicio(1, "Lectura - Contar líneas",
    ex1,
    4,  # 4 líneas en conversation.txt
)


# ============================================================
# EJERCICIO 2: Escritura básica
# Escribe un nuevo archivo llamado "output.txt" con 3 líneas de texto.
# Retorna el número de líneas escritas.
# ============================================================

def ex2():
    """Escribe en un archivo nuevo."""
    output_file = tmpdir / "output.txt"
    with open(str(output_file), 'w', encoding='utf-8') as f:
        ...
    # Verificar lo que escribiste
    written = output_file.read_text().count('\n')
    return written

ejercicio(2, "Escritura - Crear archivo con 3 líneas",
    ex2,
    3,  # 3 líneas (conta \n)
)


# ============================================================
# EJERCICIO 3: Procesamiento línea por línea
# Lee document.txt línea por línea y cuenta líneas que contienen "agentes".
# ============================================================

def ex3():
    """Procesa líneas y filtra por término."""
    count = 0
    with open(str(doc_file), 'r', encoding='utf-8') as f:
        for line in f:
            ...
    return count

ejercicio(3, "Procesamiento - Filtrar por término",
    ex3,
    2,  # 2 líneas contienen "agentes" o "agentes"
)


# ============================================================
# EJERCICIO 4: JSON - Cargar configuración
# Carga config.json y retorna el valor de "temperature".
# ============================================================

def ex4():
    """Carga JSON y extrae un valor."""
    with open(str(config_file), 'r', encoding='utf-8') as f:
        data = ...
    return data.get("temperature")

ejercicio(4, "JSON - Cargar configuración",
    ex4,
    0.7,  # temperature en config
)


# ============================================================
# EJERCICIO 5: JSON - Modificar y guardar
# Carga config.json, cambia temperature a 0.3, y guarda.
# Retorna True si se guardó correctamente.
# ============================================================

def ex5():
    """Modifica JSON y lo guarda."""
    test_config = tmpdir / "test_config.json"
    test_config.write_text(json.dumps({"temperature": 0.7}))
    
    # Tu código aquí:
    # 1. Carga el JSON
    # 2. Modifica temperature a 0.3
    # 3. Guarda el archivo
    ...
    
    # Verificación
    with open(str(test_config), 'r') as f:
        final = json.load(f)
    return final.get("temperature") == 0.3

ejercicio(5, "JSON - Modificar y guardar",
    ex5,
    True,
)


# ============================================================
# EJERCICIO 6: Append - Agregar línea a archivo
# Agrega "Usuario: Gracias" al final de conversation.txt sin sobreescribir.
# Retorna el número total de líneas después.
# ============================================================

def ex6():
    """Agrega contenido sin sobreescribir."""
    test_conv = tmpdir / "test_conv.txt"
    test_conv.write_text("Línea 1\nLínea 2")
    
    # Tu código aquí: Agrega "Línea 3"
    ...
    
    # Verificación
    lines = test_conv.read_text().split('\n')
    return len([l for l in lines if l.strip()])

ejercicio(6, "Append - Agregar sin sobreescribir",
    ex6,
    3,  # 3 líneas después de agregar
)


# ============================================================
# EJERCICIO 7: Listar archivos en directorio
# Cuenta los archivos .txt en la carpeta "documents".
# ============================================================

def ex7():
    """Lista archivos en un directorio."""
    count = 0
    # Tu código aquí: Cuenta archivos .txt en docs_dir
    ...
    return count

ejercicio(7, "Directorio - Contar archivos .txt",
    ex7,
    3,  # 3 archivos .txt en documents
)


# ============================================================
# EJERCICIO 8: Procesar múltiples archivos
# Lee todos los archivos en "documents" y suma el total de palabras.
# ============================================================

def ex8():
    """Procesa múltiples archivos."""
    total_words = 0
    # Tu código aquí:
    # Itera sobre archivos en docs_dir
    # Cuenta palabras en cada uno
    ...
    return total_words

ejercicio(8, "Múltiples archivos - Contar palabras",
    ex8,
    6,  # "Primer archivo" + "Segundo archivo" + "Tercer archivo" = 6 palabras
)


# ============================================================
# EJERCICIO 9: Path con validación
# Verifica si conversation.txt existe usando Path().
# Retorna True o False.
# ============================================================

def ex9():
    """Verifica existencia de archivo con Path."""
    exists = ...
    return exists

ejercicio(9, "Path - Verificar existencia",
    ex9,
    True,  # conversation.txt sí existe
)


# ============================================================
# EJERCICIO 10: Context Manager
# Abre conversation.txt con context manager y retorna True si se cerró correctamente.
# (Pista: verifica f.closed después del with)
# ============================================================

def ex10():
    """Usa context manager para garantizar cierre."""
    f = None
    with open(str(conv_file), 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Después del with, ¿está el archivo cerrado?
    closed = ...
    return closed

ejercicio(10, "Context Manager - Verificar cierre",
    ex10,
    True,  # El archivo debe cerrarse automáticamente
)


# ============================================================
# RESUMEN
# ============================================================

print("\n" + "=" * 50)
print(f"RESULTADO: {passed}/{total} ejercicios completados ✓")
print("=" * 50)

if passed == total:
    print("¡Excelente! 🎉 Has completado toda la práctica.")
    print("Próximos pasos:")
    print("  1. Revisa learn/ para entender los temas en profundidad")
    print("  2. Intenta los desafíos en challenges/")
elif passed >= total * 0.7:
    print("¡Buen progreso! 📈 Sigue practicando.")
else:
    print("Revisa los ejercicios fallidos y consulta la sección learn/")
