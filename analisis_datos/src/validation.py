"""Validaciones de calidad de datos."""

from __future__ import annotations

import pandas as pd

from .config import VALIDATED_TEXT_COLUMNS, VALID_STATES


def validate_dataframe(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Aplica las reglas de validación del notebook."""
    df_validated = df_clean.copy()
    df_validated = validate_document_id(df_validated)
    df_validated = validate_phone(df_validated)
    df_validated = validate_age(df_validated)
    df_validated = validate_photo_url(df_validated)
    df_validated = validate_state(df_validated)
    df_validated = cast_text_columns(df_validated)

    return df_validated


def validate_document_id(df: pd.DataFrame) -> pd.DataFrame:
    """Invalida cédulas que no tengan 7 u 8 dígitos."""
    df_validated = df.copy()
    mask = df_validated["Cédula"].str.fullmatch(r"\d{7,8}", na=False)
    df_validated.loc[~mask, "Cédula"] = pd.NA
    return df_validated


def validate_phone(df: pd.DataFrame) -> pd.DataFrame:
    """Invalida teléfonos fuera del rango de 10 a 15 dígitos."""
    df_validated = df.copy()
    mask = df_validated["Teléfono Contacto"].str.fullmatch(r"\d{10,15}", na=False)
    df_validated.loc[~mask, "Teléfono Contacto"] = pd.NA
    return df_validated


def validate_age(df: pd.DataFrame) -> pd.DataFrame:
    """Invalida edades fuera del rango humano definido por el notebook."""
    df_validated = df.copy()
    mask = df_validated["Edad"].between(0, 110)
    df_validated.loc[~mask, "Edad"] = pd.NA
    return df_validated


def validate_photo_url(df: pd.DataFrame) -> pd.DataFrame:
    """Invalida URLs que no comiencen con http o https."""
    df_validated = df.copy()
    mask = df_validated["URL Foto"].str.match(r"^https?://", na=False)
    df_validated.loc[~mask, "URL Foto"] = pd.NA
    return df_validated


def validate_state(df: pd.DataFrame) -> pd.DataFrame:
    """Invalida estados fuera del vocabulario esperado."""
    df_validated = df.copy()
    mask = df_validated["Estado"].isin(VALID_STATES)
    df_validated.loc[~mask, "Estado"] = pd.NA
    return df_validated


def cast_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte columnas textuales a string nullable de pandas."""
    df_validated = df.copy()
    df_validated[VALIDATED_TEXT_COLUMNS] = df_validated[VALIDATED_TEXT_COLUMNS].astype("string")
    return df_validated
