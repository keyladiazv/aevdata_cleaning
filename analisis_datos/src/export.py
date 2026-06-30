"""Exportación de resultados limpios."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def export_to_excel(df_final: pd.DataFrame, output_path: Path, sheet_name: str = "registros_limpios") -> Path:
    """Exporta el resultado final a Excel."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_final.to_excel(output_path, index=False, sheet_name=sheet_name)
    return output_path
