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
    """Official wrapper for using pytabify from Robot Framework."""

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
        """Load CSV, JSON or XLSX and return a RobotDataTable.

        ``path`` selects the file. ``sheet_name`` is required for XLSX; ``encoding`` defaults to
        utf-8 and applies to CSV/JSON. CSV cells remain strings, including empty cells and
        leading zeros. File or schema errors propagate.

        | ${table}= | Create Data Table From File | people.xlsx | sheet_name=People |
        """
        if sheet_name is None:
            datatable = self._create_from_file.execute(path, encoding=encoding)
        else:
            datatable = self._create_from_file.execute(
                path, sheet_name=sheet_name, encoding=encoding
            )
        return RobotDataTable(datatable)

    def create_data_table_from_records(self, records: list[dict[str, Any]]) -> RobotDataTable:
        """Create a RobotDataTable from a list of dictionaries with the same columns.

        Column order follows the first record; values keep their Python types. Column names are
        normalized to strings and must be unique and non-empty. Inconsistent schemas raise an
        error. No file is written.
        """
        datatable = self._create_from_records.execute(records)
        return RobotDataTable(datatable)

    def get_data_table_row(self, datatable: RobotDataTable | DataTable, index: int) -> RobotDataRow:
        """Return a RobotDataRow at the zero-based index.

        Accepts a RobotDataTable or native DataTable. Access cells directly by attribute or key,
        such as ${row.name} or ${row}[name]. Missing row indices raise IndexError.
        """
        return RobotDataRow(self._unwrap_table(datatable)[index])

    def get_data_table_rows(self, datatable: RobotDataTable | DataTable) -> list[RobotDataRow]:
        """Return all rows as a list of RobotDataRow objects in table order.

        Accepts a RobotDataTable or native DataTable. Rows refer to the underlying table;
        changing a row changes its in-memory data, not a file.
        """
        return list(RobotDataTable(self._unwrap_table(datatable)))

    def get_data_table_headers(self, datatable: RobotDataTable | DataTable) -> list[str]:
        """Return the table's column names as an ordered list of strings.

        Accepts a RobotDataTable or native DataTable. Does not change the table.
        """
        return [header.name for header in self._unwrap_table(datatable).headers()]

    def set_data_table_value(
        self,
        datatable: RobotDataTable | DataTable,
        row_index: int,
        column_name: str,
        value: Any,
    ) -> RobotDataTable:
        """Set one cell and return a RobotDataTable wrapping the same native table.

        ``row_index`` is zero-based; ``column_name`` identifies the column. A new column expands
        the whole schema and fills other rows with None. An invalid index raises IndexError
        without expanding the schema. Saving remains explicit.
        """
        native_table = self._unwrap_table(datatable)
        native_table.set_value(row_index, column_name, value)
        return RobotDataTable(native_table)

    def save_data_table_to_csv(
        self,
        datatable: RobotDataTable | DataTable,
        path: str,
        encoding: str = "utf-8",
    ):
        """Save a RobotDataTable or native DataTable to CSV at path.

        ``encoding`` defaults to utf-8. Writes the current in-memory table with ordered headers.
        CSV does not preserve native types like JSON or XLSX. Returns nothing; write errors
        propagate.
        """
        self._save_table.execute(self._unwrap_table(datatable), path, encoding=encoding)

    def save_data_table_to_json(
        self,
        datatable: RobotDataTable | DataTable,
        path: str,
        encoding: str = "utf-8",
    ):
        """Save a RobotDataTable or native DataTable as a JSON list of records at path.

        ``encoding`` defaults to utf-8. JSON preserves supported types such as numbers, booleans
        and null. Returns nothing; serialization and write errors propagate.
        """
        self._save_table.execute(self._unwrap_table(datatable), path, encoding=encoding)

    def save_data_table_to_xlsx(
        self,
        datatable: RobotDataTable | DataTable,
        path: str,
        encoding: str = "utf-8",
    ):
        """Save a RobotDataTable or native DataTable as an XLSX workbook at path.

        Headers are written in the first row, followed by records in schema order. ``encoding``
        is accepted for API compatibility and does not control XLSX encoding. Returns nothing;
        write errors propagate.
        """
        self._save_table.execute(self._unwrap_table(datatable), path, encoding=encoding)

    @staticmethod
    def _unwrap_table(datatable: RobotDataTable | DataTable) -> DataTable:
        if isinstance(datatable, RobotDataTable):
            return datatable.datatable
        return datatable
