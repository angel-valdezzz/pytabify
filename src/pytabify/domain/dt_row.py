from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any

from pytabify.domain.dt_field import DTField

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
        self._fields: dict[str, DTField] = {}
        self._index: int = index
        self._table: DataTable | None = table

        for field_index, (name, value) in enumerate((values or {}).items()):
            self._fields[str(name)] = DTField(str(name), value, field_index)

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

    def __getitem__(self, name: str) -> DTField:
        field_name = str(name)
        if field_name not in self._fields:
            raise KeyError(f"Column '{field_name}' does not exist in row {self._index}.")
        return self._fields[field_name]

    def __getattr__(self, name: str) -> DTField:
        try:
            return self.__getitem__(name)
        except KeyError as exc:
            raise AttributeError(f"Column '{name}' does not exist in row {self._index}.") from exc

    def __len__(self) -> int:
        return len(self._fields)

    def total_fields(self) -> int:
        return len(self._fields)

    def to_dict(self) -> dict[str, Any]:
        return {field.name: field.value for field in self}

    def __iter__(self) -> Iterator[DTField]:
        for field_name in self._ordered_field_names():
            yield self._fields[field_name]

    def bind(self, table: DataTable, index: int) -> None:
        super().__setattr__("_table", table)
        super().__setattr__("_index", index)
        self.sync_with_schema(table.column_names)

    def sync_with_schema(self, schema: list[str] | tuple[str, ...]) -> None:
        for field_index, field_name in enumerate(schema):
            if field_name not in self._fields:
                self._fields[field_name] = DTField(field_name, None, field_index)
            else:
                self._fields[field_name].set_index(field_index)

        stale_fields = [field_name for field_name in self._fields if field_name not in schema]
        for field_name in stale_fields:
            del self._fields[field_name]

    def _set_local_value(self, name: str, value: Any) -> None:
        if name in self._fields:
            self._fields[name].set_value(value)
            return

        self._fields[name] = DTField(name, value, len(self._fields))

    def _ordered_field_names(self) -> list[str]:
        if self._table is not None:
            return list(self._table.column_names)
        return list(self._fields.keys())
