# Quick start

Follow the complete minimal flow: load data, inspect rows, update the schema and save another format.

## End-to-end flow

Load a JSON file, add a column in memory and export CSV. Python and Robot Framework use the same flow. Install Robot Framework separately for the Robot example.

### Input

```json title="people.json"
[
  {"name": "Alice", "age": 30},
  {"name": "Bob", "age": 25}
]
```

### Run

=== "Python"

    ```python title="quickstart.py" hl_lines="3 8 10"
    from pytabify import DataTableCreator, DataTableSaver

    datatable = DataTableCreator.from_file("people.json")

    print(datatable.column_names)
    print(datatable[0].to_dict())

    datatable[0]["country"] = "MX"

    DataTableSaver.into_csv(datatable, "people.csv")
    ```

    ```bash title="Execution"
    python quickstart.py
    ```

=== "Robot Framework"

    ```robotframework title="quickstart.robot" hl_lines="6 10 11"
    *** Settings ***
    Library    pytabify.robot.PyTabifyLibrary    WITH NAME    PyTabify

    *** Test Cases ***
    Convertir json a csv
        ${table}=    PyTabify.Create Data Table From File    people.json
        ${headers}=    PyTabify.Get Data Table Headers    ${table}
        Log To Console    ${headers}
        ${row}=    PyTabify.Get Data Table Row    ${table}    0
        Log To Console    ${row.name}
        ${table}=    PyTabify.Set Data Table Value    ${table}    0    country    MX
        PyTabify.Save Data Table To Csv    ${table}    people.csv
    ```

    ```bash title="Execution"
    robot quickstart.robot
    ```

### Expected output

=== "Python"

    === "Console output"

        ```text title="stdout"
        ('name', 'age')
        {'name': 'Alice', 'age': 30}
        ```

    === "Generated file"

        ```csv title="people.csv"
        name,age,country
        Alice,30,MX
        Bob,25,
        ```

=== "Robot Framework"

    === "Console output"

        ```text title="stdout"
        ['name', 'age']
        Alice
        ```

    === "Generated file"

        ```csv title="people.csv"
        name,age,country
        Alice,30,MX
        Bob,25,
        ```

!!! tip "Saving is explicit"
    Cell assignment changes memory only. `into_csv` or `Save Data Table To Csv` creates the file.

??? info "Alternative sources"

    === "From a file"

        ```python title="JSON -> DataTable -> CSV" hl_lines="3 8 10"
        from pytabify import DataTableCreator, DataTableSaver

        datatable = DataTableCreator.from_file("people.json")

        print(datatable.column_names)
        print(datatable[0].to_dict())

        datatable[0]["country"] = "MX"

        DataTableSaver.into_csv(datatable, "people.csv")
        ```

    === "From records"

        ```python title="List of dictionaries -> DataTable -> JSON" hl_lines="3 10 12"
        from pytabify import DataTableCreator, DataTableSaver

        datatable = DataTableCreator.from_records(
            [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
            ]
        )

        datatable[1].country = "US"

        DataTableSaver.into_json(datatable, "people.json")
        ```

## In-memory access

```python title="Index, attribute and key access" hl_lines="1 3 4"
row = datatable[0]

print(row.name)
print(row["age"])
print(row.to_dict())
```

!!! tip "Safe schema updates"
    Adding a new column to one row expands the full schema and fills other rows with None.

## Basic parameters

| Parameter | Applies to | Purpose |
| --- | --- | --- |
| `path` | `from_file`, `into_csv`, `into_json`, `into_xlsx` | Input/output file |
| `sheet_name` | XLSX `from_file` | Specific sheet |
| `encoding` | CSV/JSON reading and writing | File encoding |
| `records` | `from_records` | Initial tabular collection |

=== "path"

    ```python title="Load from a file" hl_lines="1"
    datatable = DataTableCreator.from_file("people.json")
    ```

=== "sheet_name"

    ```python title="Read a specific sheet" hl_lines="1"
    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

=== "encoding"

    ```python title="Save JSON with explicit encoding" hl_lines="1"
    DataTableSaver.into_json(datatable, "people.json", encoding="utf-8")
    ```

## Practical format rules

- **CSV:** portable; reading returns strings.
- **JSON:** preserves supported native types.
- **XLSX:** requires sheet_name when reading.

??? info "Read an XLSX sheet"

    ```python title="Read a specific sheet"
    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

## Common errors

- Missing file: `path` must identify a real file.
- Non-rectangular records: every row must share the same set of columns.
- Unexpected CSV types: use JSON, XLSX or from_records when native types matter.

## Next steps

[Python examples](../examples/python.md){ .md-button .md-button--primary }
[Robot Framework examples](../examples/robot-framework.md){ .md-button }
[DataTableCreator reference](../reference/creator.md){ .md-button }
[DataTableSaver reference](../reference/saver.md){ .md-button }
