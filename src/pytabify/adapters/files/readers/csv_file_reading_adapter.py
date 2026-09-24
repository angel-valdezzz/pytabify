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
            with Path(path).open(encoding=encoding, newline="") as file:
                reader = csv.reader(file, strict=True)
                header = next(reader, None)
                if header is None:
                    return []
                if any(not name.strip() for name in header):
                    raise FileReadingException("El CSV contiene un encabezado vacío.")
                if len(set(header)) != len(header):
                    raise FileReadingException("El CSV contiene encabezados duplicados.")

                records: list[dict[str, Any]] = []
                for row in reader:
                    if len(row) != len(header):
                        raise FileReadingException(
                            f"El CSV tiene {len(row)} valores en la línea {reader.line_num}; "
                            f"se esperaban {len(header)}."
                        )
                    records.append(dict(zip(header, row, strict=True)))
                return records
        except FileNotFoundError as exc:
            raise FileNotFoundException(f"El archivo {path} NO Existe verifique la ruta.") from exc
        except OSError as exc:
            raise FileReadingException("Ocurrio un error al abrir el archivo de datos csv") from exc
        except FileReadingException:
            raise
        except Exception as exc:
            raise FileReadingException("Ocurrio un Error al leer el archivo de datos csv") from exc
