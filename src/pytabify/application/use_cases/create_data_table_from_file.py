from __future__ import annotations

from typing import Any

from pytabify.application.ports.reader_resolver import ReaderResolver
from pytabify.application.use_cases.create_data_table_from_records import CreateDataTableFromRecords
from pytabify.domain.data_table import DataTable


class CreateDataTableFromFile:
    """Caso de uso para construir una tabla desde un archivo."""

    def __init__(self, reader_resolver: ReaderResolver):
        self._reader_resolver = reader_resolver
        self._records_use_case = CreateDataTableFromRecords()

    def execute(self, path: str, **kwargs: Any) -> DataTable:
        reader = self._reader_resolver.resolve(path)
        records = reader.read(path, **kwargs)
        return self._records_use_case.execute(records)
