import csv

from pytabify.application.ports.table_writer import TableWriter
from pytabify.domain.data_table import DataTable
from pytabify.utils.errors import FileWritingException


class CsvFileWritingAdapter(TableWriter):
    def write(self, datatable: DataTable, path: str, encoding: str = "utf-8"):
        fieldnames = [header.name for header in datatable.headers()]
        data = datatable.to_dict()
        try:
            with open(path, mode="w", encoding=encoding, newline="") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except Exception as exc:
            raise FileWritingException(
                f"No fue posible guardar los datos en el csv {path}. Mas detalles: {exc}"
            ) from exc
