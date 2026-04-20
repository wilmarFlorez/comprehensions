"""
Lectura y escritura básica de archivos.
Contexto: Un agente de IA necesita guardar y cargar historiales de conversación.
"""

import tempfile
from pathlib import Path

# ============================================================================
# 1. ESCRITURA BÁSICA - Guardar historial de conversación
# ============================================================================

# Forma antigua (no recomendada):
# f = open('conversation.txt', 'w')
# f.write('Usuario: Hola\n')
# f.write('Agente: ¿Cómo te puedo ayudar?\n')
# f.close()  # Fácil olvidar esto

# Forma recomendada con context manager:
def save_conversation(messages: list[str], filename: str) -> None:
    """Guarda un historial de conversación en archivo."""
    with open(filename, 'w', encoding='utf-8') as f:
        for msg in messages:
            f.write(msg + '\n')
    print(f"✓ Conversación guardada en {filename}")


# ============================================================================
# 2. LECTURA BÁSICA - Cargar historial
# ============================================================================

def load_conversation(filename: str) -> list[str]:
    """Carga un historial de conversación desde archivo."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f.readlines()]


# ============================================================================
# 3. APPEND - Agregar nuevos mensajes sin sobreescribir
# ============================================================================

def add_message(filename: str, message: str) -> None:
    """Agrega un nuevo mensaje al historial sin perder lo anterior."""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(message + '\n')


# ============================================================================
# 4. PATHLIB - Forma moderna de trabajar con rutas
# ============================================================================

def save_with_pathlib(messages: list[str], filepath: Path) -> None:
    """Guarda usando pathlib (más conveniente que strings)."""
    # Crear directorio si no existe
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text('\n'.join(messages), encoding='utf-8')


def load_with_pathlib(filepath: Path) -> list[str]:
    """Carga usando pathlib."""
    return filepath.read_text(encoding='utf-8').strip().split('\n')


# ============================================================================
# EJEMPLO PRÁCTICO
# ============================================================================

if __name__ == "__main__":
    # Usar tempfile para no contaminar el sistema
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        conversation_file = tmpdir / "agent_conversation.txt"
        
        # Simular una conversación con un agente
        messages = [
            "Usuario: ¿Cuál es la capital de Francia?",
            "Agente: La capital de Francia es París.",
            "Usuario: ¿Qué idioma se habla allá?",
            "Agente: El idioma principal es francés.",
        ]
        
        # Guardar conversación inicial
        save_conversation(messages, str(conversation_file))
        
        # Cargar y mostrar
        loaded = load_conversation(str(conversation_file))
        print(f"\n📋 Conversación cargada ({len(loaded)} mensajes):")
        for msg in loaded:
            print(f"  {msg}")
        
        # Agregar nuevo mensaje
        add_message(str(conversation_file), "Usuario: Gracias por la ayuda.")
        print("\n✓ Nuevo mensaje agregado.")
        
        # Cargar versión actualizada
        updated = load_conversation(str(conversation_file))
        print(f"Total de mensajes: {len(updated)}")
