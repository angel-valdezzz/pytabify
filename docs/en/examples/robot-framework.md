---
tags:
  - Usage
---

# Robot Framework examples

`pytabify` provides its official Robot Framework wrapper, `PyTabifyLibrary`.

[Quick start](../getting-started/quickstart.md){ .md-button .md-button--primary }
[Keyword reference](../keywords/index.html){ .md-button }

## Minimal configuration

```robotframework title="Import the library" hl_lines="2"
*** Settings ***
Library    Pytabify
```

## Create a table from records

```robotframework title="In-memory RobotDataTable" hl_lines="6-8"
*** Test Cases ***
Crear tabla desde registros
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ...    ${{ {"name": "Bob", "age": 25} }}
    ${table}=    Pytabify.Create Data Table From Records    ${records}
    ${headers}=    Pytabify.Get Data Table Headers    ${table}
    Should Be Equal    ${headers}    ${["name", "age"]}
```

## Read a row by attribute or key

```robotframework title="Attribute and key access" hl_lines="6-8"
*** Test Cases ***
Inspeccionar fila
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ${table}=    Pytabify.Create Data Table From Records    ${records}
    ${row}=    Pytabify.Get Data Table Row    ${table}    0
    Should Be Equal As Strings    ${row.name}    Alice
    Should Be Equal As Integers    ${row}[age]    30
```

## Update and save the table

```robotframework title="Add a column and save JSON" hl_lines="7-8"
*** Test Cases ***
Mutar tabla y guardar
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ...    ${{ {"name": "Bob", "age": 25} }}
    ${table}=    Pytabify.Create Data Table From Records    ${records}
    ${table}=    Pytabify.Set Data Table Value    ${table}    0    country    MX
    Pytabify.Save Data Table To Json    ${table}    people.json
```

=== "Robot interface"

    - `RobotDataTable` iterates adapted rows.
    - `RobotDataRow` supports attribute and key access.
    - `Get Data Table Headers` accepts both RobotDataTable and native DataTable.

=== "When to use it"

    - Your tests run in Robot and you want to avoid manually mapping rows.
    - You need a stable tabular contract between keywords.

!!! note "Compatibility"
    Several operations accept both RobotDataTable and native DataTable, simplifying mixed Python/Robot flows.

??? info "Read a JSON file"

    ```robotframework title="Create a table from a file" hl_lines="1-2"
    ${table}=    Pytabify.Create Data Table From File    people.json
    ${headers}=    Pytabify.Get Data Table Headers    ${table}
    ```
