# DataTableCreator

Fachada publica para construir un `DataTable` desde archivo o desde registros en memoria.

## Operaciones disponibles

| Metodo | Entrada | Uso recomendado |
| --- | --- | --- |
| `from_file(path, **kwargs)` | archivo `CSV`, `JSON` o `XLSX` | ingestar datos ya persistidos |
| `from_records(records)` | lista de diccionarios | construir datos tabulares en memoria |

!!! note "Referencia rapida"
    Si ya instalaste la libreria, esta es la entrada correcta para crear tablas en escenarios reales. No necesitas pasar por infraestructura interna.

## `from_file(path, **kwargs)`

=== "JSON"

    ```python title="Cargar JSON"
    from pytabify import DataTableCreator

    datatable = DataTableCreator.from_file("people.json")
    ```

=== "CSV"

    ```python title="Cargar CSV"
    from pytabify import DataTableCreator

    datatable = DataTableCreator.from_file("people.csv", encoding="utf-8")
    ```

=== "XLSX"

    ```python title="Cargar XLSX"
    from pytabify import DataTableCreator

    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

### Parametros practicos

| Parametro | Requerido | Aplica a | Nota |
| --- | --- | --- | --- |
| `path` | Si | todos | determina el reader por extension |
| `sheet_name` | Si para lectura `XLSX` | `XLSX` | sin este valor la lectura falla |
| `encoding` | No | `CSV`, `JSON` | por defecto usa `utf-8` |

### Explicacion breve de cada argumento

- `path`: ruta del archivo de entrada.
- `sheet_name`: nombre exacto de la hoja cuando el archivo es `xlsx`.
- `encoding`: codificacion para lectura de `csv` o `json`.

## Combinaciones validas

=== "Valido"

    ```python title="Lecturas correctas"
    DataTableCreator.from_file("people.json")
    DataTableCreator.from_file("people.csv", encoding="utf-8")
    DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

=== "Invalido"

    ```python title="Combinaciones que fallan"
    DataTableCreator.from_file("people.xlsx")
    DataTableCreator.from_file("people.txt")
    ```

??? info "Lectura de XLSX"
    ```python title="Cargar una hoja especifica"
    datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
    ```

!!! warning "Extension no soportada"
    Si la extension no es `csv`, `json` o `xlsx`, el flujo termina con una excepcion de infraestructura.

??? warning "Errores comunes de sintaxis o combinacion"
    - Olvidar `sheet_name` al leer `XLSX`.
    - Pasar una extension no soportada en `path`.
    - Suponer que `encoding` aplica a `XLSX`.
    - Esperar tipos nativos al leer `CSV`.

## `from_records(records)`

```python title="Crear una tabla desde memoria"
datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)
```

### Contrato esperado

<div class="grid cards" markdown>

-   __Entrada valida__

    Una lista de diccionarios con el mismo esquema tabular.

-   __Orden estable__

    El orden de columnas queda anclado al primer registro valido.

-   __Normalizacion__

    Los nombres de columnas se normalizan a `str`.

</div>

=== "Valido"

    ```python title="Esquema consistente"
    [
        {"name": "Alice", "age": 30},
        {"age": 25, "name": "Bob"},
    ]
    ```

=== "Invalido"

    ```python title="Esquema no rectangular"
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "country": "MX"},
    ]
    ```

## Ejemplos reales de uso

=== "Preparar fixtures"

    ```python title="Tabla desde memoria para pruebas"
    datatable = DataTableCreator.from_records(
        [
            {"name": "Alice", "active": True},
            {"name": "Bob", "active": False},
        ]
    )
    ```

=== "Cargar un origen y seguir procesando"

    ```python title="Usar la tabla en memoria"
    datatable = DataTableCreator.from_file("people.json")
    first_row = datatable[0].to_dict()
    headers = datatable.column_names
    ```

!!! tip "Cuando elegir `from_records`"
    Es la mejor opcion cuando el origen real de datos ya esta en memoria o cuando quieres preparar fixtures para pruebas sin depender de archivos temporales.

## Buenas practicas de uso

- Usa `from_records` cuando el origen ya este en memoria.
- Usa `from_file` cuando la fuente real sea un archivo del que quieres conservar estructura.
- Mantén un esquema consistente en `records` y agrega columnas nuevas despues sobre la tabla, no antes con filas irregulares.
- Para datos tipados, prefiere `JSON`, `XLSX` o `from_records` frente a `CSV`.
