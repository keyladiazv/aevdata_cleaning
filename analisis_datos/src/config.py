"""Configuración central del pipeline de análisis de datos."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data_raw" / "todos_registros.xlsx"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data_limpia" / "registros_limpios.xlsx"

RAW_COLUMNS = [
    "ID",
    "Nombre",
    "Cédula",
    "Edad",
    "Última Ubicación",
    "Teléfono Contacto",
    "Observaciones",
    "Estado",
    "Ubicación Encontrado",
    "Encontrado Por",
    "Cédula Encontrado",
    "URL Foto",
    "Fecha Registro",
    "Fecha Actualización",
    "Es Menor",
    "Fuente",
]

TEXT_COLUMNS = [
    "Nombre",
    "Última Ubicación",
    "Teléfono Contacto",
    "Observaciones",
    "Estado",
    "Ubicación Encontrado",
    "Encontrado Por",
    "URL Foto",
    "Fuente",
]

VALIDATED_TEXT_COLUMNS = [
    "Nombre",
    "Cédula",
    "Última Ubicación",
    "Teléfono Contacto",
    "Observaciones",
    "Estado",
    "Ubicación Encontrado",
    "Encontrado Por",
    "URL Foto",
    "Es Menor",
    "Fuente",
]

VALID_STATES = {"Localizado", "Desaparecido"}
NAME_TRASH_PATTERNS = {"nn", "na", "ll", "j", "a", "d", "l", "yo"}

COLUMN_ALIASES = {
    "C�dula": "Cédula",
    "�ltima Ubicaci�n": "Última Ubicación",
    "Tel�fono Contacto": "Teléfono Contacto",
    "Ubicaci�n Encontrado": "Ubicación Encontrado",
    "C�dula Encontrado": "Cédula Encontrado",
    "Fecha Actualizaci�n": "Fecha Actualización",
}


@dataclass(frozen=True)
class PipelineConfig:
    """Rutas de entrada y salida del pipeline."""

    input_path: Path = DEFAULT_INPUT_PATH
    output_path: Path = DEFAULT_OUTPUT_PATH
    sheet_name: str = "registros_limpios"
