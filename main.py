"""Entry point — ejecuta el panel de progreso."""
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    subprocess.run([sys.executable, str(Path(__file__).parent / "practice.py")] + sys.argv[1:])
