# pytabify

<div class="hero" markdown>
<div class="project-brand">
<img class="project-brand-light" src="assets/logo-wordmark.svg" alt="Pytabify">
<img class="project-brand-dark" src="assets/logo-wordmark-dark.svg" alt="Pytabify">
</div>


Load test data from CSV, JSON and XLSX. Read cells by attribute or key, update the table and save results from Python or Robot Framework.

[Installation](getting-started/installation.md){ .md-button .md-button--primary }
[Quick start](getting-started/quickstart.md){ .md-button }
[Reference](reference/creator.md){ .md-button }

</div>

<div class="grid cards" markdown>

-   :material-download: **Install and verify**

    Use pip or Poetry and confirm the library loads.

    [Installation](getting-started/installation.md)

-   :material-rocket-launch: **Start quickly**

    Load a file, update a cell and export without reading the whole API.

    [Quick start](getting-started/quickstart.md)

-   :material-code-json: **Use tested examples**

    JSON → CSV, XLSX → JSON and Robot workflows covered by tests.

    [Examples](examples/python.md)

-   :material-wrench-outline: **Resolve common errors**

    Missing sheets, unsupported extensions, invalid paths and non-rectangular records.

    [Troubleshooting](troubleshooting/common-errors.md)

</div>

!!! tip "A cell returns its value"
    `table[0].nombre` and `table[0]["nombre"]` return the same value. Use brackets for names with spaces or collisions such as `to_dict`.

## Introduction

pytabify helps technical teams load, validate, update and save tabular data through one contract instead of writing a parser and conversion layer for every format.

It supports Python scripts, fixtures and simple transformations; QA teams using file-based test data; and Robot Framework suites needing stable row and column access.

## The problem it solves

One API handles reading different formats, keeping column order, updating rows consistently, exporting another format and reusing those operations from Python and Robot. Adding a column keeps all rows synchronized.

!!! note "Scope"
    Each column is one flat field. Nested business objects and immediate recording of generated identifiers belong to the test project.

## What you can do

=== "Python"

    ```python title="Leer, mutar y exportar" hl_lines="3-4 6"
    from pytabify import DataTableCreator, DataTableSaver

    datatable = DataTableCreator.from_file("people.json")
    datatable[0]["country"] = "MX"

    DataTableSaver.into_csv(datatable, "people.csv")
    ```

=== "Robot Framework"

    ```robotframework title="Crear una tabla y guardar a JSON" hl_lines="9-11"
    *** Settings ***
    Library    Pytabify

    *** Test Cases ***
    Guardar tabla enriquecida
        ${records}=    Create List
        ...    ${{ {"name": "Alice", "age": 30} }}
        ...    ${{ {"name": "Bob", "age": 25} }}
        ${table}=    Pytabify.Create Data Table From Records    ${records}
        ${table}=    Pytabify.Set Data Table Value    ${table}    0    country    MX
        Pytabify.Save Data Table To Json    ${table}    people.json
    ```

## Recommended route

1. [Install](getting-started/installation.md).
2. Complete the [quick start](getting-started/quickstart.md).
3. Follow [Python](examples/python.md) or [Robot](examples/robot-framework.md) examples.
4. Consult [Python API reference](reference/creator.md) or [keyword reference](keywords/index.html) for details.
5. Read [architecture](internal/architecture.md) only when maintaining or extending the library.

## Format coverage

| Format | Read | Write | Practical note |
| --- | --- | --- | --- |
| CSV | Yes | Yes | Values are read as text |
| JSON | Yes | Yes | Preserves supported native types |
| XLSX | Yes | Yes | Reading requires sheet_name |

For round-trips involving int, bool and None, prefer JSON or XLSX. CSV is portable but does not preserve types in the same way.
