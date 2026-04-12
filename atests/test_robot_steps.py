import json

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from pytabify.robot import PyTabifyLibrary, RobotDataRow, RobotDataTable


scenarios("features/robot.feature")


@pytest.fixture
def robot_context(tmp_path):
    return {
        "tmp_path": tmp_path,
        "library": PyTabifyLibrary(),
        "datatable": None,
        "row": None,
        "input_path": None,
        "output_path": None,
    }


@given("una colección de registros en memoria")
def given_records(robot_context):
    robot_context["records"] = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]


@given("un archivo JSON de personas")
def given_json_file(robot_context):
    input_path = robot_context["tmp_path"] / "people.json"
    records = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    input_path.write_text(json.dumps(records), encoding="utf-8")
    robot_context["input_path"] = input_path


@when("creo una RobotDataTable desde registros")
def when_create_robot_table_from_records(robot_context):
    robot_context["datatable"] = robot_context["library"].create_data_table_from_records(robot_context["records"])


@when("obtengo la fila 0 con la librería de Robot")
def when_get_first_row(robot_context):
    robot_context["row"] = robot_context["library"].get_data_table_row(robot_context["datatable"], 0)


@when(parsers.parse('asigno la columna "{column_name}" con el valor "{value}" en la fila 0 usando Robot'))
def when_set_robot_value(robot_context, column_name, value):
    robot_context["datatable"] = robot_context["library"].set_data_table_value(
        robot_context["datatable"],
        0,
        column_name,
        value,
    )


@when("guardo la RobotDataTable como JSON")
def when_save_robot_table_as_json(robot_context):
    output_path = robot_context["tmp_path"] / "robot-output.json"
    robot_context["library"].save_data_table_to_json(robot_context["datatable"], str(output_path))
    robot_context["output_path"] = output_path


@when("creo una RobotDataTable desde archivo JSON")
def when_create_robot_table_from_json_file(robot_context):
    robot_context["datatable"] = robot_context["library"].create_data_table_from_file(str(robot_context["input_path"]))


@then("la fila de Robot expone acceso por atributo y por llave")
def then_robot_row_exposes_dual_access(robot_context):
    row = robot_context["row"]
    assert isinstance(row, RobotDataRow)
    assert row.name == "Alice"
    assert row["age"] == 30
    assert row.to_dict() == {"name": "Alice", "age": 30}


@then("el archivo JSON generado incluye la nueva columna en todas las filas")
def then_robot_json_includes_new_column(robot_context):
    generated_records = json.loads(robot_context["output_path"].read_text(encoding="utf-8"))
    assert generated_records == [
        {"name": "Alice", "age": 30, "country": "MX"},
        {"name": "Bob", "age": 25, "country": None},
    ]


@then("los headers de Robot coinciden con el archivo fuente")
def then_robot_headers_match_source(robot_context):
    datatable = robot_context["datatable"]
    assert isinstance(datatable, RobotDataTable)
    assert datatable.headers == ["name", "age"]
