"""Deduplicación previa por cédula."""

from __future__ import annotations

import pandas as pd


def select_record_index(group: pd.DataFrame) -> int:
    """Selecciona el registro a conservar para una cédula duplicada."""
    localized = group[group["Estado"] == "Localizado"]
    if not localized.empty:
        return int(localized.index[0])

    if (group["Estado"] == "Desaparecido").all():
        with_phone = group[group["Teléfono Contacto"].notna()]
        if not with_phone.empty:
            return int(with_phone.index[0])

    return int(group.index[0])


def deduplicate_by_document_id(df_validos: pd.DataFrame) -> pd.DataFrame:
    """Deduplica cédulas según prioridad del notebook."""
    indices_to_keep = (
        df_validos[df_validos["Cédula"].notna()]
        .groupby("Cédula", group_keys=False)
        .apply(select_record_index)
    )

    unique_indices = df_validos[
        df_validos["Cédula"].isna() | ~df_validos["Cédula"].duplicated(keep=False)
    ].index

    return (
        df_validos.loc[unique_indices.union(indices_to_keep)]
        .sort_index()
        .reset_index(drop=True)
    )
