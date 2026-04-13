# pytabify

<div class="hero" markdown>

Convierte datos tabulares entre `CSV`, `JSON` y `XLSX` con una API Python corta y un wrapper oficial para `Robot Framework`.

[Instalacion](getting-started/installation.md){ .md-button .md-button--primary }
[Inicio rapido](getting-started/quickstart.md){ .md-button }
[Referencia](reference/creator.md){ .md-button }

</div>

<div class="grid cards" markdown>

-   :material-download: __Instala y valida__

    Entra con `pip` o `poetry` y confirma en segundos que la libreria carga bien.

    [Ver instalacion](getting-started/installation.md)

-   :material-rocket-launch: __Empieza rapido__

    Carga un archivo, modifica una celda y exporta el resultado sin navegar por toda la API.

    [Ver quickstart](getting-started/quickstart.md)

-   :material-code-json: __Usa ejemplos reales__

    La documentacion parte de flujos cubiertos por pruebas: `JSON -> CSV`, `XLSX -> JSON` y Robot Framework.

    [Ver ejemplos](examples/python.md)

-   :material-wrench-outline: __Resuelve errores comunes__

    Errores de `sheet_name`, extensiones no soportadas, rutas invalidas o datos no rectangulares.

    [Ir a troubleshooting](troubleshooting/common-errors.md)

</div>

!!! tip "Enfoque actual del proyecto"
    `pytabify` hoy es una libreria Python con adaptador oficial para Robot Framework. Si en el futuro aparece un CLI propio, se puede documentar como una entrada adicional sin romper esta estructura.

## Lo que puedes hacer

=== "Python"

    ```python title="Leer, mutar y exportar"
    from pytabify import DataTableCreator, DataTableSaver

    datatable = DataTableCreator.from_file("people.json")
    datatable[0]["country"] = "MX"

    DataTableSaver.into_csv(datatable, "people.csv")
    ```

=== "Robot Framework"

    ```robot title="Crear una tabla y guardar a JSON"
    *** Settings ***
    Library    pytabify.robot.PyTabifyLibrary    WITH NAME    PyTabify

    *** Test Cases ***
    Guardar tabla enriquecida
        ${records}=    Create List
        ...    ${{ {"name": "Alice", "age": 30} }}
        ...    ${{ {"name": "Bob", "age": 25} }}
        ${table}=    PyTabify.Create Data Table From Records    ${records}
        ${table}=    PyTabify.Set Data Table Value    ${table}    0    country    MX
        PyTabify.Save Data Table To Json    ${table}    people.json
    ```

## Flujo recomendado

1. Instala la libreria.
2. Ejecuta el quickstart completo.
3. Salta a `Python` o `Robot Framework` segun tu caso.
4. Usa la referencia solo cuando ya sepas el flujo que quieres resolver.

??? info "Por que la referencia no va primero"
    La API publica de `pytabify` es pequena. Para este tipo de herramienta, una referencia larga al inicio agrega friccion. El orden elegido privilegia uso real primero y detalle despues.

## Cobertura de formatos

| Formato | Lectura | Escritura | Nota practica |
| --- | --- | --- | --- |
| `CSV` | Si | Si | Los valores se leen como texto. |
| `JSON` | Si | Si | Conserva bien tipos nativos simples. |
| `XLSX` | Si | Si | Requiere `sheet_name` al leer. |

!!! note "Regla de oro"
    Si necesitas preservar `int`, `bool` y `None` durante el round-trip, prefiere `JSON` o `XLSX`. `CSV` es el formato mas interoperable, pero no conserva tipos de la misma forma.
