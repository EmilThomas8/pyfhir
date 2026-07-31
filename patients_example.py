from pathlib import Path
import runpy

example_path = Path(__file__).resolve().parent / "pyfhir" / "examples" / "patients_example.py"
runpy.run_path(str(example_path), run_name="__main__")
