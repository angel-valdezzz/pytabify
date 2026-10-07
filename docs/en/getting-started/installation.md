---
tags:
  - Usage
---

# Installation

Choose the installation route for your use. This page covers prerequisites, minimal steps, verification and common errors.

## Prerequisites

- **Python 3.10+**.
- **pip** to use the package, or **Poetry** to develop it and its documentation.
- **openpyxl**, installed as a package dependency for XLSX reading and writing.
- **Robot Framework**, installed separately if you use the Robot wrapper.

## Step-by-step installation

=== "User"

    ```bash title="1. Install with pip"
    pip install pytabify
    ```

    ```bash title="2. Verify installation"
    python -c "from pytabify import DataTableCreator, DataTableSaver; print('ok')"
    ```

=== "Development"

    ```bash title="1. Install dependencies with Poetry"
    poetry install
    ```

    ```bash title="2. Verify the environment"
    poetry run python -c "from pytabify import DataTableCreator, DataTableSaver; print('ok')"
    ```

    ```bash title="3. Preview documentation"
    poetry run mkdocs serve
    ```

## Initial configuration

No configuration file, environment variables or extra bootstrap is required. Prepare a CSV, JSON or XLSX file, or a list of dictionaries in memory.

## Basic commands

| Command | Purpose |
| --- | --- |
| `pip install pytabify` | Install the package |
| `poetry install` | Prepare development dependencies |
| `python -c "from pytabify import DataTableCreator; print('ok')"` | Verify minimal installation |
| `poetry run mkdocs serve` | Preview the English source pages |
| `poetry run python docs/scripts/build_docs.py` | Validate the complete bilingual site and Libdoc |

## Minimal verification

=== "Installed package"

    ```bash title="Check basic import"
    python -c "from pytabify import DataTableCreator, DataTableSaver; print('ok')"
    ```

=== "Documentation"

    ```bash title="Preview documentation"
    poetry run mkdocs serve
    ```

    ```bash title="Build the static site"
    poetry run mkdocs build
    ```

Use `mkdocs serve` to iterate on one language. Build the complete site with `docs/scripts/build_docs.py` and serve `site/` with `python -m http.server 8000 --directory site` to preview both languages.

## Execution examples

=== "Package use"

    ```bash title="Install and verify"
    pip install pytabify
    python -c "from pytabify import DataTableCreator; print('ok')"
    ```

=== "Project environment"

    ```bash title="Prepare the repository and preview docs"
    poetry install
    poetry run mkdocs serve
    ```

## Important parameters

| Parameter | Used by | Purpose |
| --- | --- | --- |
| `path` | `DataTableCreator.from_file(...)` | Input file |
| `sheet_name` | XLSX reading | Sheet selection |
| `encoding` | CSV/JSON reading and writing | File encoding |

When installation works but loading or saving fails, check these parameters first.

Development dependencies include pytest (unit/acceptance tests), Ruff (lint/format), mypy (static types) and mkdocs-material (documentation). If MkDocs is unavailable, install the development group using `poetry install`.

## Common installation or execution errors

- **Incompatible Python:** check `python --version`; versions below 3.10 are unsupported.
- **MkDocs missing:** run `poetry install` with development dependencies.
- **XLSX without sheet_name:** provide the exact workbook sheet name.
- **Unsupported extension:** only CSV, JSON and XLSX are resolved; this is a format error rather than an installation error.

[Quick start](quickstart.md){ .md-button .md-button--primary }
[Python examples](../examples/python.md){ .md-button }
