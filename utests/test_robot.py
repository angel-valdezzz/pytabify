import pytest

from pytabify import DataTableCreator
from pytabify.robot import PyTabifyLibrary, RobotDataRow, RobotDataTable


@pytest.fixture
def library():
    return PyTabifyLibrary()


@pytest.fixture
def records():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]


def test_create_data_table_from_records_returns_robot_adapter(library, records):
    datatable = library.create_data_table_from_records(records)
    assert isinstance(datatable, RobotDataTable)
    assert datatable.headers == ["name", "age"]


def test_get_data_table_row_returns_row_adapter_with_dual_access(library, records):
    datatable = library.create_data_table_from_records(records)
    row = library.get_data_table_row(datatable, 0)

    assert isinstance(row, RobotDataRow)
    assert row.name == "Alice"
    assert row["age"] == 30
    assert row.columns == ["name", "age"]
    assert row.to_dict() == {"name": "Alice", "age": 30}


def test_get_data_table_rows_returns_adapters(library, records):
    datatable = library.create_data_table_from_records(records)
    rows = library.get_data_table_rows(datatable)

    assert len(rows) == 2
    assert all(isinstance(row, RobotDataRow) for row in rows)
    assert rows[1].name == "Bob"


def test_set_data_table_value_updates_underlying_table(library, records):
    datatable = library.create_data_table_from_records(records)

    updated_table = library.set_data_table_value(datatable, 0, "country", "MX")

    assert isinstance(updated_table, RobotDataTable)
    row = library.get_data_table_row(updated_table, 0)
    second_row = library.get_data_table_row(updated_table, 1)
    assert row.country == "MX"
    assert second_row.country is None


def test_robot_wrapper_accepts_native_datatable(library, records):
    native_datatable = DataTableCreator.from_records(records)
    row = library.get_data_table_row(native_datatable, 0)

    assert row.name == "Alice"


def test_robot_row_adapter_missing_attribute_raises(library, records):
    datatable = library.create_data_table_from_records(records)
    row = library.get_data_table_row(datatable, 0)

    with pytest.raises(AttributeError):
        _ = row.country
