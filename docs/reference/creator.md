# DataTableCreator

Fachada publica para construir un `DataTable` desde archivo o desde registros en memoria.

## Metodos disponibles

| Metodo | Entrada | Uso recomendado |
| --- | --- | --- |
| `from_file(path, **kwargs)` | archivo `CSV`, `JSON` o `XLSX` | ingestar datos ya persistidos |
| `from_records(records)` | lista de diccionarios | construir datos tabulares en memoria |

## `from_file(path, **kwargs)`

```python title="Uso basico"
from pytabify import DataTableCreator

datatable = DataTableCreator.from_file("people.json")
```

### Parametros practicos

| Parametro | Requerido | Aplica a | Nota |
| --- | --- | --- | --- |
| `path` | Si | todos | determina el reader por extension |
| `sheet_name` | Si para lectura `XLSX` | `XLSX` | sin este valor la lectura falla |
| `encoding` | No | `CSV`, `JSON` | por defecto usa `utf-8` |

??? info "Lectura de XLSX"
    ```python title="Cargar una hoja especifica"
    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

!!! warning "Extension no soportada"
    Si la extension no es `csv`, `json` o `xlsx`, el flujo termina con una excepcion de infraestructura.

## `from_records(records)`

```python title="Crear una tabla desde memoria"
datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)
```

### Contrato esperado

<div class="grid cards" markdown>

-   __Entrada valida__

    Una lista de diccionarios con el mismo esquema tabular.

-   __Orden estable__

    El orden de columnas queda anclado al primer registro valido.

-   __Normalizacion__

    Los nombres de columnas se normalizan a `str`.

</div>

=== "Valido"

    ```python title="Esquema consistente"
    [
        {"name": "Alice", "age": 30},
        {"age": 25, "name": "Bob"},
    ]
    ```

=== "Invalido"

    ```python title="Esquema no rectangular"
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "country": "MX"},
    ]
    ```

!!! tip "Cuando elegir `from_records`"
    Es la mejor opcion cuando el origen real de datos ya esta en memoria o cuando quieres preparar fixtures para pruebas sin depender de archivos temporales.
