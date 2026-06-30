"""Utilidades compartidas del pipeline."""

from __future__ import annotations

import re
import unicodedata
from difflib import SequenceMatcher
from typing import Any

import pandas as pd


def quitar_acentos(texto: Any) -> str | pd._libs.missing.NAType:
    """Quita acentos preservando valores faltantes."""
    if pd.isna(texto):
        return pd.NA

    return "".join(
        caracter
        for caracter in unicodedata.normalize("NFKD", str(texto))
        if not unicodedata.combining(caracter)
    )


def normalizar_texto(texto: Any) -> str | pd._libs.missing.NAType:
    """Normaliza texto con el mismo criterio usado en el notebook."""
    if pd.isna(texto):
        return pd.NA

    texto_normalizado = str(texto)
    texto_normalizado = quitar_acentos(texto_normalizado)
    texto_normalizado = texto_normalizado.strip()
    texto_normalizado = re.sub(r"\s+", " ", texto_normalizado)

    return texto_normalizado


def similitud(texto_a: Any, texto_b: Any) -> float:
    """Calcula similitud simple entre dos textos."""
    if pd.isna(texto_a) or pd.isna(texto_b):
        return 0.0

    return SequenceMatcher(None, str(texto_a).lower(), str(texto_b).lower()).ratio()
