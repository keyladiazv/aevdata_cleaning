# Limpieza de datos AEV

Este repositorio contiene la parte de análisis y limpieza de datos ubicada en `analisis_datos/`. El objetivo es tomar el archivo consolidado original del scraping, trabajar sobre una copia y generar una versión limpia en Excel para pasos posteriores del pipeline.

> Por privacidad y trazabilidad, este repositorio no versiona el scraping externo ni archivos `.xlsx`, `.csv` o similares.

## Gobernanza del fork Open-Vzla-SOS

Este repositorio es un **fork operativo mantenido por Open-Vzla-SOS**.

- Repositorio original upstream: [`keyladiazv/aevdata_cleaning`](https://github.com/keyladiazv/aevdata_cleaning).
- Función dentro del ecosistema: limpieza, normalización, deduplicación y control de calidad.
- La rama `main` se reserva para sincronización con upstream.
- La rama `develop` es la rama de integración de Open-Vzla-SOS.
- Todo cambio propio debe realizarse en ramas `feature/*`, `fix/*`, `docs/*`, `test/*` o `chore/*`.
- Los cambios propios deben llegar a `develop` mediante pull request.
- No deben ejecutarse scrapers, notebooks o procesos que utilicen datos reales, llamen servicios externos, escriban en APIs o afecten ambientes de producción sin autorización explícita. Las pruebas locales y aisladas deberán utilizar datos ficticios o anonimizados.
- Se identificaron riesgos heredados del upstream que deberán gestionarse mediante tareas separadas por los responsables correspondientes; su remediación queda fuera de este cambio.

## Ruta rápida

1. Cloná este repositorio.
2. Instalá las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Conseguí el archivo `todos_registros.xlsx` desde la fuente original de scraping usada para el análisis: [`Amilkir/aevscraping`](https://github.com/Amilkir/aevscraping).
4. Copialo en:

   ```text
   analisis_datos/data_raw/todos_registros.xlsx
   ```

5. Ejecutá el notebook:

   ```text
   analisis_datos/notebooks/01_exploracion_dataset.ipynb
   ```

6. Revisá los resultados de validación dentro del notebook. La exportación final a Excel queda pendiente hasta validar la limpieza.

## Qué hace la limpieza

| Área | Decisión |
|------|----------|
| Datos originales | Se cargan en `df_raw` y no se modifican. |
| Datos de trabajo | Se usa `df_clean = df_raw.copy()`. |
| Cédula | Se crea `Cédula_clean` solo para cédulas de 7 u 8 dígitos válidos, excluyendo valores repetidos como `11111111`. |
| Nombre | Se crea `Nombre_clean`, eliminando HTML, patrones sospechosos y caracteres no informativos. |
| Duplicados por nombre | Se consolida por `Nombre_clean`, priorizando localizado/encontrado, cédula, teléfono, más campos informativos y fechas recientes. |
| Datos complementarios | Si la mejor fila no tiene un dato, se completa con el primer dato válido disponible entre sus duplicados. |
| Exportación | Pendiente: todavía no se genera Excel final porque la limpieza sigue en revisión. |

## Por qué no se sube `aevscraping` ni el Excel

La carpeta `aevscraping` proviene de otro repositorio y se usa solo como fuente local. Además, `todos_registros.xlsx` puede contener datos personales como nombres, cédulas y teléfonos. Por eso se deja fuera del control de versiones.

La persona que ejecute este proyecto debe obtener el archivo fuente por separado y ubicarlo en `analisis_datos/data_raw/`.

## Estructura

```text
.
├── analisis_datos/
│   ├── AGENT.md
│   ├── README.md
│   ├── data_raw/
│   │   └── .gitkeep
│   ├── data_limpia/
│   │   └── .gitkeep
│   └── notebooks/
│       └── 01_exploracion_dataset.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```
