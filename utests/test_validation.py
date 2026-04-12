import pytest

from pytabify.domain.validation import validate_records
from pytabify.utils.errors import DataTableValidationException


def test_validate_records_rejects_non_list_input():
    with pytest.raises(DataTableValidationException, match="must be a list"):
        validate_records({"name": "Alice"})


def test_validate_records_rejects_non_dict_first_row():
    with pytest.raises(DataTableValidationException, match="must be a dictionary"):
        validate_records(["Alice"])


def test_validate_records_rejects_non_dict_row_after_first():
    with pytest.raises(DataTableValidationException, match="Row 1 must be a dictionary"):
        validate_records([{"name": "Alice"}, "Bob"])


def test_validate_records_rejects_non_rectangular_schema():
    with pytest.raises(DataTableValidationException, match="does not match the table schema"):
        validate_records([{"name": "Alice", "age": 30}, {"name": "Bob", "country": "MX"}])


def test_validate_records_normalizes_column_names_to_strings():
    schema, rows = validate_records([{1: "Alice", 2: 30}, {1: "Bob", 2: 25}])

    assert schema == ["1", "2"]
    assert rows == [{"1": "Alice", "2": 30}, {"1": "Bob", "2": 25}]


def test_validate_records_normalizes_later_row_order_to_first_row_schema():
    schema, rows = validate_records(
        [
            {"name": "Alice", "age": 30},
            {"age": 25, "name": "Bob"},
        ]
    )

    assert schema == ["name", "age"]
    assert rows == [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]


def test_validate_records_allows_empty_input():
    schema, rows = validate_records([])
    assert schema == []
    assert rows == []
