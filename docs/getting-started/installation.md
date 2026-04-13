# Instalacion

Instala `pytabify` con el camino que corresponda a tu uso. Esta pagina cubre prerequisitos, pasos de instalacion, verificacion inicial y errores frecuentes.

## Prerequisitos

<div class="grid cards" markdown>

-   __Python__

    `pytabify` requiere `Python >= 3.10`.

-   __pip o Poetry__

    Usa `pip` si solo vas a consumir la libreria. Usa `poetry` si vas a desarrollar o iterar en la documentacion del proyecto.

-   __openpyxl__

    Se instala como dependencia del paquete y habilita lectura y escritura de `XLSX`.

</div>

## Instalacion paso a paso

=== "Usuario"

    ```bash title="1. Instalar con pip"
    pip install pytabify
    ```

    ```bash title="2. Verificar la instalacion"
    python -c "from pytabify import DataTableCreator, DataTableSaver; print('ok')"
    ```

=== "Desarrollo"

    ```bash title="1. Instalar dependencias con Poetry"
    poetry install
    ```

    ```bash title="2. Verificar el entorno"
    poetry run python -c "from pytabify import DataTableCreator, DataTableSaver; print('ok')"
    ```

    ```bash title="3. Levantar la documentacion local"
    poetry run mkdocs serve
    ```

## Configuracion inicial

`pytabify` no requiere archivo de configuracion, variables de entorno ni bootstrap adicional para empezar a usar la API publica.

!!! note "Que si necesitas preparar"
    Lo unico que debes tener listo es el origen de datos con el que vas a trabajar: un archivo `csv`, `json` o `xlsx`, o una lista de diccionarios en memoria.

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

## Comandos basicos

| Comando | Cuando usarlo |
| --- | --- |
| `pip install pytabify` | instalar la libreria para consumo |
| `poetry install` | preparar el entorno de desarrollo |
| `python -c "from pytabify import DataTableCreator; print('ok')"` | verificar instalacion minima |
| `poetry run mkdocs serve` | iterar localmente sobre la documentacion |
| `poetry run mkdocs build` | validar que el sitio compila |

## Ejemplos de ejecucion

=== "Consumo simple"

    ```bash title="Instalar y validar"
    pip install pytabify
    python -c "from pytabify import DataTableCreator; print('ok')"
    ```

=== "Entorno del proyecto"

    ```bash title="Preparar repo y levantar docs"
    poetry install
    poetry run mkdocs serve
    ```

## Parametros importantes

Aunque la instalacion no expone muchos parametros propios, estos son los mas relevantes cuando empieces a ejecutar la libreria:

| Parametro | Donde aparece | Para que sirve |
| --- | --- | --- |
| `path` | `DataTableCreator.from_file(...)` | indica el archivo de entrada |
| `sheet_name` | lectura de `XLSX` | selecciona la hoja a leer |
| `encoding` | lectura y escritura de `CSV` o `JSON` | controla codificacion del archivo |

??? info "Cuando mirar estos parametros"
    Si la libreria ya instala bien pero el primer flujo falla al cargar o guardar archivos, casi siempre el problema real esta en `path`, `sheet_name` o `encoding`.

## Dependencias de desarrollo relevantes

| Dependencia | Para que sirve |
| --- | --- |
| `pytest` | pruebas unitarias y de aceptacion |
| `ruff` | lint y formato |
| `mypy` | chequeo estatico |
| `mkdocs-material` | sitio tecnico de documentacion |

??? warning "Entorno sin dependencias de desarrollo"
    Si `poetry run mkdocs build` falla porque `mkdocs` no existe, el entorno se creo sin el grupo de desarrollo. Reinstala con `poetry install`.

## Errores frecuentes de instalacion o ejecucion

!!! warning "Python incompatible"
    Si el entorno usa una version menor a `3.10`, la instalacion o la ejecucion puede fallar. Verifica la version activa con `python --version`.

!!! warning "`mkdocs` no encontrado"
    Si `poetry run mkdocs build` falla, el entorno no tiene dependencias de desarrollo instaladas. Ejecuta `poetry install`.

!!! warning "Lectura de XLSX sin `sheet_name`"
    La libreria se instala bien, pero el flujo de lectura falla si intentas abrir un `xlsx` sin indicar la hoja.

!!! warning "Extension no soportada"
    `pytabify` solo resuelve `csv`, `json` y `xlsx`. Si pasas otra extension, el problema no es de instalacion sino del formato de entrada.

## Siguiente paso

[Ir al inicio rapido](quickstart.md){ .md-button .md-button--primary }
[Ver ejemplos reales](../examples/python.md){ .md-button }
