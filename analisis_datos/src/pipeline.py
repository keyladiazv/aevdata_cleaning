"""Orquestador del pipeline de análisis de datos."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .cleaning import add_clean_name, filter_valid_names
from .config import DEFAULT_INPUT_PATH, DEFAULT_OUTPUT_PATH, PipelineConfig
from .consolidation import consolidate_entities
from .deduplication import deduplicate_by_document_id
from .entities import build_entities
from .export import export_to_excel
from .io import load_raw_data
from .normalization import normalize_dataframe
from .validation import validate_dataframe


def run_pipeline(config: PipelineConfig) -> pd.DataFrame:
    """Ejecuta el flujo completo: carga, limpieza, entidades, consolidación y exportación."""
    df_raw = load_raw_data(config.input_path)
    df_clean = normalize_dataframe(df_raw)
    df_validated = validate_dataframe(df_clean)
    df_entities = add_clean_name(df_validated)
    df_validos = filter_valid_names(df_entities)
    df_deduplicated = deduplicate_by_document_id(df_validos)
    df_entidad = build_entities(df_deduplicated)
    df_final = consolidate_entities(df_entidad)
    export_to_excel(df_final, config.output_path, config.sheet_name)

    return df_final


def parse_args() -> argparse.Namespace:
    """Parsea argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(description="Ejecuta el pipeline de limpieza de datos AEV.")
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Ruta al archivo todos_registros.xlsx.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Ruta del Excel final.",
    )
    parser.add_argument(
        "--sheet-name",
        default="registros_limpios",
        help="Nombre de la hoja del Excel exportado.",
    )
    return parser.parse_args()


def main() -> None:
    """Punto de entrada del pipeline."""
    args = parse_args()
    config = PipelineConfig(input_path=args.input, output_path=args.output, sheet_name=args.sheet_name)
    df_final = run_pipeline(config)
    print(f"Pipeline finalizado. Filas exportadas: {len(df_final)}. Salida: {config.output_path}")


if __name__ == "__main__":
    main()
