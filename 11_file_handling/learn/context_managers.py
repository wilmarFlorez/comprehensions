"""
Context Managers - Manejo seguro de archivos y recursos.
Contexto: Los agentes deben manejar archivos de forma segura sin fugas de recursos.
"""

import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import IO, Generator

# ============================================================================
# 1. CONTEXT MANAGERS CON FILES (with statement)
# ============================================================================

# ❌ PELIGROSO - Archivo puede quedar abierto si ocurre error:
def unsafe_read_file(filename: str) -> str:
    f = open(filename, 'r', encoding='utf-8')
    content = f.read()
    # Si ocurre error aquí, f.close() nunca se ejecuta!
    f.close()
    return content


# ✅ SEGURO - Context manager garantiza cierre:
def safe_read_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# ============================================================================
# 2. CREAR CONTEXT MANAGERS PERSONALIZADOS
# ============================================================================

@contextmanager
def open_file_safe(filename: str, mode: str = 'r'):
    """
    Context manager personalizado para manejo seguro de archivos.
    Garantiza que el archivo se cierre incluso si ocurre excepción.
    """
    f = None
    try:
        f = open(filename, mode, encoding='utf-8')
        yield f
    finally:
        # Se ejecuta SIEMPRE, incluso si hay error
        if f and not f.closed:
            f.close()
            print(f"✓ Archivo cerrado: {filename}")


# ============================================================================
# 3. CONTEXT MANAGER PARA TRANSACCIONES DE ARCHIVO
# ============================================================================

@contextmanager
def atomic_file_write(filename: str):
    """
    Context manager que escribe en archivo temporal y lo reemplaza al final.
    Si ocurre error, el archivo original se mantiene intacto.
    """
    temp_filename = filename + '.tmp'
    try:
        yield temp_filename
        # Si llegamos aquí, la escritura fue exitosa
        Path(temp_filename).replace(filename)
        print(f"✓ Archivo actualizado de forma atómica: {filename}")
    except Exception as e:
        # Si hay error, eliminar archivo temporal y relanzar excepción
        Path(temp_filename).unlink(missing_ok=True)
        print(f"✗ Error, cambios descartados: {e}")
        raise


# ============================================================================
# 4. CONTEXT MANAGER PARA GESTIÓN DE MÚLTIPLES ARCHIVOS
# ============================================================================

@contextmanager
def batch_open_files(filenames: list[str], mode: str = 'r') -> Generator[list[IO], None, None]:
    """
    Abre múltiples archivos y garantiza que todos se cierren.
    Útil para procesar múltiples documentos en un agente.
    """
    files = []
    try:
        for filename in filenames:
            files.append(open(filename, mode, encoding='utf-8'))
        yield files
    finally:
        for f in files:
            if f and not f.closed:
                f.close()
        print(f"✓ Cerrados {len(files)} archivos")


# ============================================================================
# 5. CONTEXT MANAGER CON LOGGING DE OPERACIONES
# ============================================================================

@contextmanager
def logged_file_operation(filename: str, operation: str):
    """
    Context manager que registra inicio y fin de operación de archivo.
    Útil para debugging en agentes.
    """
    print(f"📝 Iniciando: {operation} en {Path(filename).name}")
    try:
        yield
    except Exception as e:
        print(f"❌ Error durante {operation}: {e}")
        raise
    else:
        print(f"✅ Completado: {operation}")


# ============================================================================
# 6. CONTEXT MANAGER PARA BACKUP
# ============================================================================

@contextmanager
def with_backup(filename: str):
    """
    Context manager que crea backup antes de modificar archivo.
    Si ocurre error, puede restaurar desde backup.
    """
    filepath = Path(filename)
    backup_path = Path(str(filename) + '.backup')
    
    # Crear backup
    if filepath.exists():
        backup_path.write_bytes(filepath.read_bytes())
        print(f"✓ Backup creado: {backup_path.name}")
    
    try:
        yield
    except Exception:
        # Restaurar desde backup
        if backup_path.exists():
            backup_path.replace(filename)
            print(f"⚠ Restaurado desde backup: {filename}")
        raise
    else:
        # Eliminar backup si todo fue bien
        backup_path.unlink(missing_ok=True)


# ============================================================================
# EJEMPLO PRÁCTICO
# ============================================================================

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Archivo de ejemplo
        agent_log = tmpdir / "agent_log.txt"
        config_file = tmpdir / "agent_config.txt"
        
        # 1. Context manager básico
        print("1️⃣ CONTEXT MANAGER BÁSICO")
        print("=" * 50)
        agent_log.write_text("Agente iniciado\nProcesando solicitud")
        with safe_read_file(str(agent_log)) as content:
            print(f"Contenido: {content}")
        
        # 2. Context manager personalizado
        print("\n2️⃣ CONTEXT MANAGER PERSONALIZADO")
        print("=" * 50)
        with open_file_safe(str(agent_log), mode='a') as f:
            f.write("\nAgente finalizado")
        print(f"Contenido final de {agent_log.name}:")
        print(f"  {agent_log.read_text()}")
        
        # 3. Escritura atómica
        print("\n3️⃣ ESCRITURA ATÓMICA (Segura)")
        print("=" * 50)
        config_file.write_text("model=gpt-4\ntemperature=0.7")
        with atomic_file_write(str(config_file)) as temp_file:
            with open(temp_file, 'w') as f:
                f.write("model=gpt-4o\ntemperature=0.5\n")
        print(f"Contenido actualizado: {config_file.read_text()}")
        
        # 4. Múltiples archivos
        print("\n4️⃣ MANEJO DE MÚLTIPLES ARCHIVOS")
        print("=" * 50)
        
        file1 = tmpdir / "doc1.txt"
        file2 = tmpdir / "doc2.txt"
        file1.write_text("Primer documento")
        file2.write_text("Segundo documento")
        
        with batch_open_files([str(file1), str(file2)]) as files:
            for idx, f in enumerate(files, 1):
                content = f.read()
                print(f"  Archivo {idx}: {content}")
        
        # 5. Logging de operaciones
        print("\n5️⃣ LOGGING DE OPERACIONES")
        print("=" * 50)
        with logged_file_operation(str(agent_log), "lectura de log"):
            content = agent_log.read_text()
            lines = len(content.split('\n'))
        print(f"  Total líneas: {lines}")
        
        # 6. Con backup
        print("\n6️⃣ MANEJO CON BACKUP")
        print("=" * 50)
        config_file.write_text("version=1.0.0\n")
        try:
            with with_backup(str(config_file)):
                with open(config_file, 'w') as f:
                    f.write("version=1.1.0\n")
                print("  Configuración actualizada")
        except Exception:
            print("  Error detectado, archivo restaurado")
