# Instalacion

Instala `pytabify` con el camino que corresponda a tu uso.

=== "Usuario"

    ```bash title="Instalacion con pip"
    pip install pytabify
    ```

=== "Desarrollo"

    ```bash title="Instalacion del entorno con Poetry"
    poetry install
    ```

## Requisitos

<div class="grid cards" markdown>

-   __Python__

    `pytabify` requiere `Python >= 3.10`.

-   __Dependencia principal__

    `openpyxl` se usa para lectura y escritura de `XLSX`.

-   __Stack de documentacion__

    El proyecto ahora integra `MkDocs Material` desde dependencias de desarrollo.

</div>

## Verificacion minima

=== "Paquete instalado"

    ```bash title="Comprobar import basico"
    python -c "from pytabify import DataTableCreator, DataTableSaver; print('ok')"
    ```

=== "Sitio de documentacion"

    ```bash title="Levantar documentacion local"
    poetry run mkdocs serve
    ```

    ```bash title="Generar el sitio estatico"
    poetry run mkdocs build
    ```

!!! note "Cuando usar cada comando"
    Usa `mkdocs serve` cuando quieras iterar en contenido y `mkdocs build` para validar que la navegacion, extensiones y enlaces compilan sin errores.

## Dependencias de desarrollo relevantes

| Dependencia | Para que sirve |
| --- | --- |
| `pytest` | pruebas unitarias y de aceptacion |
| `ruff` | lint y formato |
| `mypy` | chequeo estatico |
| `mkdocs-material` | sitio tecnico de documentacion |

??? warning "Entorno sin dependencias de desarrollo"
    Si `poetry run mkdocs build` falla porque `mkdocs` no existe, el entorno se creo sin el grupo de desarrollo. Reinstala con `poetry install`.

## Siguiente paso

[Ir al inicio rapido](quickstart.md){ .md-button .md-button--primary }
[Ver ejemplos reales](../examples/python.md){ .md-button }
