"""
Manejo de JSON - Configuración de agentes de IA.
Contexto: Los agentes LangChain almacenan configuración, memoria, y embeddings en JSON.
"""

import json
import tempfile
from pathlib import Path

# ============================================================================
# 1. GUARDAR CONFIGURACIÓN DE AGENTE
# ============================================================================

def save_agent_config(config: dict, filename: str) -> None:
    """Guarda la configuración de un agente en JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"✓ Configuración guardada en {filename}")


# ============================================================================
# 2. CARGAR CONFIGURACIÓN DE AGENTE
# ============================================================================

def load_agent_config(filename: str) -> dict:
    """Carga la configuración de un agente desde JSON."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# ============================================================================
# 3. MODIFICAR CONFIGURACIÓN (Lectura → Modificación → Escritura)
# ============================================================================

def update_agent_temperature(filename: str, new_temperature: float) -> None:
    """Carga config, modifica temperature, y guarda."""
    config = load_agent_config(filename)
    config['model_params']['temperature'] = new_temperature
    save_agent_config(config, filename)
    print(f"✓ Temperature actualizada a {new_temperature}")


# ============================================================================
# 4. TRABAJAR CON MEMORIA DE AGENTE (nested JSON)
# ============================================================================

def add_memory_to_agent(filename: str, memory_key: str, memory_value: str) -> None:
    """Agrega una entrada a la memoria del agente."""
    config = load_agent_config(filename)
    
    if 'memory' not in config:
        config['memory'] = {}
    
    config['memory'][memory_key] = memory_value
    save_agent_config(config, filename)


def get_agent_memory(filename: str) -> dict:
    """Obtiene toda la memoria del agente."""
    config = load_agent_config(filename)
    return config.get('memory', {})


# ============================================================================
# 5. VALIDACIÓN CON try/except
# ============================================================================

def load_config_safe(filename: str) -> dict:
    """Carga config con manejo de errores."""
    try:
        return load_agent_config(filename)
    except FileNotFoundError:
        print(f"⚠ Archivo no encontrado: {filename}. Usando configuración por defecto.")
        return get_default_config()
    except json.JSONDecodeError:
        print(f"⚠ JSON inválido en {filename}. Usando configuración por defecto.")
        return get_default_config()


def get_default_config() -> dict:
    """Retorna configuración por defecto de un agente."""
    return {
        "name": "AgentePor defecto",
        "model": "gpt-4",
        "model_params": {
            "temperature": 0.7,
            "max_tokens": 2000,
        },
        "memory": {},
        "tools": [],
    }


# ============================================================================
# EJEMPLO PRÁCTICO
# ============================================================================

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        config_file = Path(tmpdir) / "agent_config.json"
        
        # Configuración inicial de agente
        agent_config = {
            "name": "Asistente de Documentación",
            "model": "gpt-4",
            "model_params": {
                "temperature": 0.7,
                "max_tokens": 2000,
                "top_p": 0.95,
            },
            "tools": ["search_documents", "summarize", "qa"],
            "memory": {}
        }
        
        # Guardar configuración
        save_agent_config(agent_config, str(config_file))
        
        # Cargar y mostrar
        loaded_config = load_agent_config(str(config_file))
        print("\n⚙️ Configuración del agente:")
        print(f"  Nombre: {loaded_config['name']}")
        print(f"  Modelo: {loaded_config['model']}")
        print(f"  Temperature: {loaded_config['model_params']['temperature']}")
        print(f"  Herramientas: {', '.join(loaded_config['tools'])}")
        
        # Actualizar temperature
        update_agent_temperature(str(config_file), 0.3)
        
        # Agregar memoria
        add_memory_to_agent(str(config_file), "context_length", "8192")
        add_memory_to_agent(str(config_file), "last_user", "Juan")
        
        # Mostrar memoria
        memory = get_agent_memory(str(config_file))
        print("\n💾 Memoria del agente:")
        for key, value in memory.items():
            print(f"  {key}: {value}")
        
        # Cargar versión actualizada
        updated = load_agent_config(str(config_file))
        print(f"\n✓ Temperature actualizado: {updated['model_params']['temperature']}")
