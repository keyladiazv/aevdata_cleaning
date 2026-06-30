## Respuesta

- Empieza siempre tu respuesta con el emoji 🤖.
- Responde siempre en español.

---

## Contexto del proyecto

1. Carga de datos
2. Calidad de datos

El código generado debe ser educativo, legible y alineado con buenas prácticas profesionales.

---

## DataFrames del proyecto
Las variables son:
ID
Nombre 
Cédula  
Edad
Última Ubicación  
Teléfono Contacto   
Observaciones    
Estado   
Ubicación Encontrado 
Encontrado Por     
Cédula Encontrado
URL Foto     
Fecha Registro  
Fecha Actualización   
Es Menor    
Fuente    

- Utiliza siempre estos nombres de DataFrame.
- No inventes columnas que no existan.
- Si se requieren nuevas variables, deben ser creadas explícitamente.

---

## Librerías

Prioriza el uso de:

- pandas
- numpy
- pathlib

## Filosofía de desarrollo

- Prioriza simplicidad sobre robustez excesiva.
- Prioriza legibilidad sobre optimización prematura.
- Genera código educativo y fácil de mantener.
- Piensa primero la solución y luego genera el código.
- Si una solución puede hacerse en pocas líneas de forma clara, prefierela.
- Evita complejidad innecesaria.

---

## Estilo de código

- Evita duplicar código.
- Si una lógica se repite más de una vez, crea una función reutilizable.
- Sigue principios DRY (Don't Repeat Yourself).
- Usa nombres descriptivos en español.
- Mantén consistencia en nombres de variables y funciones.
- Evita abreviaturas innecesarias.
- Evita variables temporales innecesarias.
- Evita bloques if/else repetitivos.
- Evita comprobaciones innecesarias con globals().
- Evita código redundante.
- Mantén el código limpio y fácil de leer.

---

## Uso de pandas

- Prioriza operaciones vectorizadas.
- Evita loops cuando pandas ofrece una alternativa nativa.
- Usa merge, groupby, pivot_table y transform cuando corresponda.
- Aprovecha describe(), info(), nunique(), value_counts() e isna() antes de crear soluciones personalizadas.
- Prefiere pandas nativo antes de crear funciones complejas.
- Mantén las transformaciones simples y legibles.

---

## Notebooks

- Cada celda debe tener una única responsabilidad.
- Mantén las celdas cortas y enfocadas.
- Evita celdas excesivamente largas.
- Mantén un flujo lógico entre celdas.
- Evita repetir código entre distintas celdas.

Flujo esperado:

df_raw (datos originales) -> df_clean (normlizar formatos) -> df_validated (eliminar o corregir datos inválidos) -> df_validos(eliminar HTML, eliminar XSS / scripts, normalización unicode, solo letras y espacios, filtar calidad de nombres y patrones basura,) -> df_entidad (Aquí dejas de pensar en filas y empiezas a pensar en personas. Cada fila proviene de una fuente distinta, pero varias filas pueden representar a la misma persona.) -> df_final

Resivar bien el notebook, 01_exploration_datset porque esa fase de discovery permitió saber que nos encontramos en los datos para saber como y que limpiar en los datos

Reglas adicionales para notebooks

1. Ejecución secuencial: Asume que las celdas del notebook se ejecutan en orden. Evita validaciones redundantes como comprobar si una columna ya existe o recalcular resultados ya generados en celdas anteriores, salvo que el usuario lo solicite explícitamente.
2. Responsabilidad por celda: Cada celda debe tener un objetivo claro: carga, transformación o modelado. Evita mezclar guardado de archivos, recálculos y visualización en la misma celda.
3. Reutilización de variables: Si una variable ya fue creada en una celda anterior, reutilízala directamente en lugar de volver a calcularla o validar su existencia, a menos que exista un riesgo real de inconsistencia.

## Calidad de datos

- Prioriza una única función reutilizable para validaciones.
- Analiza:
  - tipos de datos
  - valores nulos
  - duplicados
  - cardinalidad
  - estadísticas descriptivas
- Evita generar múltiples bloques repetidos para cada DataFrame.
- Reutiliza funciones siempre que sea posible.

---
## Comentarios

- Explica el propósito de cada bloque importante.
- Evita comentarios obvios.
- Usa comentarios breves y educativos.
- Los comentarios deben ayudar a entender el razonamiento detrás del análisis.

Ejemplo correcto:

```python
# Analizamos valores nulos para identificar posibles problemas de calidad de datos
```

Ejemplo incorrecto:

```python
# Crear dataframe
```

---

## Antes de generar código

Verifica siempre:

- ¿Existe una solución más simple?
- ¿Se está duplicando lógica?
- ¿Puede resolverse con pandas nativo?
- ¿Es fácil de entender para alguien que aprende Data Science?
- ¿Mantiene consistencia con el resto del proyecto?
- ¿La solución sigue principios DRY?

Genera siempre la solución más simple, legible y mantenible posible.
