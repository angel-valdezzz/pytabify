# DataTableSaver

Fachada publica para persistir un `DataTable` en distintos formatos.

## Operaciones disponibles

| Metodo | Salida | Nota |
| --- | --- | --- |
| `into_csv(datatable, path, encoding="utf-8")` | `CSV` | ideal para interoperabilidad |
| `into_json(datatable, path, encoding="utf-8")` | `JSON` | conserva mejor tipos simples |
| `into_xlsx(datatable, path, encoding="utf-8")` | `XLSX` | salida apta para hojas de calculo |

## Explicacion breve de cada opcion

- `datatable`: tabla nativa que quieres persistir.
- `path`: ruta y nombre del archivo de salida.
- `encoding`: codificacion para `CSV` y `JSON`.

## Guardar el mismo DataTable en varios formatos

```python title="Persistir una misma tabla" hl_lines="9 10 11"
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

## Variantes reales de uso

=== "Exportar a CSV"

    ```python title="Salida interoperable" hl_lines="1"
    DataTableSaver.into_csv(datatable, "people.csv")
    ```

=== "Exportar a JSON"

    ```python title="Salida con tipos simples" hl_lines="1"
    DataTableSaver.into_json(datatable, "people.json", encoding="utf-8")
    ```

=== "Exportar a XLSX"

    ```python title="Salida para Excel" hl_lines="1"
    DataTableSaver.into_xlsx(datatable, "people.xlsx")
    ```

??? info "Ejemplo secundario"
    ```python title="Convertir JSON a XLSX" hl_lines="1 2"
    datatable = DataTableCreator.from_file("people.json")
    DataTableSaver.into_xlsx(datatable, "people.xlsx")
    ```

!!! note "Tipos nativos"
    `JSON` y `XLSX` representan mejor `int`, `bool` y `None` que `CSV`.

??? warning "Errores de escritura"
    Si la ruta no se puede escribir o el adaptador de salida falla, la operacion termina con una excepcion de escritura. Revisa permisos, ruta y extension objetivo.

## Errores comunes de sintaxis o combinacion

- Usar una extension no soportada en `path`.
- Esperar que `encoding` modifique la escritura de `XLSX`.
- Intentar guardar una estructura que no sea un `DataTable` nativo.
- Asumir que `CSV` conserva tipos igual que `JSON` o `XLSX`.

## Buenas practicas de uso

- Usa una extension coherente con el formato que quieres producir.
- Si el archivo va a consumirse fuera de Python, `CSV` suele ser la salida mas portable.
- Si necesitas round-trip con tipos simples, prioriza `JSON`.
- Si el destino natural es Excel, usa `into_xlsx` en lugar de generar `CSV` por costumbre.

[Ver DataTable](data-table.md){ .md-button .md-button--primary }
[Formatos soportados](file-formats.md){ .md-button }
