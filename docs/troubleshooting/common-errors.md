# Errores comunes

Esta pagina concentra las fallas mas probables al usar `pytabify` y la forma rapida de resolverlas.

## Extension no soportada

!!! failure "Sintoma"
    Intentas leer o guardar un archivo con una extension distinta de `csv`, `json` o `xlsx`.

**Causa**  
Los resolvers seleccionan adaptadores por extension.

**Solucion**  
Usa una extension soportada y consistente con el formato real del archivo.

## `sheet_name` faltante en XLSX

!!! failure "Sintoma"
    Intentas leer un archivo `xlsx` sin indicar el nombre de hoja.

**Causa**  
El reader de Excel exige `sheet_name`.

**Solucion**  

```python title="Lectura correcta de XLSX"
datatable = DataTableCreator.from_file("people.xlsx", sheet_name="People")
```

## Hoja inexistente en XLSX

!!! failure "Sintoma"
    El archivo existe, pero el nombre de hoja no coincide.

**Causa**  
La hoja pedida no aparece en el workbook.

**Solucion**  
Valida el nombre exacto en Excel y vuelve a ejecutar con ese valor.

## Datos no rectangulares en `from_records`

!!! failure "Sintoma"
    `from_records` falla al crear la tabla.

**Causa**  
Al menos una fila no coincide con el esquema del primer registro.

=== "Valido"

    ```python title="Todas las filas comparten schema"
    [
        {"name": "Alice", "age": 30},
        {"age": 25, "name": "Bob"},
    ]
    ```

=== "Invalido"

    ```python title="Schema inconsistente"
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "country": "MX"},
    ]
    ```

**Solucion**  
Normaliza el conjunto antes de construir el `DataTable` o agrega las columnas nuevas mediante mutacion controlada sobre la tabla ya creada.

## Ruta inexistente

!!! failure "Sintoma"
    La carga falla aunque el formato es correcto.

**Causa**  
El archivo no existe en la ruta entregada.

**Solucion**  
Revisa ruta absoluta o relativa, directorio de ejecucion y permisos del proceso.

## Diferencia de tipos al leer CSV

!!! warning "Sintoma"
    Un valor numerico llega como texto despues de leer `CSV`.

**Causa**  
`CSV` no preserva tipos nativos de la misma manera que `JSON` o `XLSX`.

**Solucion**  
Si el flujo depende de tipos, usa `JSON`, `XLSX` o crea la tabla con `from_records`.

## Acceso a columna inexistente

!!! warning "Sintoma"
    Leer `datatable[0]["country"]` o `datatable[0].country` falla.

**Causa**  
La columna no existe en el esquema actual.

**Solucion**  
Agrega la columna primero con una mutacion valida:

```python title="Expandir el esquema"
datatable[0]["country"] = "MX"
```

??? info "Regla util"
    Si agregas una columna en una fila, `pytabify` la propaga al resto con `None`. Ese es el camino esperado para enriquecer una tabla ya valida.
