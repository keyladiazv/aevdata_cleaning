"""Limpieza específica de nombres para construir entidades."""

from __future__ import annotations

import re
import unicodedata
from typing import Any

import pandas as pd

from .config import NAME_TRASH_PATTERNS


def limpiar_nombre(texto: Any) -> str | pd._libs.missing.NAType:
    """Limpia nombres replicando la lógica del notebook."""
    if pd.isna(texto):
        return pd.NA

    nombre = str(texto)
    nombre = re.sub(r"<.*?>", "", nombre)
    nombre = re.sub(r"(?i)(on\w+=|javascript:|script)", "", nombre)
    nombre = unicodedata.normalize("NFKD", nombre)
    nombre = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", "", nombre)
    nombre = re.sub(r"\s+", " ", nombre).strip()

    return nombre if nombre != "" else pd.NA


def add_clean_name(df: pd.DataFrame) -> pd.DataFrame:
    """Crea Nombre_clean para la etapa de entidades."""
    df_entities = df.copy()
    df_entities["Nombre_clean"] = df_entities["Nombre"].apply(limpiar_nombre)
    return df_entities


def filter_valid_names(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra nombres vacíos, demasiado cortos o patrones basura."""
    df_validos = df[df["Nombre_clean"].notna()].copy()
    df_validos = df_validos[df_validos["Nombre_clean"].str.len() > 3]
    df_validos = df_validos[~df_validos["Nombre_clean"].str.lower().isin(NAME_TRASH_PATTERNS)]
    df_validos = df_validos[
        df_validos["Nombre_clean"].str.contains(r"^[A-Za-záéíóúÁÉÍÓÚñÑ ]{4,}$", regex=True)
    ]
    return df_validos
