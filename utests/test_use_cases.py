from unittest.mock import MagicMock

import pytest

from pytabify.application.use_cases.create_data_table_from_file import CreateDataTableFromFile
from pytabify.application.use_cases.create_data_table_from_records import CreateDataTableFromRecords
from pytabify.application.use_cases.save_data_table import SaveDataTable
from pytabify.domain.data_table import DataTable
from pytabify.utils.errors import DataTableValidationException


def test_create_data_table_from_records_returns_domain_table():
    datatable = CreateDataTableFromRecords().execute(
        [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
        ]
    )

    assert isinstance(datatable, DataTable)
    assert datatable.to_dict() == [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]


def test_create_data_table_from_records_propagates_validation_error():
    with pytest.raises(DataTableValidationException):
        CreateDataTableFromRecords().execute([{"name": "Alice"}, {"name": "Bob", "age": 25}])


def test_create_data_table_from_file_uses_reader_resolver_and_normalizes_records():
    reader = MagicMock()
    reader.read.return_value = [{"name": "Alice", "age": 30}, {"age": 25, "name": "Bob"}]
    reader_resolver = MagicMock()
    reader_resolver.resolve.return_value = reader

    datatable = CreateDataTableFromFile(reader_resolver).execute("sample.json", encoding="utf-8")

    reader_resolver.resolve.assert_called_once_with("sample.json")
    reader.read.assert_called_once_with("sample.json", encoding="utf-8")
    assert datatable.to_dict() == [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]


def test_save_data_table_uses_writer_resolver():
    writer = MagicMock()
    writer_resolver = MagicMock()
    writer_resolver.resolve.return_value = writer
    datatable = CreateDataTableFromRecords().execute([{"name": "Alice"}, {"name": "Bob"}])

    SaveDataTable(writer_resolver).execute(datatable, "output.json", encoding="utf-16")

    writer_resolver.resolve.assert_called_once_with("output.json")
    writer.write.assert_called_once_with(datatable, "output.json", encoding="utf-16")
