import pytest

from pytabify import DataTable, DataTableCreator
from pytabify.domain.dt_row import DTRow
from pytabify.domain.errors import DataTableValidationException


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
    assert sample_datatable[0].name == "Alice"
    assert sample_datatable[0]["age"] == 30
    assert sample_datatable[0].active is True
    assert sample_datatable[0].nickname is None


def test_datatable_row_method_matches_getitem(sample_datatable):
    assert sample_datatable.row(1) is sample_datatable[1]


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


def test_column_names_is_stable_tuple(sample_datatable):
    assert sample_datatable.column_names == ("name", "age", "active", "nickname")


def test_row_getitem_raises_for_missing_column(sample_datatable):
    with pytest.raises(KeyError):
        sample_datatable[0]["country"]


def test_row_getattr_raises_for_missing_column(sample_datatable):
    with pytest.raises(AttributeError):
        _ = sample_datatable[0].country


def test_assigning_existing_column_updates_value_without_duplicates(sample_datatable):
    sample_datatable[0]["age"] = 31
    assert sample_datatable[0].age == 31
    assert sample_datatable[1].age == 25
    assert [header.name for header in sample_datatable.headers()] == [
        "name",
        "age",
        "active",
        "nickname",
    ]


def test_assigning_new_column_expands_schema_and_backfills_none(sample_datatable):
    sample_datatable[0]["country"] = "MX"

    assert [header.name for header in sample_datatable.headers()] == [
        "name",
        "age",
        "active",
        "nickname",
        "country",
    ]
    assert sample_datatable[0].country == "MX"
    assert sample_datatable[1].country is None


def test_setting_attribute_on_bound_row_expands_schema(sample_datatable):
    sample_datatable[1].country = "US"

    assert sample_datatable.column_names == ("name", "age", "active", "nickname", "country")
    assert sample_datatable[0].country is None
    assert sample_datatable[1].country == "US"


def test_row_to_dict_follows_table_schema(sample_datatable):
    sample_datatable[0]["country"] = "MX"
    assert sample_datatable[1].to_dict() == {
        "name": "Bob",
        "age": 25,
        "active": False,
        "nickname": None,
        "country": None,
    }


def test_invalid_row_index_does_not_expand_schema(sample_datatable):
    with pytest.raises(IndexError):
        sample_datatable.set_value(5, "new_column", "value")
    assert "new_column" not in sample_datatable.column_names


def test_attribute_and_mapping_access_preserve_native_values(sample_datatable):
    row = sample_datatable[0]
    assert row.name == row["name"] == "Alice"
    assert row.active is True
    assert row.nickname is None
    assert list(row) == ["name", "age", "active", "nickname"]


def test_local_dtrow_overwrites_existing_fields():
    row = DTRow({"name": "Alice"}, 0)
    row["name"] = "Bea"
    row.country = "MX"

    assert row["name"] == "Bea"
    assert row.country == "MX"
    assert row.to_dict() == {"name": "Bea", "country": "MX"}


def test_local_dtrow_iterates_in_insertion_order():
    row = DTRow({"name": "Alice", "age": 30}, 0)
    assert list(row) == ["name", "age"]
