"""Normalización de formatos del dataset."""

from __future__ import annotations

import pandas as pd

from .config import TEXT_COLUMNS
from .utils import normalizar_texto


def normalize_dataframe(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Replica la normalización base del notebook sobre una copia de trabajo."""
    df_clean = df_raw.copy()
    df_clean = normalize_text_columns(df_clean)
    df_clean = normalize_document_id(df_clean)
    df_clean = normalize_phone(df_clean)
    df_clean = normalize_dates(df_clean)
    df_clean = normalize_age(df_clean)
    df_clean = normalize_title_columns(df_clean)

    return df_clean


def normalize_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza columnas textuales reutilizando un único criterio."""
    df_clean = df.copy()
    for column in TEXT_COLUMNS:
        df_clean[column] = df_clean[column].apply(normalizar_texto)
    return df_clean


def normalize_document_id(df: pd.DataFrame) -> pd.DataFrame:
    """Deja la cédula solo con dígitos."""
    df_clean = df.copy()
    df_clean["Cédula"] = df_clean["Cédula"].astype(str).str.replace(r"\D", "", regex=True)
    return df_clean


def normalize_phone(df: pd.DataFrame) -> pd.DataFrame:
    """Deja el teléfono solo con dígitos."""
    df_clean = df.copy()
    df_clean["Teléfono Contacto"] = df_clean["Teléfono Contacto"].str.replace(r"\D", "", regex=True)
    return df_clean


def normalize_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte fechas inválidas a valores faltantes."""
    df_clean = df.copy()
    df_clean["Fecha Registro"] = pd.to_datetime(df_clean["Fecha Registro"], errors="coerce")
    df_clean["Fecha Actualización"] = pd.to_datetime(df_clean["Fecha Actualización"], errors="coerce")
    return df_clean


def normalize_age(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte edad a valor numérico."""
    df_clean = df.copy()
    df_clean["Edad"] = pd.to_numeric(df_clean["Edad"], errors="coerce")
    return df_clean


def normalize_title_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza capitalización de columnas categóricas del notebook."""
    df_clean = df.copy()
    df_clean["Es Menor"] = df_clean["Es Menor"].str.strip().str.title()
    df_clean["Estado"] = df_clean["Estado"].str.strip().str.title()
    return df_clean
