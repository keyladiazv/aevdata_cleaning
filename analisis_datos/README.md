# Análisis de datos AEV

Pipeline profesional para limpiar, validar, construir entidades y exportar a Excel el consolidado `todos_registros.xlsx` generado por el scraping.

> Alcance: este módulo trabaja solo dentro de `analisis_datos/`. El scraping es una fuente externa de referencia y no forma parte de este pipeline.

## Ruta rápida

```bash
pip install -r analisis_datos/requirements.txt
python -m analisis_datos.src.pipeline
```

Entrada esperada:

```text
analisis_datos/data_raw/todos_registros.xlsx
```

Salida generada:

```text
analisis_datos/data_limpia/registros_limpios.xlsx
```

También podés indicar rutas explícitas:

```bash
python -m analisis_datos.src.pipeline \
  --input analisis_datos/data_raw/todos_registros.xlsx \
  --output analisis_datos/data_limpia/registros_limpios.xlsx
```

## Flujo del pipeline

```text
Scraping (solo referencia)
↓
Carga
↓
Limpieza
↓
Normalización
↓
Validaciones
↓
Entidades
↓
Deduplicación
↓
Consolidación
↓
Exportación a Excel (.xlsx)
```

El notebook `notebooks/01_exploracion_dataset.ipynb` queda como evidencia del análisis exploratorio y no debe modificarse para ejecutar el pipeline productivo.

## Arquitectura

```text
analisis_datos/
├── AGENT.md
├── README.md
├── RECOMENDACIONES.md
├── requirements.txt
├── data_raw/
│   └── todos_registros.xlsx        # entrada local, no versionada
├── data_limpia/
│   └── registros_limpios.xlsx      # salida local, no versionada
├── notebooks/
│   └── 01_exploracion_dataset.ipynb
└── src/
    ├── config.py
    ├── io.py
    ├── cleaning.py
    ├── normalization.py
    ├── validation.py
    ├── entities.py
    ├── deduplication.py
    ├── consolidation.py
    ├── export.py
    ├── utils.py
    └── pipeline.py
```

## Módulos

| Módulo | Responsabilidad |
|---|---|
| `config.py` | Rutas, columnas esperadas y reglas constantes. |
| `io.py` | Carga del Excel y normalización de nombres de columnas. |
| `normalization.py` | Normalización de texto, cédulas, teléfonos, fechas, edad y categorías. |
| `validation.py` | Reglas de calidad para cédula, teléfono, edad, URL y estado. |
| `cleaning.py` | Limpieza específica de nombres y filtros de calidad. |
| `deduplication.py` | Deduplicación previa por cédula. |
| `entities.py` | Construcción de entidades con union-find. |
| `consolidation.py` | Selección del mejor registro por entidad y separación de nombres múltiples. |
| `export.py` | Exportación final a Excel. |
| `pipeline.py` | Orquestación end-to-end y CLI. |

## Entradas y salidas

| Tipo | Ruta | Descripción |
|---|---|---|
| Entrada | `data_raw/todos_registros.xlsx` | Consolidado original obtenido desde scraping. |
| Salida | `data_limpia/registros_limpios.xlsx` | Dataset limpio, validado, deduplicado y consolidado. |
| Evidencia | `notebooks/01_exploracion_dataset.ipynb` | Notebook exploratorio original; no se modifica. |
| Recomendaciones | `RECOMENDACIONES.md` | Mejoras o riesgos detectados que no se implementan en este alcance. |

## Lógica conservada del notebook

- `df_raw`: datos originales cargados desde Excel.
- `df_clean`: normalización de formatos básicos.
- `df_validated`: invalidación de datos fuera de regla.
- `df_entities`: creación de `Nombre_clean` y preparación para entidades.
- `df_validos`: registros con nombres válidos para consolidación.
- `df_entidad`: grupos de identidad con `entity_id`.
- `df_final`: mejor registro por entidad, con nombres múltiples separados.

## Instalación

Se recomienda usar un entorno virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r analisis_datos/requirements.txt
```

En Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r analisis_datos/requirements.txt
```

## Privacidad

Los archivos Excel de entrada y salida pueden contener datos personales. No deben versionarse.
