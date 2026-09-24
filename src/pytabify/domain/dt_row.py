from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pytabify.domain.data_table import DataTable


class DTRow:
    """Representa una fila con acceso por indice logico o por atributo."""

    def __init__(
        self,
        values: dict[str, Any] | None = None,
        index: int = 0,
        table: DataTable | None = None,
    ) -> None:
        self._values: dict[str, Any] = {}
        self._index: int = index
        self._table: DataTable | None = table

        for name, value in (values or {}).items():
            self._values[str(name)] = value

    def __setitem__(self, name: str, value: Any) -> None:
        if self._table is not None:
            self._table.set_value(self._index, str(name), value)
            return

        self._set_local_value(str(name), value)

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            super().__setattr__(name, value)
            return

        self.__setitem__(name, value)

    def __getitem__(self, name: str) -> Any:
        field_name = str(name)
        if field_name not in self._values:
            raise KeyError(f"Column '{field_name}' does not exist in row {self._index}.")
        return self._values[field_name]

    def __getattr__(self, name: str) -> Any:
        try:
            return self.__getitem__(name)
        except KeyError as exc:
            raise AttributeError(f"Column '{name}' does not exist in row {self._index}.") from exc

    def __len__(self) -> int:
        return len(self._values)

    def total_fields(self) -> int:
        return len(self._values)

    def to_dict(self) -> dict[str, Any]:
        return {name: self._values[name] for name in self}

    def __iter__(self) -> Iterator[str]:
        return iter(self._ordered_field_names())

    def bind(self, table: DataTable, index: int) -> None:
        super().__setattr__("_table", table)
        super().__setattr__("_index", index)
        self.sync_with_schema(table.column_names)

    def sync_with_schema(self, schema: list[str] | tuple[str, ...]) -> None:
        self._values = {name: self._values.get(name) for name in schema}

    def _set_local_value(self, name: str, value: Any) -> None:
        self._values[name] = value

    def _ordered_field_names(self) -> list[str]:
        if self._table is not None:
            return list(self._table.column_names)
        return list(self._values)
