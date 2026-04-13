# DataTable

`DataTable` es el contrato tabular en memoria. Mantiene un esquema canonico estable y filas sincronizadas con ese esquema.

## Lectura

=== "Acceso por indice"

    ```python title="Obtener una fila"
    row = datatable[0]
    print(row.to_dict())
    ```

=== "Acceso por atributo"

    ```python title="Leer un campo"
    print(datatable[0].name.value)
    ```

=== "Acceso por llave"

    ```python title="Leer un campo por columna"
    print(datatable[0]["age"].value)
    ```

## Escritura

=== "Actualizar columna existente"

    ```python title="Mutar una celda sin duplicar columnas"
    datatable[0]["age"] = 31
    ```

=== "Agregar columna nueva"

    ```python title="Expandir el esquema"
    datatable[0]["country"] = "MX"
    ```

    ```python title="Efecto en toda la tabla"
    print(datatable[0].country.value)  # MX
    print(datatable[1].country.value)  # None
    ```

## Operaciones utiles

| Operacion | Resultado |
| --- | --- |
| `len(datatable)` | total de filas |
| `datatable.row(index)` | fila por indice |
| `datatable.column_names` | tupla con nombres de columna |
| `datatable.headers()` | headers con nombre e indice |
| `datatable.to_dict()` | lista serializable de registros |

!!! tip "Schema-first"
    El esquema no depende de la fila que leas despues. Queda definido por la validacion inicial y por las expansiones controladas que hagas sobre la tabla.

??? info "Lo que no debes asumir"
    - No asumas que leer desde `CSV` preserva tipos nativos.
    - No asumas que una columna ausente en una fila puede omitirse sin afectar el contrato.
    - No asumas que una columna inexistente devolvera `None`; en lectura directa puede lanzar `KeyError` o `AttributeError`.
