import shutil
from pathlib import Path

PROYECTO = Path(__file__).resolve().parent.parent
ORIGEN = PROYECTO / "data" / "PlantVillage"
DESTINO = PROYECTO / "data" / "tomate"

for carpeta in ORIGEN.iterdir():
    if carpeta.name.startswith("Tomato"):
        shutil.copytree(carpeta, DESTINO / carpeta.name, dirs_exist_ok=True)
        print("Copiada:", carpeta.name)