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

4. Revisá los resultados de validación dentro del notebook. La exportación final a Excel queda pendiente hasta validar la limpieza.

## Criterio principal de duplicados

Los duplicados por `Nombre_clean` se reducen consolidando información. Primero se ordenan los registros por prioridad de evidencia:

1. localizado/encontrado;
2. cédula válida;
3. teléfono válido;
4. mayor cantidad de campos informativos;
5. fechas más recientes.

Luego se toma el primer dato válido por columna dentro del grupo. Así no se pierde información cuando la ubicación, la cédula y el teléfono están repartidos entre distintas filas duplicadas.

## Estado de exportación

La exportación a `data_limpia/registros_limpios.xlsx` está planificada, pero todavía no se ejecuta desde el notebook porque la limpieza sigue en revisión.

## Nota de privacidad

Los archivos de datos no se versionan. La carpeta conserva solo `.gitkeep` para indicar dónde colocar entradas y salidas.
