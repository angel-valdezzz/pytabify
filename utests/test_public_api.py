from pytabify import (
    DataTable,
    DataTableCreator,
    DataTableSaver,
    PyTabifyLibrary,
    RobotDataRow,
    RobotDataTable,
)
from pytabify.domain.dt_field import DTField
from pytabify.domain.dt_header import DTHeader
from pytabify.domain.dt_row import DTRow
from pytabify.io.file_formats import FileFormats
from pytabify.io.strategies.reading import CSVFileReadingStrategy, JSONFileReadingStrategy, XLSXReadingStrategy
from pytabify.io.strategies.saving import CsvFileSavingStrategy, JsonFileSavingStrategy, XlsxFileSavingStrategy


def test_public_package_exports_expected_symbols():
    assert DataTableCreator is not None
    assert DataTableSaver is not None
    assert DataTable is not None
    assert PyTabifyLibrary is not None
    assert RobotDataRow is not None
    assert RobotDataTable is not None


def test_domain_types_are_constructible_from_public_contract():
    field = DTField("name", "Alice", 0)
    row = DTRow({"name": "Alice"}, 0)
    datatable = DataTable.from_records([{"name": "Alice"}], ["name"])
    header = DTHeader("name", 0)

    assert field.value == "Alice"
    assert row.name.value == "Alice"
    assert datatable.headers() == [header]


def test_legacy_io_strategy_contracts_are_preserved():
    assert FileFormats(".csv").get_strategy() is CSVFileReadingStrategy
    assert FileFormats(".json").get_strategy() is JSONFileReadingStrategy
    assert FileFormats(".xlsx").get_strategy() is XLSXReadingStrategy
    assert callable(CsvFileSavingStrategy.save)
    assert callable(JsonFileSavingStrategy.save)
    assert callable(XlsxFileSavingStrategy.save)
