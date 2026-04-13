from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

from pytabify.adapters.files.errors import FileNotFoundException, FileReadingException
from pytabify.application.ports.table_reader import TableReader


class JSONFileReadingAdapter(TableReader):
    def read(self, path: str, **kwargs) -> list[dict[str, Any]]:
        encoding = kwargs.get("encoding", "utf-8")
        try:
            with Path(path).open(encoding=encoding) as file:
                return cast(list[dict[str, Any]], json.load(file))
        except FileNotFoundError as exc:
            raise FileNotFoundException(f"El archivo {path} NO Existe verifique la ruta.") from exc
        except json.JSONDecodeError as exc:
            raise FileReadingException("Ocurrio un error al leer el archivo de datos json") from exc
        except OSError as exc:
            raise FileReadingException(
                "Ocurrio un error al abrir el archivo de datos json"
            ) from exc
