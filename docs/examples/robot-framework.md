# Ejemplos en Robot Framework

`pytabify` expone un wrapper oficial para Robot Framework mediante `PyTabifyLibrary`.

## Configuracion minima

```robot title="Importar la libreria"
*** Settings ***
Library    pytabify.robot.PyTabifyLibrary    WITH NAME    PyTabify
```

## Crear una tabla desde registros

```robot title="RobotDataTable desde memoria"
*** Test Cases ***
Crear tabla desde registros
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ...    ${{ {"name": "Bob", "age": 25} }}
    ${table}=    PyTabify.Create Data Table From Records    ${records}
    ${headers}=    PyTabify.Get Data Table Headers    ${table}
    Should Be Equal    ${headers}    ${["name", "age"]}
```

## Leer una fila con acceso dual

```robot title="Acceso por atributo y por llave"
*** Test Cases ***
Inspeccionar fila
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ${table}=    PyTabify.Create Data Table From Records    ${records}
    ${row}=    PyTabify.Get Data Table Row    ${table}    0
    Should Be Equal As Strings    ${row.name}    Alice
    Should Be Equal As Integers    ${row}[age]    30
```

## Mutar y guardar la tabla

```robot title="Agregar columna y persistir a JSON"
*** Test Cases ***
Mutar tabla y guardar
    ${records}=    Create List
    ...    ${{ {"name": "Alice", "age": 30} }}
    ...    ${{ {"name": "Bob", "age": 25} }}
    ${table}=    PyTabify.Create Data Table From Records    ${records}
    ${table}=    PyTabify.Set Data Table Value    ${table}    0    country    MX
    PyTabify.Save Data Table To Json    ${table}    people.json
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
    ```robot title="Crear una tabla desde archivo"
    ${table}=    PyTabify.Create Data Table From File    people.json
    ${headers}=    PyTabify.Get Data Table Headers    ${table}
    ```
