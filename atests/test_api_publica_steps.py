import csv
import json

import pytest
from openpyxl import Workbook
from pytest_bdd import given, parsers, scenarios, then, when

from pytabify import DataTableCreator, DataTableSaver

scenarios("features/api_publica.feature")


@pytest.fixture
def context(tmp_path):
    return {
        "tmp_path": tmp_path,
        "datatable": None,
        "input_path": None,
        "output_path": None,
    }


@given("un archivo JSON de personas")
def given_json_file(context):
    input_path = context["tmp_path"] / "people.json"
    records = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    input_path.write_text(json.dumps(records), encoding="utf-8")
    context["input_path"] = input_path
    context["expected_records"] = records


@given(parsers.parse('un archivo XLSX de personas en la hoja "{sheet_name}"'))
def given_xlsx_file(context, sheet_name):
    input_path = context["tmp_path"] / "people.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    records = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    sheet.append(["name", "age"])
    for record in records:
        sheet.append([record["name"], record["age"]])
    workbook.save(input_path)
    context["input_path"] = input_path
    context["sheet_name"] = sheet_name
    context["expected_records"] = records


@given("una colección de registros en memoria")
def given_records_in_memory(context):
    context["records"] = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]


@when("cargo el DataTable con la API pública")
def when_load_datatable_from_json(context):
    context["datatable"] = DataTableCreator.from_file(str(context["input_path"]))


@when("cargo el DataTable XLSX con la API pública")
def when_load_datatable_from_xlsx(context):
    context["datatable"] = DataTableCreator.from_file(
        str(context["input_path"]),
        sheet_name=context["sheet_name"],
    )


@when("creo un DataTable desde registros")
def when_create_datatable_from_records(context):
    context["datatable"] = DataTableCreator.from_records(context["records"])


@when("guardo el DataTable como CSV")
def when_save_as_csv(context):
    output_path = context["tmp_path"] / "people.csv"
    DataTableSaver.into_csv(context["datatable"], str(output_path))
    context["output_path"] = output_path


@when("guardo el DataTable como JSON")
def when_save_as_json(context):
    output_path = context["tmp_path"] / "people.json"
    DataTableSaver.into_json(context["datatable"], str(output_path))
    context["output_path"] = output_path


@when(parsers.parse('agrego la columna "{column_name}" con el valor "{value}" en la fila 0'))
def when_add_column_to_row(context, column_name, value):
    context["datatable"][0][column_name] = value


@then("el archivo CSV generado contiene las columnas esperadas")
def then_csv_contains_expected_columns(context):
    with context["output_path"].open(encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    assert rows == [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]


@then("el archivo JSON generado conserva los registros esperados")
def then_json_keeps_expected_records(context):
    generated_records = json.loads(context["output_path"].read_text(encoding="utf-8"))
    assert generated_records == context["expected_records"]


@then("el archivo JSON generado incluye la nueva columna en todas las filas")
def then_json_includes_new_column_everywhere(context):
    generated_records = json.loads(context["output_path"].read_text(encoding="utf-8"))
    assert generated_records == [
        {"name": "Alice", "age": 30, "country": "MX"},
        {"name": "Bob", "age": 25, "country": None},
    ]
