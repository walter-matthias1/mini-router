import csv
import sys

def normalize_row(row: dict[str, str]) -> dict[str, str]:
    return {k.strip(): v.strip() for k, v in row.items()}

def drop_empty(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [r for r in rows if any(r.values())]

