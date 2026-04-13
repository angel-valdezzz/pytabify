# Formatos soportados

`pytabify` resuelve un problema muy concreto: mover datos tabulares entre memoria y archivos con un contrato estable.

## Vista rapida

| Formato | Leer | Guardar | Conserva tipos | Consideracion principal |
| --- | --- | --- | --- | --- |
| `CSV` | Si | Si | Limitado | todo entra como texto al leer |
| `JSON` | Si | Si | Si, para tipos simples | buen round-trip para APIs y fixtures |
| `XLSX` | Si | Si | Si, segun el contenido de celdas | requiere `sheet_name` al leer |

## Cuándo usar cada formato

<div class="grid cards" markdown>

-   __CSV__

    Mejor cuando necesitas interoperar rapido con otras herramientas o entregar un archivo plano.

-   __JSON__

    Mejor cuando quieres preservar estructura y tipos simples con friccion baja.

-   __XLSX__

    Mejor cuando el origen o destino natural del usuario es Excel.

</div>

## Reglas practicas por formato

=== "CSV"

    - El reader devuelve valores como texto.
    - Usa `encoding="utf-8"` salvo necesidad puntual.
    - Es el formato menos expresivo para `None` y booleanos.

=== "JSON"

    - Funciona bien para pruebas, fixtures y round-trip simple.
    - Mantiene mejor enteros, booleanos y `null`.

=== "XLSX"

    - Necesita `sheet_name` para leer.
    - La primera fila se interpreta como encabezado.
    - Es buena opcion cuando tu fuente ya vive en Excel.

!!! warning "Extension valida"
    Los resolvers de infraestructura trabajan por extension de archivo. Si cambias la extension manualmente a un formato no soportado, la lectura o escritura fallara.
