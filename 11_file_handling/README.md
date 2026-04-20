# Manejo de Archivos en Python - Para Agentes de IA

## 📚 Descripción

Esta sección enseña **cómo trabajar con archivos en Python**, especializado en el contexto de **agentes de IA** y **LangChain**. Aprenderás a:

- ✅ Leer y escribir archivos de forma segura
- ✅ Procesar configuraciones JSON
- ✅ Procesar documentos grandes línea por línea
- ✅ Indexar múltiples documentos (RAG)
- ✅ Usar context managers para evitar fugas de recursos
- ✅ Resolver problemas comunes en agentes

## 🎯 ¿Por qué necesitas esto para aprender LangChain?

Los agentes de IA frecuentemente necesitan:

1. **Cargar configuración** → JSON, YAML
2. **Procesar documentos** → Para embeddings y RAG
3. **Mantener memoria** → Guardar/cargar conversaciones
4. **Indexar datos** → Para búsqueda rápida en agentes
5. **Manejar errores** → Operaciones seguras de archivo

## 📁 Estructura del Proyecto

```
11_file_handling/
├── learn/              # 🧑‍🏫 Ejemplos pedagogógicos
│   ├── basic_file_io.py          # Lectura/escritura básica
│   ├── json_config.py             # Manejo JSON (config de agentes)
│   ├── text_processing.py         # Procesamiento línea por línea
│   ├── directory_traversal.py     # Procesar múltiples archivos
│   └── context_managers.py        # Manejo seguro de recursos
│
├── practice.py         # ✏️ Ejercicios auto-verificados (10 ejercicios)
│
└── challenges/         # 🏆 5 niveles progresivos
    ├── level_1_for_loops.py      # Soluciona con for-loops
    ├── level_2_comprehensions.py # Soluciona con comprehensions
    ├── level_3_one_liners.py     # Soluciona como one-liners
    ├── level_4_no_imports.py     # Soluciona sin importaciones extra
    ├── level_5_functional.py     # Soluciona con map/filter/lambda
    └── solutions/                # 📖 Soluciones de referencia
        ├── level_1_solution.py
        ├── level_2_solution.py
        ├── level_3_solution.py
        ├── level_4_solution.py
        └── level_5_solution.py
```

## 🚀 Cómo Empezar

### Paso 1: Entiende los Conceptos (20 min)

Ejecuta los ejemplos en `learn/`:

```bash
python learn/basic_file_io.py
python learn/json_config.py
python learn/text_processing.py
python learn/directory_traversal.py
python learn/context_managers.py
```

### Paso 2: Practica (20 min)

Resuelve los ejercicios auto-verificados:

```bash
python practice.py
```

El sistema te dirá qué ejercicios pasaste ✓ y cuáles fallaron ✗.

### Paso 3: Desafíos Progresivos (60 min)

Intenta los 5 niveles en orden:

```bash
# Nivel 1: Domina for-loops
python challenges/level_1_for_loops.py

# Nivel 2: Aprende comprehensions
python challenges/level_2_comprehensions.py

# Nivel 3: Haz one-liners
python challenges/level_3_one_liners.py

# Nivel 4: Usa solo built-ins
python challenges/level_4_no_imports.py

# Nivel 5: Programación funcional
python challenges/level_5_functional.py
```

### Paso 4: Revisa Soluciones

Después de intentar cada nivel, revisa la solución:

```bash
python challenges/solutions/level_1_solution.py
```

## 🧠 Conceptos Clave Aprendidos

### 1. **Context Managers** (with statement)

```python
# ❌ Peligroso
f = open("archivo.txt")
contenido = f.read()
f.close()  # ¿Y si ocurre error?

# ✅ Seguro
with open("archivo.txt") as f:
    contenido = f.read()
# Se cierra automáticamente
```

### 2. **Procesar Línea por Línea** (Memory Efficient)

```python
# Para archivos grandes: no cargar todo en memoria
with open("documento_grande.txt") as f:
    for linea in f:
        procesar(linea)
```

### 3. **Manejo JSON** (Config de Agentes)

```python
import json

# Guardar config
config = {"model": "gpt-4", "temperature": 0.7}
with open("config.json", "w") as f:
    json.dump(config, f)

# Cargar config
with open("config.json") as f:
    config = json.load(f)
```

### 4. **Traversal de Directorios** (Indexar Documentos)

```python
from pathlib import Path

# Listar todos los .txt
for archivo in Path("documentos").glob("*.txt"):
    contenido = archivo.read_text()
    procesar(contenido)
```

### 5. **Comprehensions vs For-loops**

```python
# For-loop (Nivel 1)
archivos = []
for f in Path(".").glob("*.txt"):
    archivos.append(f.name)

# Comprehension (Nivel 2 - Recomendado en código real)
archivos = [f.name for f in Path(".").glob("*.txt")]

# One-liner (Nivel 3 - Muy conciso)
# (igual que arriba, pero en contexto más complejo)

# Funcional (Nivel 5)
archivos = list(map(lambda f: f.name, Path(".").glob("*.txt")))
```

## 🎓 Patrón Pedagógico

Cada desafío sigue este patrón:

1. **Nivel 1 (For-loops)**: Aprende la lógica con loops explícitos
2. **Nivel 2 (Comprehensions)**: Refactoriza a Pythonic comprehensions
3. **Nivel 3 (One-liners)**: Optimiza a máxima concisión
4. **Nivel 4 (Sin imports)**: Usa solo built-ins de Python
5. **Nivel 5 (Funcional)**: Piensa en composición de funciones

**Recomendación**: El Nivel 2 es el "sweet spot" para código real.

## 💡 Casos de Uso en Agentes de IA

### 1. Sistema RAG (Retrieval-Augmented Generation)

```python
# Indexar documentos
for archivo in Path("documentos").glob("*.txt"):
    contenido = archivo.read_text()
    embeddings = modelo.embed(contenido)
    guardar_embedding(archivo.name, embeddings)
```

### 2. Cargar Configuración de Agente

```python
with open("agent_config.json") as f:
    config = json.load(f)
    agente = Agent(model=config["model"], tools=config["tools"])
```

### 3. Guardar Historial de Conversación

```python
historial = []
while True:
    usuario_input = input("Tú: ")
    respuesta = agente.run(usuario_input)
    historial.append({"user": usuario_input, "agent": respuesta})
    
    # Guardar historial
    with open("historial.json", "w") as f:
        json.dump(historial, f)
```

### 4. Procesar Documentos Grandes

```python
# Procesa línea por línea: eficiente en memoria
with open("documento_grande.pdf") as f:
    for linea in f:
        embedding = modelo.embed(linea)
        guardar(embedding)
```

## 📚 Recursos Complementarios

Después de esta sección, puedes aprender:
- **YAML**: Para archivos de configuración más complejos
- **CSV/Pandas**: Para datos tabulares
- **SQLite**: Para almacenamiento persistente
- **Async I/O**: Para lectura no-bloqueante de archivos

## ✅ Checklist de Aprendizaje

- [ ] Entiendo cómo usar `with` para lectura/escritura segura
- [ ] Puedo procesar archivos línea por línea
- [ ] Sé cargar y guardar JSON
- [ ] Puedo listar archivos en un directorio
- [ ] Entiendo context managers personalizados
- [ ] Puedo resolver los desafíos Nivel 1 (for-loops)
- [ ] Puedo resolver los desafíos Nivel 2 (comprehensions)
- [ ] Puedo resolver los desafíos Nivel 5 (funcional)

## 🆘 Consejos de Debugging

**"Mi archivo no se carga"**
- ¿Está la ruta correcta? Usa `print(Path("archivo").exists())`
- ¿El archivo está en el lugar esperado?

**"Encoding issues"**
- Siempre especifica: `open(..., encoding='utf-8')`

**"Archivo no se guarda"**
- Verifica que el directorio existe: `Path(directorio).mkdir(exist_ok=True)`
- Usa context manager para garantizar que se escribe

**"Archivo muy grande"**
- Procesa línea por línea, no `read_all()`
- Usa generadores para memoria eficiente

## 🎉 Próximos Pasos

Después de dominar esta sección:

1. **Aplica a LangChain**: Carga documentos con DocumentLoader
2. **Crea un RAG simple**: Indexa documentos y búscalos
3. **Construye un agente**: Que guarde su memoria en archivos

---

**¿Listo? Comienza con `python learn/basic_file_io.py`** 🚀
