from __future__ import annotations

from collections.abc import Iterator, Mapping
from typing import Any

from pytabify.domain.dt_row import DTRow


class RobotDataRow(Mapping[str, Any]):
    """Adaptador de fila para Robot con acceso por atributo y por llave."""

    def __init__(self, row: DTRow):
        self._row = row

    def __getitem__(self, key: str) -> Any:
        return self._row[key]

    def __getattr__(self, name: str) -> Any:
        return getattr(self._row, name)

    def __iter__(self) -> Iterator[str]:
        return iter(self.keys())

    def __len__(self) -> int:
        return len(self._row)

    @property
    def columns(self) -> list[str]:
        return list(self._row)

    def keys(self):
        return self.columns

    def items(self):
        return [(name, self._row[name]) for name in self._row]

    def values(self):
        return [self._row[name] for name in self._row]

    def to_dict(self) -> dict[str, Any]:
        return self._row.to_dict()
