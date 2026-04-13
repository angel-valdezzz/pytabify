from __future__ import annotations

from abc import ABC, abstractmethod

from pytabify.domain.data_table import DataTable


class TableWriter(ABC):
    @abstractmethod
    def write(self, datatable: DataTable, path: str, encoding: str = "utf-8") -> None:
        """Persiste una tabla en una salida externa."""
