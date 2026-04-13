from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from pytabify.domain.dt_header import DTHeader
from pytabify.domain.dt_row import DTRow


class DataTable:
    """Representa un conjunto de filas y columnas con esquema canonico estable."""

    def __init__(self, rows: list[DTRow] | None = None, schema: list[str] | None = None) -> None:
        self._schema: list[str] = [str(name) for name in (schema or [])]
        self._rows: list[DTRow] = rows or []
        self._sync_rows()

    @classmethod
    def from_records(cls, records: list[dict[str, Any]], schema: list[str]) -> DataTable:
        rows = [DTRow(record, index=row_index) for row_index, record in enumerate(records)]
        return cls(rows=rows, schema=schema)

    def __len__(self) -> int:
        return len(self._rows)

    def row(self, index: int) -> DTRow:
        return self._rows[index]

    def total_rows(self) -> int:
        return len(self._rows)

    def __getitem__(self, index: int) -> DTRow:
        return self._rows[index]

    def __iter__(self) -> Iterator[DTRow]:
        return iter(self._rows)

    @property
    def column_names(self) -> tuple[str, ...]:
        return tuple(self._schema)

    def headers(self) -> list[DTHeader]:
        return [DTHeader(field_name, index) for index, field_name in enumerate(self._schema)]

    def to_dict(self) -> list[dict[str, Any]]:
        return [row.to_dict() for row in self._rows]

    def set_value(self, row_index: int, column_name: str, value: Any) -> None:
        normalized_name = str(column_name)
        if normalized_name not in self._schema:
            self._schema.append(normalized_name)

        self._sync_rows()
        self._rows[row_index]._set_local_value(normalized_name, value)
        self._sync_rows()

    def _sync_rows(self) -> None:
        for row_index, row in enumerate(self._rows):
            row.bind(self, row_index)
