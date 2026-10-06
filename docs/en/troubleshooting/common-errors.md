# Common errors

## Invalid CSV headers or rows

For FileReadingException, verify unique non-empty headers and exactly one cell per header on every row. The message identifies inconsistent lines. Quote commas or embedded newlines using CSV rules.

## An identifier was lost after a failed test

Changing table[0].folio modifies memory only. Saving CSV requires DataTableSaver.into_csv or Save Data Table To Csv. If a case may fail before saving, record generated identifiers in result storage immediately and export CSV separately.

## Unsupported extension

Resolvers choose adapters by extension. Use csv, json or xlsx matching the actual format.

## Missing sheet_name

XLSX reading requires the sheet name:

```python title="Valid XLSX read" hl_lines="1"
datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
```

## Missing XLSX sheet

Check the exact sheet name in the workbook and provide it to sheet_name.

## Non-rectangular records

Every record must match the first record's columns.

=== "Valid"

    ```python title="All rows share the schema" hl_lines="2-3"
    [
        {"name": "Alice", "age": 30},
        {"age": 25, "name": "Bob"},
    ]
    ```

=== "Invalid"

    ```python title="Inconsistent schema" hl_lines="3"
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "country": "MX"},
    ]
    ```

Normalize records before constructing the table, or add columns through controlled updates afterwards.

## Missing path

Check absolute/relative paths, working directory and process permissions. A supported format does not make a missing file readable.

## CSV type differences

CSV reading returns strings. Use JSON, XLSX or from_records when assertions depend on native types.

## Missing column

Reading a nonexistent column by key or attribute fails. Add it through a valid update:

```python title="Expand the schema" hl_lines="1"
datatable[0]["country"] = "MX"
```

Adding a column in one row propagates it to other rows with None. This is the supported way to enrich an existing table.
