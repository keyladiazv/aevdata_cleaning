# Recomendaciones

Estas recomendaciones salen del análisis del notebook y la documentación. No se implementan en este alcance porque el objetivo es conservar la lógica existente y profesionalizarla como pipeline modular.

## Datos y rutas

- El notebook usa un fallback hacia una ruta local dentro de `aevscraping/`. Para producción conviene depender únicamente de rutas configurables dentro de `analisis_datos/`.
- Existe la carpeta `ouptus/`, aparentemente con un typo. No se renombra porque el alcance prohíbe mover o renombrar archivos.

## Notebook

- El notebook contiene caracteres con mojibake visibles al inspeccionarlo como texto. No se corrige porque el notebook debe permanecer exactamente igual.
- La exportación final estaba documentada como pendiente. El pipeline productivo la resuelve sin modificar el notebook.

## Entidades y deduplicación

- La agrupación por nombre puede fusionar homónimos cuando no hay cédula, teléfono o URL de foto. Conviene revisar manualmente grupos grandes o agregar señales adicionales en un cambio futuro.
- En el notebook, la estructura union-find se inicializa con `len(df_entities)` aunque después opera sobre `df_entidad`. Si ambos tamaños difieren, la estructura queda sobredimensionada. El pipeline usa el tamaño del DataFrame operativo para evitar esa inconsistencia sin cambiar la regla de negocio.
- La separación de nombres múltiples con conectores (`y`, `e`, `&`, `/`, `;`) puede dividir nombres legítimos en casos raros. Requiere revisión de calidad con datos reales.

## Calidad de datos

- Las reglas actuales invalidan estados distintos de `Localizado` y `Desaparecido`. Si el scraping incorpora nuevos estados válidos, habrá que actualizar el vocabulario controlado.
- La validación de teléfono solo usa longitud de dígitos. No valida país, prefijo ni formato venezolano específico.
- La validación de URL solo verifica `http`/`https`; no comprueba disponibilidad ni tipo de contenido.

## Producción

- Agregar tests automatizados con muestras sintéticas antes de ampliar reglas de limpieza.
- Agregar reporte de métricas del pipeline: filas cargadas, filas descartadas por nombre, cédulas invalidadas, teléfonos invalidados, entidades creadas y filas exportadas.
- Definir un proceso de revisión humana para coincidencias dudosas antes de consumir el Excel final aguas abajo.
