# Ejemplos en Python

Estos flujos reflejan escenarios ya cubiertos por las pruebas del proyecto.

## Convertir JSON a CSV

```python title="Round-trip simple desde archivo"
from pytabify import DataTableCreator, DataTableSaver

datatable = DataTableCreator.from_file("people.json")
DataTableSaver.into_csv(datatable, "people.csv")
```

!!! note "Comportamiento esperado"
    Este flujo esta cubierto por los tests end-to-end del proyecto. Es el mejor ejemplo base para usuarios que solo quieren transformar un archivo rapidamente.

## Cargar XLSX y persistir como JSON

```python title="XLSX -> JSON"
from pytabify import DataTableCreator, DataTableSaver

datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
DataTableSaver.into_json(datatable, "people.json")
```

??? warning "Si falta `sheet_name`"
    La lectura de `XLSX` lanza una excepcion cuando no recibe un nombre de hoja. Si no conoces la hoja correcta, revisa primero el archivo fuente.

## Enriquecer registros antes de guardar

```python title="Expandir el esquema y exportar"
from pytabify import DataTableCreator, DataTableSaver

datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)

datatable[0]["country"] = "MX"

DataTableSaver.into_json(datatable, "people-enriched.json")
```

=== "Antes"

    ```python title="Registros iniciales"
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    ```

=== "Despues"

    ```python title="Salida serializada"
    [
        {"name": "Alice", "age": 30, "country": "MX"},
        {"name": "Bob", "age": 25, "country": None},
    ]
    ```

## Usarlo en pruebas

```python title="Fixtures y assertions"
from pytabify import DataTableCreator

datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "active": True, "nickname": None},
        {"name": "Bob", "active": False, "nickname": None},
    ]
)

assert datatable[0].active.value is True
assert datatable[1].nickname.value is None
```

!!! tip "Eleccion de formato"
    Si las assertions dependen de tipos nativos, usa `from_records`, `JSON` o `XLSX`. Evita basarte en tipos al leer desde `CSV`.
