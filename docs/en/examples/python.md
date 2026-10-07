---
tags:
  - Usage
---

# Python examples

These workflows are covered by the project's tests.

[Quick start](../getting-started/quickstart.md){ .md-button .md-button--primary }
[Saving tables](../reference/saver.md){ .md-button }

## Convert JSON to CSV

```python title="Simple file round-trip" hl_lines="3-4"
from pytabify import DataTableCreator, DataTableSaver

datatable = DataTableCreator.from_file("people.json")
DataTableSaver.into_csv(datatable, "people.csv")
```

!!! note "Expected behavior"
    This end-to-end flow is the simplest starting point for transforming a file quickly.

## Load XLSX and save JSON

```python title="XLSX -> JSON" hl_lines="3-4"
from pytabify import DataTableCreator, DataTableSaver

datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
DataTableSaver.into_json(datatable, "people.json")
```

??? warning "Missing sheet_name"
    XLSX reading raises an exception without a sheet name. Check the source workbook for the correct sheet.

## Enrich records before saving

```python title="Expand schema and export" hl_lines="10 12"
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

=== "Before"

    ```python title="Initial records" hl_lines="2-3"
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    ```

=== "After"

    ```python title="Serialized output" hl_lines="2-3"
    [
        {"name": "Alice", "age": 30, "country": "MX"},
        {"name": "Bob", "age": 25, "country": None},
    ]
    ```

## Use in tests

```python title="Fixtures and assertions" hl_lines="10-11"
from pytabify import DataTableCreator

datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "active": True, "nickname": None},
        {"name": "Bob", "active": False, "nickname": None},
    ]
)

assert datatable[0].active is True
assert datatable[1].nickname is None
```

!!! tip "Choose the format"
    For assertions depending on native types, use `from_records`, JSON or XLSX. CSV reading returns strings.
