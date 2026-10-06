# pytabify

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo-wordmark-dark.svg">
  <img src="docs/assets/logo-wordmark.svg" alt="Pytabify" width="380">
</picture>

**Datos tabulares para pruebas en Python y Robot Framework.**

[English](README.md) · **Español**

[Manual de usuario ↗](https://angel-valdezzz.github.io/pytabify/es/) · [Referencia de keywords ↗](https://angel-valdezzz.github.io/pytabify/es/keywords/) · [PyPI ↗](https://pypi.org/project/pytabify/) · [Ejemplos visuales ↗](https://angel-valdezzz.github.io/pytabify/es/examples/visual/)


[![PyPI](https://img.shields.io/pypi/v/pytabify?logo=pypi)](https://pypi.org/project/pytabify/)
![Python](https://img.shields.io/pypi/pyversions/pytabify?logo=python)
![Robot Framework](https://img.shields.io/badge/Robot_Framework-compatible-00A6A6?logo=robotframework)
[![License](https://img.shields.io/github/license/angel-valdezzz/pytabify)](LICENSE)
[![CI](https://github.com/angel-valdezzz/pytabify/actions/workflows/ci.yml/badge.svg)](https://github.com/angel-valdezzz/pytabify/actions/workflows/ci.yml)

## Funcionalidades

- Lectura y escritura CSV, JSON y XLSX mediante una API.
- Acceso directo a celdas por atributo o clave.
- Actualización consistente de columnas en todas las filas.
- API Python y wrapper oficial para Robot Framework.

## Instalación

Python 3.10+. openpyxl se instala como dependencia. Robot Framework solo se necesita para suites Robot.

```bash
pip install pytabify
# Optional for Robot suites:
pip install robotframework
```

## Uso rápido

```python
from pytabify import DataTableCreator, DataTableSaver

table = DataTableCreator.from_records([
    {"name": "Ana", "active": True},
    {"name": "Luis", "active": False},
])
assert table[0].name == table[0]["name"] == "Ana"
assert table[0].active is True

table[0].folio = "F-001"
assert table[1].folio is None
DataTableSaver.into_json(table, "cases.json")
```

Lee archivos con `DataTableCreator.from_file("cases.csv")`. Para XLSX indica `sheet_name`. Utiliza el wrapper oficial de Robot así:

```robotframework
*** Settings ***
Library    Pytabify

*** Test Cases ***
Read a case
    ${table}=    Pytabify.Create Data Table From File    cases.json
    ${row}=    Pytabify.Get Data Table Row    ${table}    0
    Should Be Equal    ${row.name}    Ana
    ${table}=    Pytabify.Set Data Table Value    ${table}    0    folio    F-002
    Pytabify.Save Data Table To Json    ${table}    updated.json
```

Ejecuta primero el ejemplo Python para crear cases.json. Las expresiones Robot pueden usar `$row.name` directamente; no requieren una propiedad `.value`.

## Configuración y limitaciones

No requiere configuración adicional. Los valores CSV conservan texto, incluidos ceros iniciales y celdas vacías. JSON, XLSX y from_records conservan los tipos compatibles de su origen. Las filas deben compartir esquema; se rechazan encabezados vacíos/repetidos y longitudes de fila CSV inconsistentes.

Una columna nueva rellena las demás filas con None. Usa corchetes para nombres con espacios o coincidencias con métodos como `row["to_dict"]`. Cada columna es un campo plano; los objetos de negocio anidados quedan fuera de este contrato.

Actualizar cambia solo la memoria. Guardar exige una llamada explícita. Si una prueba falla antes de guardar, ese archivo no se crea: registra los identificadores generados inmediatamente en otro almacenamiento de resultados cuando lo necesites.

## Ejemplos

Consulta la [referencia de API Python ↗](https://angel-valdezzz.github.io/pytabify/es/reference/creator/), los [ejemplos Robot ↗](https://angel-valdezzz.github.io/pytabify/es/examples/robot-framework/) y el ejemplo visual de tabla antes/después.

## Desarrollo y contribución

```bash
poetry install
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy src/pytabify
poetry run lint-imports
poetry run pytest
poetry run python docs/scripts/build_docs.py
poetry build
```

Envía los cambios mediante un pull request con verificaciones aprobadas. Actualiza ambos idiomas. Las traducciones de Libdoc viven en `docs/translations/es/libdoc.json`; la compilación rechaza entradas faltantes o desactualizadas.

## Licencia

MIT. Consulta [LICENSE](LICENSE).
