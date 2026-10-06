# Ejemplos en Robot Framework

`pytabify` expone un wrapper oficial para Robot Framework mediante `PyTabifyLibrary`.

[Inicio rapido](../getting-started/quickstart.md){ .md-button .md-button--primary }
[Arquitectura](../internal/architecture.md){ .md-button }

## Configuracion minima

```robotframework title="Importar la libreria" hl_lines="2"
*** Settings ***
Library    Pytabify
```

## Crear una tabla desde registros

```robotframework title="RobotDataTable desde memoria" hl_lines="6-8"
*** Test Cases ***
Crear tabla desde registros
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ...    ${{ {"name": "Bob", "age": 25} }}
    ${table}=    Pytabify.Create Data Table From Records    ${records}
    ${headers}=    Pytabify.Get Data Table Headers    ${table}
    Should Be Equal    ${headers}    ${["name", "age"]}
```

## Leer una fila con acceso dual

```robotframework title="Acceso por atributo y por llave" hl_lines="6-8"
*** Test Cases ***
Inspeccionar fila
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ${table}=    Pytabify.Create Data Table From Records    ${records}
    ${row}=    Pytabify.Get Data Table Row    ${table}    0
    Should Be Equal As Strings    ${row.name}    Alice
    Should Be Equal As Integers    ${row}[age]    30
```

## Mutar y guardar la tabla

```robotframework title="Agregar columna y persistir a JSON" hl_lines="7-8"
*** Test Cases ***
Mutar tabla y guardar
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ...    ${{ {"name": "Bob", "age": 25} }}
    ${table}=    Pytabify.Create Data Table From Records    ${records}
    ${table}=    Pytabify.Set Data Table Value    ${table}    0    country    MX
    Pytabify.Save Data Table To Json    ${table}    people.json
```

=== "Lo que expone Robot"

    - `RobotDataTable` itera filas adaptadas.
    - `RobotDataRow` permite acceso por atributo y por llave.
    - `Get Data Table Headers` acepta tanto `RobotDataTable` como `DataTable`.

=== "Cuando conviene usarlo"

    - Cuando tus pruebas viven en Robot y no quieres mapear manualmente filas.
    - Cuando necesitas un contrato tabular estable entre keywords.

!!! note "Compatibilidad"
    El wrapper acepta tanto `RobotDataTable` como `DataTable` nativo en varias operaciones, lo que simplifica flujos mixtos entre Python y Robot.

??? info "Lectura desde archivo JSON"
    ```robotframework title="Crear una tabla desde archivo" hl_lines="1-2"
    ${table}=    Pytabify.Create Data Table From File    people.json
    ${headers}=    Pytabify.Get Data Table Headers    ${table}
    ```
