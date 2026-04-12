from typing import Any

from pytabify.bootstrap import (
    build_create_table_from_file_use_case,
    build_create_table_from_records_use_case,
)
from pytabify.domain.data_table import DataTable

class DataTableCreator:
    """Permite crear un DataTable a partir de un archivo o de una lista de diccionarios.
    
    Ejemplo:

    ```python
    from pytabify import DataTableCreator

    dt = DataTableCreator.from_file("data.json")
    dt = DataTableCreator.from_records([{"name": "Alice", "age": 30}])
    ```

    Notas:
    - El archivo debe tener una extension valida (.csv, .json, .xlsx).
    - La lista de diccionarios debe tener la misma estructura (lista de diccionarios).
    - Para lectura de archivos XLSX se debe especificar el nombre de la hoja con el argumento sheet_name.
    """

    @staticmethod
    def from_file(path: str, **kwargs) -> DataTable:
        """Crea un DataTable a partir de un archivo."""
        return build_create_table_from_file_use_case().execute(path, **kwargs)

    @staticmethod
    def from_records(records: list[dict[str, Any]]) -> DataTable:
        """Crea un DataTable a partir de una lista de diccionarios."""
        return build_create_table_from_records_use_case().execute(records)
