from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from pytabify.adapters.files.errors import FileNotFoundException, FileReadingException
from pytabify.application.ports.table_reader import TableReader


class CSVFileReadingAdapter(TableReader):
    def read(self, path: str, **kwargs) -> list[dict[str, Any]]:
        encoding = kwargs.get("encoding", "utf-8")
        try:
            with Path(path).open(encoding=encoding) as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError as exc:
            raise FileNotFoundException(f"El archivo {path} NO Existe verifique la ruta.") from exc
        except OSError as exc:
            raise FileReadingException("Ocurrio un error al abrir el archivo de datos csv") from exc
        except Exception as exc:
            raise FileReadingException("Ocurrio un Error al leer el archivo de datos csv") from exc
