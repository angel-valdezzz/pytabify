from typing import Any

from pytabify.utils.errors import DataTableValidationException


def validate_records(data: Any) -> tuple[list[str], list[dict[str, Any]]]:
    """Valida una coleccion de registros y devuelve una version normalizada."""
    if not isinstance(data, list):
        raise DataTableValidationException("DataTable data must be a list of dictionaries.")

    if not data:
        return [], []

    if not isinstance(data[0], dict):
        raise DataTableValidationException("Each row must be a dictionary.")

    schema = [str(column_name) for column_name in data[0].keys()]
    expected_columns = set(schema)
    normalized_rows: list[dict[str, Any]] = []

    for row_index, record in enumerate(data):
        if not isinstance(record, dict):
            raise DataTableValidationException(f"Row {row_index} must be a dictionary.")

        normalized_record = {str(column_name): value for column_name, value in record.items()}
        current_columns = set(normalized_record.keys())
        if current_columns != expected_columns:
            raise DataTableValidationException(
                f"Row {row_index} does not match the table schema. "
                f"Expected columns {schema}, got {list(normalized_record.keys())}."
            )

        normalized_rows.append({column_name: normalized_record[column_name] for column_name in schema})

    return schema, normalized_rows
