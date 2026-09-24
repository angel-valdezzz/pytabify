# DataTable y filas

Una `DataTable` contiene filas planas y una lista ordenada de columnas. La lectura de una celda entrega el **valor directamente**, sin un objeto intermedio.

```python
from pytabify import DataTableCreator

table = DataTableCreator.from_records([
    {"nombre": "Ana", "activo": True},
    {"nombre": "Luis", "activo": False},
])
row = table[0]

assert row.nombre == "Ana"
assert row["nombre"] == "Ana"
assert row.activo is True
assert table.row(1).nombre == "Luis"
```

Usa corchetes para nombres con espacios o caracteres especiales y para columnas que coincidan con métodos de la fila, por ejemplo `row["to_dict"]`. Una columna ausente produce `KeyError` entre corchetes o `AttributeError` por atributo.

## Actualizar datos

```python
row["nombre"] = "Andrea"
row.folio = "F-001"
assert table[1].folio is None
assert table.column_names == ("nombre", "activo", "folio")
```

Actualizar una columna existente cambia solo esa celda. Agregar una columna la incorpora al esquema de todas las filas y completa las demás con `None`. Un índice de fila inexistente produce `IndexError` y no modifica el esquema.

## Recorrer y exportar

```python
for row in table:
    print(row.nombre, row.to_dict())

assert list(table[0]) == ["nombre", "activo", "folio"]
assert len(table) == 2
print(table.to_dict())
```

| Operación | Resultado |
| --- | --- |
| `table[index]` o `table.row(index)` | Fila en esa posición |
| `row.campo` o `row["campo"]` | Valor de la celda |
| `row.to_dict()` | Diccionario con las columnas en orden |
| `table.column_names` | Tupla de nombres de columna |
| `table.headers()` | Objetos con nombre e índice del encabezado |
| `table.to_dict()` | Lista de diccionarios |

Los CSV se leen como texto: una celda vacía es `""` y `"01000"` conserva el cero. En `from_records`, JSON y XLSX, los valores conservan los tipos propios de cada origen. Pytabify no construye objetos anidados ni interpreta un encabezado como una ruta de atributos.

[Crear tablas](creator.md){ .md-button .md-button--primary }
[Guardar tablas](saver.md){ .md-button }
