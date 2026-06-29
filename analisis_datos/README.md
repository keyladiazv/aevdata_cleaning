# Análisis de datos

Esta carpeta contiene el notebook de exploración y limpieza de datos para el consolidado original de AEV.

## Cómo ejecutar

1. Instalá dependencias desde la raíz del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

2. Colocá el archivo fuente en:

   ```text
   analisis_datos/data_raw/todos_registros.xlsx
   ```

3. Ejecutá en orden:

   ```text
   notebooks/01_exploracion_dataset.ipynb
   ```

4. Revisá los resultados de validación y construcción de entidades dentro del notebook. La exportación final a Excel queda pendiente hasta validar la limpieza.

## Flujo del notebook

El notebook mantiene un flujo progresivo para no mezclar responsabilidades:

```text
df_raw -> df_clean -> df_validated -> df_entities
```

- `df_raw`: datos originales cargados desde Excel.
- `df_clean`: normalización de texto, acentos, espacios, teléfonos, cédulas, fechas y tipos básicos.
- `df_validated`: invalidación de valores fuera de regla, como cédulas, teléfonos, edades, URLs y estados no válidos.
- `df_entities`: agrupación de registros que probablemente representan a la misma persona.

## Criterio de entidades

`df_entities` deja de pensar en filas aisladas y construye grupos de identidad.

La lógica une registros mediante:

1. `Cédula`, como clave fuerte.
2. `Teléfono Contacto`, como clave fuerte.
3. `Nombre` + `Edad` + `Última Ubicación`, como clave débil combinada.

No se usa `Nombre` por sí solo porque puede fusionar personas distintas con nombres iguales.

## Estado de exportación

La exportación a `data_limpia/registros_limpios.xlsx` está planificada, pero todavía no se ejecuta desde el notebook porque la limpieza sigue en revisión.

## Nota de privacidad

Los archivos de datos no se versionan. La carpeta conserva solo `.gitkeep` para indicar dónde colocar entradas y salidas.
