import json

from pytabify.application.ports.table_writer import TableWriter
from pytabify.domain.data_table import DataTable
from pytabify.utils.errors import FileWritingException


class JsonFileWritingAdapter(TableWriter):
    def write(self, datatable: DataTable, path: str, encoding: str = "utf-8"):
        data = datatable.to_dict()
        try:
            with open(path, mode="w", encoding=encoding) as output_file:
                json.dump(data, output_file, ensure_ascii=False)
        except Exception as exc:
            raise FileWritingException(
                f"No fue posible guardar los datos en el json {path}. Mas detalles: {exc}"
            ) from exc
