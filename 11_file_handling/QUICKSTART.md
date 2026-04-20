"""
GUÍA RÁPIDA: Manejo de Archivos en Python (Contexto de Agentes de IA)
=====================================================================

¡Hola! Has encontrado una nueva sección diseñada específicamente para
aprender manejo de archivos en Python mientras trabajas con agentes de IA
y LangChain.

INICIO RÁPIDO (5 minutos)
================================

1. Lee la carpeta 11_file_handling/README.md

2. Ejecuta un ejemplo para ver cómo funciona:
   $ python 11_file_handling/learn/basic_file_io.py

3. Intenta completar los ejercicios:
   $ python 11_file_handling/practice.py

PASOS RECOMENDADOS
=================================

PASO 1: Entiende los conceptos (20 minutos)
   Ejecuta en orden:
   - python learn/basic_file_io.py          # Leer/escribir básico
   - python learn/json_config.py             # Configuración de agentes
   - python learn/text_processing.py         # Procesar documentos
   - python learn/directory_traversal.py     # Indexar RAG
   - python learn/context_managers.py        # Manejo seguro

PASO 2: Practica con ejercicios (20 minutos)
   $ python practice.py
   
   Completa los 10 ejercicios donde dice "..."
   Los asserts te dirán si acertaste.

PASO 3: Desafíos progresivos (60 minutos)
   Resuelve los 5 niveles EN ORDEN:
   
   Level 1: Usa for-loops tradicionales
   $ python challenges/level_1_for_loops.py
   
   Level 2: Usa list/dict comprehensions (Recomendado)
   $ python challenges/level_2_comprehensions.py
   
   Level 3: Haz todo como one-liners
   $ python challenges/level_3_one_liners.py
   
   Level 4: Usa solo built-ins (sin Path, etc)
   $ python challenges/level_4_no_imports.py
   
   Level 5: Programación funcional (map/filter/lambda)
   $ python challenges/level_5_functional.py

PASO 4: Compara con soluciones
   Después de cada nivel, revisa la solución:
   $ python challenges/solutions/level_1_solution.py

TEMAS CUBIERTOS
=================================

✅ Lectura y escritura de archivos
✅ Context managers (with statement)
✅ Manejo JSON (configuración)
✅ Procesamiento línea por línea
✅ Directory traversal (múltiples archivos)
✅ RAG indexing (para agentes)
✅ Error handling en I/O

POR QUÉ ES IMPORTANTE PARA LANGCHAIN
====================================

Los agentes de IA necesitan:

1. Cargar configuración
   → JSON (temperaturte, model, tools)

2. Procesar documentos
   → Para embeddings y búsqueda (RAG)

3. Guardar memoria
   → Historial de conversaciones

4. Indexar datos
   → Búsqueda rápida en agentes

5. Manejo seguro
   → Context managers para evitar errores

CASOS DE USO REALES
=================================

🤖 Agente RAG:
   for archivo in documentos/:
       contenido = leer(archivo)
       embedding = modelo.embed(contenido)
       guardar(embedding)

📋 Guardar historial:
   with open("historial.json") as f:
       json.dump(conversaciones, f)

⚙️ Cargar configuración:
   with open("agent_config.json") as f:
       config = json.load(f)

📊 Procesar archivo grande:
   with open("documento_grande.txt") as f:
       for linea in f:
           procesar(linea)  # Memory-efficient

PATRÓN DE APRENDIZAJE
==================================

Cada desafío te enseña la MISMA tarea con 5 enfoques diferentes:

Comportamiento:
   Level 1    → Level 2    → Level 3    → Level 4    → Level 5
   for-loop   compreh.     one-liner    sin import   map/filter
   │          │            │            │            │
   └─ Más imperativo      ─┘            └─ Más funcional/conciso ─┘

EJEMPLO: Listar archivos .txt

Level 1 (For-loop):
   archivos = []
   for f in Path(".").glob("*.txt"):
       archivos.append(f.name)

Level 2 (Comprehension) ⭐ RECOMENDADO:
   archivos = [f.name for f in Path(".").glob("*.txt")]

Level 3 (One-liner):
   (igual al 2, pero es one-liner en contexto más complejo)

Level 4 (Sin imports Path):
   archivos = [f for f in os.listdir(".") if f.endswith(".txt")]

Level 5 (Funcional):
   archivos = list(map(lambda f: f.name, Path(".").glob("*.txt")))

DÓNDE BUSCAR AYUDA
================================

Si tienes dudas sobre:

• Lectura/escritura       → learn/basic_file_io.py
• JSON (Config)           → learn/json_config.py
• Procesar línea por línea → learn/text_processing.py
• Múltiples archivos      → learn/directory_traversal.py
• Context managers        → learn/context_managers.py
• Cómo resolver desafíos  → challenges/solutions/

PRÓXIMOS PASOS DESPUÉS DE ESTA SECCIÓN
======================================

1. Aprende YAML (configuraciones más complejas)
2. Aprende CSV/Pandas (datos tabulares)
3. Aprende SQLite (persistencia)
4. Construye un RAG simple con tus nuevas habilidades

¡COMIENZA AHORA!
===============

Te recomiendo empezar así:

1. Lee 11_file_handling/README.md
2. Ejecuta: python 11_file_handling/learn/basic_file_io.py
3. Ejecuta: python 11_file_handling/practice.py
4. Intenta los desafíos Level 1 y 2

¡Que disfrutes aprendiendo! 🚀
"""

if __name__ == "__main__":
    print(__doc__)
