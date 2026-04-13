# Inicio rapido

Este recorrido cubre el flujo minimo completo: cargar datos, inspeccionar filas, mutar el esquema y guardar en otro formato.

## Flujo minimo de principio a fin

Este ejemplo toma un archivo `JSON`, lo carga en memoria, agrega una columna nueva y lo exporta a `CSV`. El mismo flujo aparece en Python y en Robot Framework.

### Input

```json title="people.json"
[
  {"name": "Alice", "age": 30},
  {"name": "Bob", "age": 25}
]
```

### Comando

=== "Python"

    ```python title="quickstart.py"
    from pytabify import DataTableCreator, DataTableSaver

    datatable = DataTableCreator.from_file("people.json")

    print(datatable.column_names)
    print(datatable[0].to_dict())

    datatable[0]["country"] = "MX"

    DataTableSaver.into_csv(datatable, "people.csv")
    ```

    ```bash title="Ejecucion"
    python quickstart.py
    ```

=== "Robot Framework"

    ```robotframework title="quickstart.robot"
    *** Settings ***
    Library    pytabify.robot.PyTabifyLibrary    WITH NAME    PyTabify

    *** Test Cases ***
    Convertir json a csv
        ${table}=    PyTabify.Create Data Table From File    people.json
        ${headers}=    PyTabify.Get Data Table Headers    ${table}
        Log To Console    ${headers}
        ${row}=    PyTabify.Get Data Table Row    ${table}    0
        Log To Console    ${row.to_dict()}
        ${table}=    PyTabify.Set Data Table Value    ${table}    0    country    MX
        PyTabify.Save Data Table To Csv    ${table}    people.csv
    ```

    ```bash title="Ejecucion"
    robot quickstart.robot
    ```


### Output esperado

=== "Python"

    === "Salida en consola"

        ```text title="stdout"
        ('name', 'age')
        {'name': 'Alice', 'age': 30}
        ```

    === "Archivo generado"

        ```csv title="people.csv"
        name,age,country
        Alice,30,MX
        Bob,25,
        ```

=== "Robot Framework"

    === "Salida en consola"

        ```text title="stdout"
        ['name', 'age']
        {'name': 'Alice', 'age': 30}
        ```

    === "Archivo generado"

        ```csv title="people.csv"
        name,age,country
        Alice,30,MX
        Bob,25,
        ```

!!! tip "Que demuestra este flujo"
    El ejemplo muestra las tres operaciones centrales de `pytabify`: lectura, mutacion con esquema estable y persistencia en otro formato.

## Variantes del mismo flujo

=== "Desde archivo"

    ```python title="JSON -> DataTable -> CSV"
    from pytabify import DataTableCreator, DataTableSaver

    datatable = DataTableCreator.from_file("people.json")

    print(datatable.column_names)
    print(datatable[0].to_dict())

    datatable[0]["country"] = "MX"

    DataTableSaver.into_csv(datatable, "people.csv")
    ```

=== "Desde registros"

    ```python title="Lista de diccionarios -> DataTable -> JSON"
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

## Que pasa en memoria

```python title="Acceso por indice, atributo y llave"
row = datatable[0]

print(row.name.value)
print(row["age"].value)
print(row.to_dict())
```

!!! tip "Mutacion segura del esquema"
    Si agregas una columna nueva en una fila, `pytabify` extiende el esquema completo y rellena `None` en las demas filas.

## Ejemplo comparativo

=== "Input"

    ```json title="people.json"
    [
      {"name": "Alice", "age": 30},
      {"name": "Bob", "age": 25}
    ]
    ```

=== "Output"

    ```json title="people-enriched.json"
    [
      {"name": "Alice", "age": 30, "country": "MX"},
      {"name": "Bob", "age": 25, "country": null}
    ]
    ```

## Casos que debes recordar

<div class="grid cards" markdown>

-   __`CSV`__

    Bueno para interoperabilidad rapida. Al leer, los valores llegan como texto.

-   __`JSON`__

    Buena opcion cuando quieres conservar tipos nativos simples.

-   __`XLSX`__

    Necesita `sheet_name` al leer desde archivo.

</div>

??? info "Lectura de XLSX"
    ```python title="Lectura de una hoja especifica"
    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

## Despues del quickstart

[Ejemplos en Python](../examples/python.md){ .md-button .md-button--primary }
[Referencia de DataTableCreator](../reference/creator.md){ .md-button }
