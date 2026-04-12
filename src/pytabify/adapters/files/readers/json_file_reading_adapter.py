from __future__ import annotations

import json
from typing import Any

from pytabify.application.ports.table_reader import TableReader
from pytabify.utils.errors import FileNotFoundException, FileReadingException


class JSONFileReadingAdapter(TableReader):
    def read(self, path: str, **kwargs) -> list[dict[str, Any]]:
        encoding = kwargs.get("encoding", "utf-8")
        try:
            with open(path, mode="r", encoding=encoding) as file:
                return json.load(file)
        except FileNotFoundError as exc:
            raise FileNotFoundException(f"El archivo {path} NO Existe verifique la ruta.") from exc
        except json.JSONDecodeError as exc:
            raise FileReadingException("Ocurrio un error al leer el archivo de datos json") from exc
        except OSError as exc:
            raise FileReadingException("Ocurrio un error al abrir el archivo de datos json") from exc
