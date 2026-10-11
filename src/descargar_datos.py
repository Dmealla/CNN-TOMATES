import shutil
from pathlib import Path

import kagglehub

# Carpeta data/ del proyecto, calculada a partir de la ubicación de este archivo
DESTINO = Path(__file__).resolve().parent.parent / "data"

# Descarga el conjunto y devuelve la carpeta donde quedó guardado
ruta_descarga = kagglehub.dataset_download("emmarex/plantdisease")

# Copia las imágenes a data/
shutil.copytree(ruta_descarga, DESTINO, dirs_exist_ok=True)

print("Datos guardados en:", DESTINO)