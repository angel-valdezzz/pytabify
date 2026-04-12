from __future__ import annotations

from typing import Any

from pytabify.domain.data_table import DataTable
from pytabify.domain.validation import validate_records


class CreateDataTableFromRecords:
    """Caso de uso para construir una tabla desde registros en memoria."""

    def execute(self, records: list[dict[str, Any]]) -> DataTable:
        schema, normalized_data = validate_records(records)
        return DataTable.from_records(normalized_data, schema)
