from pytabify import DataTableCreator
from pytabify.domain.validation import validate_records
from pytabify.robot import PyTabifyLibrary


def test_domain_validation_module_stays_available():
    schema, rows = validate_records([{"name": "Alice"}, {"name": "Bob"}])
    assert schema == ["name"]
    assert rows == [{"name": "Alice"}, {"name": "Bob"}]


def test_robot_create_data_table_from_file_supports_json_without_sheet_name(tmp_path):
    input_file = tmp_path / "people.json"
    input_file.write_text('[{"name":"Alice","age":30}]', encoding="utf-8")

    datatable = PyTabifyLibrary().create_data_table_from_file(str(input_file))

    assert datatable.headers == ["name", "age"]
    assert datatable[0].name == "Alice"


def test_robot_save_methods_delegate_without_returning_value(tmp_path):
    library = PyTabifyLibrary()
    datatable = library.create_data_table_from_records([{"name": "Alice"}])

    json_file = tmp_path / "people.json"
    csv_file = tmp_path / "people.csv"
    xlsx_file = tmp_path / "people.xlsx"

    assert library.save_data_table_to_json(datatable, str(json_file)) is None
    assert library.save_data_table_to_csv(datatable, str(csv_file)) is None
    assert library.save_data_table_to_xlsx(datatable, str(xlsx_file)) is None

    native = DataTableCreator.from_file(str(json_file))
    assert native.to_dict() == [{"name": "Alice"}]
