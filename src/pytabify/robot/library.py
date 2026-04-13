from typing import Any

from pytabify.bootstrap import (
    build_create_table_from_file_use_case,
    build_create_table_from_records_use_case,
    build_save_table_use_case,
)
from pytabify.domain.data_table import DataTable
from pytabify.robot.robot_data_row import RobotDataRow
from pytabify.robot.robot_data_table import RobotDataTable


class PyTabifyLibrary:
    """Wrapper oficial para usar pytabify desde Robot Framework."""

    def __init__(self):
        self._create_from_file = build_create_table_from_file_use_case()
        self._create_from_records = build_create_table_from_records_use_case()
        self._save_table = build_save_table_use_case()

    def create_data_table_from_file(
        self,
        path: str,
        sheet_name: str | None = None,
        encoding: str = "utf-8",
    ) -> RobotDataTable:
        if sheet_name is None:
            datatable = self._create_from_file.execute(path, encoding=encoding)
        else:
            datatable = self._create_from_file.execute(
                path, sheet_name=sheet_name, encoding=encoding
            )
        return RobotDataTable(datatable)

    def create_data_table_from_records(self, records: list[dict[str, Any]]) -> RobotDataTable:
        datatable = self._create_from_records.execute(records)
        return RobotDataTable(datatable)

    def get_data_table_row(self, datatable: RobotDataTable | DataTable, index: int) -> RobotDataRow:
        return RobotDataRow(self._unwrap_table(datatable)[index])

    def get_data_table_rows(self, datatable: RobotDataTable | DataTable) -> list[RobotDataRow]:
        return list(RobotDataTable(self._unwrap_table(datatable)))

    def get_data_table_headers(self, datatable: RobotDataTable | DataTable) -> list[str]:
        return [header.name for header in self._unwrap_table(datatable).headers()]

    def set_data_table_value(
        self,
        datatable: RobotDataTable | DataTable,
        row_index: int,
        column_name: str,
        value: Any,
    ) -> RobotDataTable:
        native_table = self._unwrap_table(datatable)
        native_table.set_value(row_index, column_name, value)
        return RobotDataTable(native_table)

    def save_data_table_to_csv(
        self,
        datatable: RobotDataTable | DataTable,
        path: str,
        encoding: str = "utf-8",
    ):
        self._save_table.execute(self._unwrap_table(datatable), path, encoding=encoding)

    def save_data_table_to_json(
        self,
        datatable: RobotDataTable | DataTable,
        path: str,
        encoding: str = "utf-8",
    ):
        self._save_table.execute(self._unwrap_table(datatable), path, encoding=encoding)

    def save_data_table_to_xlsx(
        self,
        datatable: RobotDataTable | DataTable,
        path: str,
        encoding: str = "utf-8",
    ):
        self._save_table.execute(self._unwrap_table(datatable), path, encoding=encoding)

    @staticmethod
    def _unwrap_table(datatable: RobotDataTable | DataTable) -> DataTable:
        if isinstance(datatable, RobotDataTable):
            return datatable.datatable
        return datatable
