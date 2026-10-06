# DataTableSaver

Public facade for saving a native DataTable in supported formats.

## Operations

| Method | Output | Note |
| --- | --- | --- |
| `into_csv(datatable, path, encoding="utf-8")` | CSV | Portable interoperability |
| `into_json(datatable, path, encoding="utf-8")` | JSON | Supported simple types |
| `into_xlsx(datatable, path, encoding="utf-8")` | XLSX | Spreadsheet output |

`datatable` is the native table, `path` selects the output file, and encoding applies to CSV/JSON.

## Save one table in multiple formats

```python title="Save one table" hl_lines="10-12"
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

    Headers occupy the first row; records follow schema order.

## Parameters

| Parameter | Required | Meaning |
| --- | --- | --- |
| datatable | Yes | Native DataTable |
| path | Yes | Output path |
| encoding | No | CSV/JSON encoding |

## Usage variants

=== "Export CSV"

    ```python title="Portable output" hl_lines="1"
    DataTableSaver.into_csv(datatable, "people.csv")
    ```

=== "Export JSON"

    ```python title="Output with simple types" hl_lines="1"
    DataTableSaver.into_json(datatable, "people.json", encoding="utf-8")
    ```

=== "Export XLSX"

    ```python title="Excel output" hl_lines="1"
    DataTableSaver.into_xlsx(datatable, "people.xlsx")
    ```

??? info "Convert JSON to XLSX"

    ```python title="Convert JSON to XLSX" hl_lines="1-2"
    datatable = DataTableCreator.from_file("people.json")
    DataTableSaver.into_xlsx(datatable, "people.xlsx")
    ```

JSON and XLSX represent supported int, bool and None values better than CSV. Invalid paths or adapter failures raise write exceptions; check permissions, path and extension.

## Common mistakes

- Unsupported path extension.
- Expecting encoding to change XLSX writing.
- Passing an object other than native DataTable.
- Assuming CSV preserves types like JSON/XLSX.

## Good practices

Match extension and intended format. Choose CSV for portability, JSON for typed round-trips, and into_xlsx when Excel is the destination.

[DataTable](data-table.md){ .md-button .md-button--primary }
[Supported formats](file-formats.md){ .md-button }
