# pytabify

**Datos tabulares para pruebas en Python y Robot Framework.**

[Documentación completa](https://angel-valdezzz.github.io/pytabify/) · [PyPI](https://pypi.org/project/pytabify/)

pytabify lee CSV, JSON y XLSX como tablas de filas planas. Cada columna es un campo y cada fila permite consultar sus valores directamente: `row.name` o `row["name"]`. Puedes actualizar celdas, añadir columnas y guardar la tabla en cualquiera de los formatos compatibles.

## Instalación

```bash
pip install pytabify
```

Para ejecutar pruebas con Robot Framework, instala también `robotframework` en tu proyecto.

## Un CSV, una tabla

Archivo `casos.csv`:

```csv
nombre,cp,cotizacion
Ana,01000,
Luis,64000,
```

```python
from pytabify import DataTableCreator, DataTableSaver

table = DataTableCreator.from_file("casos.csv")
row = table[0]

assert row.nombre == row["nombre"] == "Ana"
assert row.cp == "01000"  # CSV conserva texto, incluidos los ceros iniciales
assert row.cotizacion == ""

row.cotizacion = "COT-123"
table[1]["cotizacion"] = "COT-456"
DataTableSaver.into_csv(table, "casos_actualizados.csv")
```

La escritura en memoria **no** guarda el archivo automáticamente. Llama a `into_csv` cuando quieras exportar el estado de la tabla. Si una prueba falla antes de esa llamada, ese CSV de salida no se crea; para conservar cada folio en el momento de obtenerlo hace falta un registro de resultados independiente.

## En Robot Framework

```robotframework
*** Settings ***
Library    pytabify.robot.PyTabifyLibrary    WITH NAME    PyTabify

*** Test Cases ***
Leer un caso
    ${table}=    PyTabify.Create Data Table From File    casos.csv
    ${row}=      PyTabify.Get Data Table Row        ${table}    0
    Should Be Equal    ${row.nombre}       Ana
    Should Be Equal    ${row}[cp]           01000
    IF    $row.cotizacion == ''
        Log    Aún no tiene cotización
    END
    ${table}=    PyTabify.Set Data Table Value    ${table}    0    cotizacion    COT-123
    PyTabify.Save Data Table To Csv    ${table}    casos_actualizados.csv
```

En expresiones `IF`, Robot puede evaluar el valor de `$row.cotizacion` directamente; no necesitas una propiedad `.value` ni `Evaluate`.

## Datos desde Python

```python
table = DataTableCreator.from_records(
    [{"nombre": "Ana", "activo": True}, {"nombre": "Luis", "activo": False}]
)
assert table[0].activo is True
table[0]["folio"] = "F-1"
assert table[1].folio is None  # Las columnas nuevas se agregan a todas las filas
```

`from_records` conserva tipos de Python, como `bool`, `int` y `None`. En CSV los valores se leen como cadenas; para un encabezado que no sea identificador de Python, o que coincida con un método como `to_dict`, usa `row["nombre de columna"]`.

## Formatos y reglas

| Entrada | Valores leídos | Opciones |
| --- | --- | --- |
| CSV | Cadenas, también para números y celdas vacías | `encoding="utf-8"` |
| JSON | Tipos representados en JSON | `encoding="utf-8"` |
| XLSX | Tipos entregados por openpyxl | `sheet_name="Hoja1"` |

Las filas deben compartir columnas. Los encabezados vacíos o repetidos y las filas CSV con más o menos celdas se rechazan con un error que identifica el problema. Las columnas se mantienen en orden; agregar una columna asigna `None` a las demás filas.

Consulta la [guía de inicio](https://angel-valdezzz.github.io/pytabify/getting-started/quickstart/), la [API de tablas](https://angel-valdezzz.github.io/pytabify/reference/data-table/) y los [ejemplos de Robot](https://angel-valdezzz.github.io/pytabify/examples/robot-framework/) para más casos.

## Desarrollo

```bash
poetry install
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy src/pytabify
poetry run lint-imports
poetry run pytest
poetry run mkdocs build --strict
```

## Licencia

MIT. Consulta [LICENSE](LICENSE).
