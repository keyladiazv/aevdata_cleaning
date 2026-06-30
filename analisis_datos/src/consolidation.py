"""Consolidación final de entidades."""

from __future__ import annotations

import re

import pandas as pd


def consolidate_entities(df_entidad: pd.DataFrame) -> pd.DataFrame:
    """Selecciona el mejor registro por entidad y separa nombres múltiples."""
    df_scored = add_priority_score(df_entidad)
    df_final = select_best_record_by_entity(df_scored)
    df_final = split_multiple_people(df_final)
    return df_final


def add_priority_score(df_entidad: pd.DataFrame) -> pd.DataFrame:
    """Agrega score de prioridad según la lógica del notebook."""
    df_scored = df_entidad.copy()
    df_scored["score"] = (
        (df_scored["Estado"].eq("Localizado").astype(int) * 1000)
        + (df_scored["Cédula"].notna().astype(int) * 100)
        + (df_scored["Teléfono Contacto"].notna().astype(int) * 50)
        + (df_scored["URL Foto"].notna().astype(int) * 20)
        + (df_scored["Edad"].notna().astype(int) * 10)
    )
    return df_scored


def select_best_record_by_entity(df_entidad: pd.DataFrame) -> pd.DataFrame:
    """Conserva la mejor fila de cada entity_id."""
    sorted_entities = df_entidad.sort_values(
        ["entity_id", "score", "Fecha Actualización"],
        ascending=[True, False, False],
    )
    return sorted_entities.drop_duplicates(subset="entity_id", keep="first").reset_index(drop=True)


def separar_personas(nombre: object) -> list[str]:
    """Separa nombres múltiples con los separadores usados en el notebook."""
    if pd.isna(nombre):
        return []

    clean_name = str(nombre).strip()
    pattern = r"\s+(?:y|e|&|/)\s+|;"
    return [person.strip() for person in re.split(pattern, clean_name) if person.strip()]


def split_multiple_people(df_final: pd.DataFrame) -> pd.DataFrame:
    """Expande filas cuando Nombre_clean contiene varias personas."""
    new_rows = []

    for _, row in df_final.iterrows():
        people = separar_personas(row["Nombre_clean"])
        if len(people) <= 1:
            new_rows.append(row.copy())
            continue

        for person in people:
            new_row = row.copy()
            new_row["Nombre_clean"] = person
            new_row["Nombre"] = person
            new_rows.append(new_row)

    return pd.DataFrame(new_rows).reset_index(drop=True)
