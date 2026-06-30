"""Construcción de entidades/personas a partir de registros."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .utils import similitud


class UnionFind:
    """Estructura simple para agrupar filas que representan la misma entidad."""

    def __init__(self, size: int) -> None:
        self.parent = np.arange(size)

    def find(self, value: int) -> int:
        """Busca la raíz de un grupo."""
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = int(self.parent[value])
        return int(value)

    def union(self, left: int, right: int) -> None:
        """Une dos grupos si aún no comparten raíz."""
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def build_entities(df_validos: pd.DataFrame) -> pd.DataFrame:
    """Construye entity_id conservando las reglas del notebook."""
    df_entidad = df_validos.copy()
    df_entidad["fila_id"] = np.arange(len(df_entidad))

    union_find = UnionFind(len(df_entidad))
    union_by_column(df_entidad, union_find, "Cédula")
    union_by_column(df_entidad, union_find, "Teléfono Contacto")
    union_by_column(df_entidad, union_find, "URL Foto")
    union_by_similarity(df_entidad, union_find)

    df_entidad["entity_id"] = [union_find.find(i) for i in df_entidad["fila_id"]]
    df_entidad["entity_id"] = pd.factorize(df_entidad["entity_id"])[0]

    return df_entidad


def union_by_column(df_entidad: pd.DataFrame, union_find: UnionFind, column: str) -> None:
    """Une filas que comparten un identificador fuerte."""
    for _, group in df_entidad[df_entidad[column].notna()].groupby(column):
        row_ids = group["fila_id"].to_numpy()
        for index in range(1, len(row_ids)):
            union_find.union(int(row_ids[0]), int(row_ids[index]))


def union_by_similarity(df_entidad: pd.DataFrame, union_find: UnionFind) -> None:
    """Une filas con el mismo Nombre_clean si superan el score mínimo."""
    for _, group in df_entidad.groupby("Nombre_clean"):
        if len(group) < 2:
            continue

        rows = group.to_dict("records")
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                score = calculate_similarity_score(rows[i], rows[j])
                if score >= 40:
                    union_find.union(int(rows[i]["fila_id"]), int(rows[j]["fila_id"]))


def calculate_similarity_score(left: dict, right: dict) -> int:
    """Calcula el score de similitud definido en el notebook."""
    score = 0

    if pd.notna(left["Cédula"]) and left["Cédula"] == right["Cédula"]:
        score += 100

    if pd.notna(left["Teléfono Contacto"]) and left["Teléfono Contacto"] == right["Teléfono Contacto"]:
        score += 100

    left_age = left["Edad"]
    right_age = right["Edad"]
    if pd.notna(left_age) and pd.notna(right_age):
        if abs(left_age - right_age) <= 2:
            score += 20
    else:
        score += 10

    if similitud(left["Última Ubicación"], right["Última Ubicación"]) >= 0.60:
        score += 30

    if left["Estado"] == right["Estado"]:
        score += 5

    return score
