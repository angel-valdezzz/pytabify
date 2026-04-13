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


def test_public_api_stays_focused_on_use_cases_and_robot_surface():
    assert callable(DataTableCreator.from_file)
    assert callable(DataTableCreator.from_records)
    assert callable(DataTableSaver.into_csv)
    assert callable(DataTableSaver.into_json)
    assert callable(DataTableSaver.into_xlsx)
