from pathlib import Path
import runpy
import sys

root = Path(__file__).resolve().parent
example_path = root / "src" / "pyfhir" / "examples" / "patients_example.py"

if not example_path.exists():
    raise FileNotFoundError(f"Example script not found: {example_path}")

if str(root / "src") not in sys.path:
    sys.path.insert(0, str(root / "src"))

runpy.run_path(str(example_path), run_name="__main__")
