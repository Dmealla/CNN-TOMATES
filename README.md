# Detección de enfermedades en hojas de tomate

Proyecto de ciencia de datos que clasifica fotos de hojas de tomate para detectar
si la planta está sana o qué enfermedad tiene (10 clases).
Compara un modelo clásico de machine learning con una red neuronal convolucional (CNN).

Datos: conjunto PlantVillage, solo las 16.011 fotos de tomate.

## Resultados

| Modelo | Exactitud en prueba |
|---|---|
| Random Forest (6 características de color) | 0,72 |
| CNN en PyTorch (2 capas de convolución) | 0,91 |

La CNN mejora sobre todo en las enfermedades que se parecen en el color pero no en la forma
de las manchas: el recall del tizón temprano pasó de 0,34 a 0,78. Solo 2 de 1.444 hojas
enfermas de la prueba fueron clasificadas como sanas.

## Contenido

| Archivo | Qué hace |
|---|---|
| `notebooks/01_exploracion.ipynb` | Exploración de las fotos y cantidad por clase |
| `notebooks/02_modelo_clasico.ipynb` | Características de color, Random Forest y comparación de modelos clásicos |
| `notebooks/03_redes_neuronales.ipynb` | Una neurona a mano y filtros de convolución |
| `notebooks/04_cnn.ipynb` | Entrenamiento y evaluación de la CNN |
| `src/descargar_datos.py` | Descarga PlantVillage desde Kaggle a `data/` |
| `src/preparar_datos.py` | Copia solo las clases de tomate a `data/tomate/` |
| `modelos/red_tomate.pt` | Pesos de la CNN entrenada |

## Cómo ejecutarlo

Desde la carpeta del proyecto, en Windows:

```bash
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python src\descargar_datos.py
.venv\Scripts\python src\preparar_datos.py
```

Después abrir los notebooks en orden, con el kernel del entorno `.venv`.

El entrenamiento de la CNN tarda alrededor de una hora en CPU. Para usar la red sin
entrenar, cargar los pesos guardados como muestra la última sección del notebook 04.

| `notebooks/05_demo.ipynb` 
| Demostración: carga la red guardada y abre una aplicación para clasificar fotos |
## Demostración

Ejecutar todas las celdas de `notebooks/05_demo.ipynb` (no entrena nada, tarda segundos)
y abrir `http://127.0.0.1:7860` en el navegador. Se puede subir una foto o elegir una de
las fotos de ejemplo, que son de la prueba y la red nunca vio.

El modelo se entrenó con fotos de laboratorio: con fotos de campo puede equivocarse,
incluso mostrando 100% de seguridad.