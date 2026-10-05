# pytabify

**Tabular test data for Python and Robot Framework.**

**English** · [Español](README.es.md)

[User guide](https://angel-valdezzz.github.io/pytabify/) · [Keyword reference](https://angel-valdezzz.github.io/pytabify/keywords/) · [PyPI](https://pypi.org/project/pytabify/) · [Visual examples](https://angel-valdezzz.github.io/pytabify/examples/visual/)

## Features

- Read and save CSV, JSON and XLSX through one API.
- Direct cell access by attribute or key.
- Consistent column updates across all rows.
- Native Python API and an official Robot Framework wrapper.

## Installation

Python 3.10+. openpyxl is installed as a dependency. Robot Framework is needed only for Robot suites.

```bash
pip install pytabify
# Optional for Robot suites:
pip install robotframework
```

## Quick start

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

Read files with `DataTableCreator.from_file("cases.csv")`. For XLSX provide `sheet_name`. Use the official Robot wrapper as follows:

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

Run the Python example first to create cases.json. Robot expressions can use `$row.name` directly; no `.value` property is required.

## Configuration and limitations

No additional configuration is required. CSV values remain strings, including leading zeros and empty cells. JSON, XLSX and from_records retain their supported source types. Rows must share a schema; empty/duplicate headers and inconsistent CSV row lengths are rejected.

Adding a column fills other rows with None. Use brackets for names with spaces or collisions such as `row["to_dict"]`. Each column is a flat field; nested business objects are outside this contract.

Updates change memory only. Saving requires an explicit saver call. If a test fails before saving, that output file is not created: record generated identifiers immediately in separate result storage when required.

## Examples

See the [Python API reference](https://angel-valdezzz.github.io/pytabify/reference/creator/), [Robot examples](https://angel-valdezzz.github.io/pytabify/examples/robot-framework/) and visual before/after table example.

## Development and contribution

```bash
poetry install
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy src/pytabify
poetry run lint-imports
poetry run pytest
poetry run python scripts/build_docs.py
poetry build
```

Submit changes through a pull request with passing checks. Update both documentation languages. Libdoc translations live in `docs/translations/es/libdoc.json`; builds reject missing or stale entries.

## License

MIT. See [LICENSE](LICENSE).
