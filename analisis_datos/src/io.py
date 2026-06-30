"""Entrada de datos del pipeline."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .config import COLUMN_ALIASES, RAW_COLUMNS


def load_raw_data(input_path: Path) -> pd.DataFrame:
    """Carga el Excel fuente sin modificar el archivo original."""
    if not input_path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de entrada: {input_path}. "
            "Colocá todos_registros.xlsx en analisis_datos/data_raw/."
        )

    df_raw = pd.read_excel(input_path)
    return normalize_column_names(df_raw)


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Unifica nombres de columnas esperados por el análisis."""
    df_normalized = df.rename(columns=COLUMN_ALIASES).copy()
    missing_columns = [column for column in RAW_COLUMNS if column not in df_normalized.columns]

    if missing_columns:
        raise ValueError(f"Faltan columnas obligatorias: {missing_columns}")

    return df_normalized
