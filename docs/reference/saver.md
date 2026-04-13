# DataTableSaver

Fachada publica para persistir un `DataTable` en distintos formatos.

## Metodos disponibles

| Metodo | Salida | Nota |
| --- | --- | --- |
| `into_csv(datatable, path, encoding="utf-8")` | `CSV` | ideal para interoperabilidad |
| `into_json(datatable, path, encoding="utf-8")` | `JSON` | conserva mejor tipos simples |
| `into_xlsx(datatable, path, encoding="utf-8")` | `XLSX` | salida apta para hojas de calculo |

## Guardar el mismo DataTable en varios formatos

```python title="Persistir una misma tabla"
from pytabify import DataTableCreator, DataTableSaver

datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)

DataTableSaver.into_csv(datatable, "people.csv")
DataTableSaver.into_json(datatable, "people.json")
DataTableSaver.into_xlsx(datatable, "people.xlsx")
```

=== "CSV"

    ```text title="people.csv"
    name,age
    Alice,30
    Bob,25
    ```

=== "JSON"

    ```json title="people.json"
    [
      {"name": "Alice", "age": 30},
      {"name": "Bob", "age": 25}
    ]
    ```

=== "XLSX"

    El archivo se genera con encabezados en la primera fila y luego los registros en orden de esquema.

## Parametros

| Parametro | Requerido | Descripcion |
| --- | --- | --- |
| `datatable` | Si | instancia nativa de `DataTable` |
| `path` | Si | ruta de salida |
| `encoding` | No | relevante para `CSV` y `JSON` |

!!! note "Tipos nativos"
    `JSON` y `XLSX` representan mejor `int`, `bool` y `None` que `CSV`.

??? warning "Errores de escritura"
    Si la ruta no se puede escribir o el adaptador de salida falla, la operacion termina con una excepcion de escritura. Revisa permisos, ruta y extension objetivo.
