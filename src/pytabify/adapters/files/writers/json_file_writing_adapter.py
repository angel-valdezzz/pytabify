import json
from pathlib import Path

from pytabify.adapters.files.errors import FileWritingException
from pytabify.application.ports.table_writer import TableWriter
from pytabify.domain.data_table import DataTable


class JsonFileWritingAdapter(TableWriter):
    def write(self, datatable: DataTable, path: str, encoding: str = "utf-8") -> None:
        data = datatable.to_dict()
        try:
            with Path(path).open(mode="w", encoding=encoding) as output_file:
                json.dump(data, output_file, ensure_ascii=False)
        except Exception as exc:
            raise FileWritingException(
                f"No fue posible guardar los datos en el json {path}. Mas detalles: {exc}"
            ) from exc
