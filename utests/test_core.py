import pytest

from pytabify import DataTable, DataTableCreator
from pytabify.domain.dt_field import DTField
from pytabify.domain.dt_row import DTRow
from pytabify.utils.errors import DataTableValidationException


@pytest.fixture
def sample_records():
    return [
        {"name": "Alice", "age": 30, "active": True, "nickname": None},
        {"name": "Bob", "age": 25, "active": False, "nickname": None},
    ]


@pytest.fixture
def sample_datatable(sample_records):
    return DataTableCreator.from_records(sample_records)


def test_from_records_creates_datatable_with_native_types(sample_datatable):
    assert isinstance(sample_datatable, DataTable)
    assert len(sample_datatable) == 2
    assert sample_datatable[0].name.value == "Alice"
    assert sample_datatable[0].age.value == 30
    assert sample_datatable[0].active.value is True
    assert sample_datatable[0].nickname.value is None


def test_from_records_allows_empty_lists():
    datatable = DataTableCreator.from_records([])
    assert len(datatable) == 0
    assert datatable.headers() == []
    assert datatable.to_dict() == []


def test_from_records_rejects_non_rectangular_data():
    records = [{"name": "Alice", "age": 30}, {"name": "Bob"}]
    with pytest.raises(DataTableValidationException):
        DataTableCreator.from_records(records)


def test_headers_follow_schema_order(sample_datatable):
    headers = sample_datatable.headers()
    assert [header.name for header in headers] == ["name", "age", "active", "nickname"]
    assert [header.index for header in headers] == [0, 1, 2, 3]


def test_row_getitem_raises_for_missing_column(sample_datatable):
    with pytest.raises(KeyError):
        sample_datatable[0]["country"]


def test_row_getattr_raises_for_missing_column(sample_datatable):
    with pytest.raises(AttributeError):
        _ = sample_datatable[0].country


def test_assigning_existing_column_updates_value_without_duplicates(sample_datatable):
    sample_datatable[0]["age"] = 31
    assert sample_datatable[0].age.value == 31
    assert [header.name for header in sample_datatable.headers()] == ["name", "age", "active", "nickname"]


def test_assigning_new_column_expands_schema_and_backfills_none(sample_datatable):
    sample_datatable[0]["country"] = "MX"

    assert [header.name for header in sample_datatable.headers()] == ["name", "age", "active", "nickname", "country"]
    assert sample_datatable[0].country.value == "MX"
    assert sample_datatable[1].country.value is None


def test_row_to_dict_follows_table_schema(sample_datatable):
    sample_datatable[0]["country"] = "MX"
    assert sample_datatable[1].to_dict() == {
        "name": "Bob",
        "age": 25,
        "active": False,
        "nickname": None,
        "country": None,
    }


def test_dtfield_preserves_native_value_and_length():
    field = DTField("edad", 20, 1)
    none_field = DTField("nickname", None, 2)

    assert field.name == "edad"
    assert field.value == 20
    assert field.index == 1
    assert str(field) == "20"
    assert len(field) == 2
    assert none_field.is_none is True
    assert len(none_field) == 0


def test_local_dtrow_overwrites_existing_fields():
    row = DTRow({"name": "Alice"}, 0)
    row["name"] = "Bea"
    row.country = "MX"

    assert row["name"].value == "Bea"
    assert row.country.value == "MX"
    assert row.to_dict() == {"name": "Bea", "country": "MX"}
