## pytabify

**Tabify your data, Python-style**

*Tabula tus datos con Python*

`pytabify` es una librería ligera para cargar, validar y persistir datos tabulares desde `CSV`, `JSON` y `XLSX`. Está pensada para automatización de pruebas, fixtures, scripts y flujos simples de datos en Python y Robot Framework.

## Documentation

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-0f766e?style=flat-square)](https://angel-valdezzz.github.io/pytabify/)

Puedes consultar la documentación completa aquí:

https://angel-valdezzz.github.io/pytabify/

## Características

- Soporte para múltiples formatos: `CSV`, `JSON` y `XLSX`.
- Contrato tabular estable con columnas ordenadas y consistentes.
- Preserva tipos nativos en memoria.
- Wrapper oficial para Robot Framework.
- Exportación flexible a múltiples formatos.

## Arquitectura

El paquete sigue una separación basada en clean architecture y arquitectura hexagonal:

- `domain`: entidades y reglas del modelo tabular.
- `application`: puertos y casos de uso.
- `adapters`: adaptadores concretos para archivos y Robot Framework.
- `creator.py` y `saver.py`: fachadas públicas enfocadas en la API de uso.

## Instalación

```bash
pip install pytabify
```

## Uso básico

### Crear un DataTable desde archivo

```python
from pytabify import DataTableCreator

datatable = DataTableCreator.from_file("data.json")
datatable = DataTableCreator.from_file("data.csv", encoding="utf-8")
datatable = DataTableCreator.from_file("data.xlsx", sheet_name="Hoja1")
```

### Acceder y modificar datos

```python
row = datatable[0]
print(row.name.value)

for row in datatable:
    print(row.to_dict())

row["age"] = 31
row.country = "MX"
```

### Guardar datos

```python
from pytabify import DataTableSaver

DataTableSaver.into_csv(datatable, "output.csv")
DataTableSaver.into_json(datatable, "output.json")
DataTableSaver.into_xlsx(datatable, "output.xlsx")
```

## Integración con pruebas automatizadas

### Python

```python
from pytabify import DataTableCreator

datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)

assert datatable[0].name.value == "Alice"
assert datatable[1].age.value == 25
```

### Robot Framework

```robotframework
*** Settings ***
Library    pytabify.robot.PyTabifyLibrary    WITH NAME    PyTabify

*** Test Cases ***
Leer datos desde CSV
    ${datatable}=    PyTabify.Create Data Table From File    path=data.csv
    Should Not Be Empty    ${datatable}

Validar un campo especifico
    ${row}=    PyTabify.Get Data Table Row    ${datatable}    0
    Should Be Equal As Strings    ${row.name}    Alice
    Should Be Equal As Integers    ${row}[age]    30
```

## Pruebas

```bash
poetry install
poetry run pytest
poetry run pytest utests -q
poetry run pytest atests -q --no-cov
poetry run ruff check .
poetry run ruff format .
poetry run mypy src/pytabify
poetry run lint-imports
```

## Licencia

Este proyecto está bajo la licencia `MIT`. Consulta el archivo `LICENSE` para más detalles.
