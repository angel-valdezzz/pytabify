# DataTableCreator

Public facade for creating tables from files or records.

## Operations

| Method | Input | Result |
| --- | --- | --- |
| `from_file(path, **kwargs)` | CSV, JSON or XLSX | Native DataTable |
| `from_records(records)` | List of dictionaries | Native DataTable |

## from_file

=== "JSON"

    ```python title="Load JSON" hl_lines="3"
    from pytabify import DataTableCreator

    datatable = DataTableCreator.from_file("people.json")
    ```

=== "CSV"

    ```python title="Load CSV" hl_lines="3"
    from pytabify import DataTableCreator

    datatable = DataTableCreator.from_file("people.csv", encoding="utf-8")
    ```

=== "XLSX"

    ```python title="Load XLSX" hl_lines="3"
    from pytabify import DataTableCreator

    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

`path` selects the input file; its extension selects the reader. `sheet_name` is required for XLSX. `encoding` defaults to utf-8 and applies to CSV/JSON, not XLSX.

### Valid combinations

=== "Valid"

    ```python title="Valid reads" hl_lines="3"
    DataTableCreator.from_file("people.json")
    DataTableCreator.from_file("people.csv", encoding="utf-8")
    DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

=== "Invalid"

    ```python title="Invalid combinations"
    DataTableCreator.from_file("people.xlsx")
    DataTableCreator.from_file("people.txt")
    ```

??? info "Specific XLSX sheet"

    ```python title="Load a specific sheet"
    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

Unsupported extensions raise infrastructure errors. Common mistakes include missing sheet_name, unsupported paths, expecting encoding to affect XLSX and assuming CSV reads native types.

## from_records

```python title="Create a table from memory" hl_lines="1"
datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)
```

Records must be dictionaries sharing the same tabular schema. Column order follows the first valid record. Names are normalized to strings and must be unique and non-empty.

=== "Valid"

    ```python title="Consistent schema"
    [
        {"name": "Alice", "age": 30},
        {"age": 25, "name": "Bob"},
    ]
    ```

=== "Invalid"

    ```python title="Non-rectangular schema"
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "country": "MX"},
    ]
    ```

## Usage examples

=== "Prepare fixtures"

    ```python title="In-memory test table" hl_lines="1"
    datatable = DataTableCreator.from_records(
        [
            {"name": "Alice", "active": True},
            {"name": "Bob", "active": False},
        ]
    )
    ```

=== "Load and process"

    ```python title="Use the in-memory table" hl_lines="1 2 3"
    datatable = DataTableCreator.from_file("people.json")
    first_row = datatable[0].to_dict()
    headers = datatable.column_names
    ```

## Good practices

- Use from_records when data is already in memory or for file-independent fixtures.
- Use from_file when your source is a file.
- Keep input schemas consistent; add new columns afterwards through table updates rather than irregular input rows.
- Prefer JSON, XLSX or from_records for typed data.

[Saving tables](saver.md){ .md-button .md-button--primary }
[DataTable](data-table.md){ .md-button }
