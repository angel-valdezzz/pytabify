# DataTable and rows

A DataTable contains flat rows and ordered columns. Reading a cell returns its value directly without an intermediate object.

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

Use brackets for spaces, special characters and names colliding with row methods, such as `row["to_dict"]`. Missing columns raise KeyError by key or AttributeError by attribute.

## Update data

```python
row["nombre"] = "Andrea"
row.folio = "F-001"
assert table[1].folio is None
assert table.column_names == ("nombre", "activo", "folio")
```

Updating an existing column changes only that cell. Adding a column expands the full schema and fills other rows with None. A missing row index raises IndexError without changing the schema.

## Iterate and export

```python
for row in table:
    print(row.nombre, row.to_dict())

assert list(table[0]) == ["nombre", "activo", "folio"]
assert len(table) == 2
print(table.to_dict())
```

| Operation | Result |
| --- | --- |
| `table[index]` or `table.row(index)` | Row at that position |
| `row.field` or `row["field"]` | Cell value |
| `row.to_dict()` | Ordered-column dictionary |
| `table.column_names` | Tuple of column names |
| `table.headers()` | Header name/index objects |
| `table.to_dict()` | List of dictionaries |

CSV values are strings: an empty cell is `""` and `"01000"` keeps its leading zero. from_records, JSON and XLSX keep their source's supported types. pytabify does not build nested objects or interpret headers as attribute paths.

[Creating tables](creator.md){ .md-button .md-button--primary }
[Saving tables](saver.md){ .md-button }
