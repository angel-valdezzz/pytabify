from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import Any, overload

from pytabify.domain.data_table import DataTable
from pytabify.robot.robot_data_row import RobotDataRow


class RobotDataTable(Sequence[RobotDataRow]):
    """Adaptador de tabla para Robot Framework."""

    def __init__(self, datatable: DataTable):
        self._datatable = datatable

    @overload
    def __getitem__(self, index: int) -> RobotDataRow: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[RobotDataRow]: ...

    def __getitem__(self, index: int | slice) -> RobotDataRow | Sequence[RobotDataRow]:
        rows = [RobotDataRow(row) for row in self._datatable]
        return rows[index]

    def __len__(self) -> int:
        return len(self._datatable)

    def __iter__(self) -> Iterator[RobotDataRow]:
        for row in self._datatable:
            yield RobotDataRow(row)

    @property
    def headers(self) -> list[str]:
        return [header.name for header in self._datatable.headers()]

    def row(self, index: int) -> RobotDataRow:
        return self[index]

    def rows(self) -> list[RobotDataRow]:
        return list(self)

    def to_dict(self) -> list[dict[str, Any]]:
        return self._datatable.to_dict()

    @property
    def datatable(self) -> DataTable:
        return self._datatable
