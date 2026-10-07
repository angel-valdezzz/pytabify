---
tags:
  - Uso
---

# Ejemplos visuales

Este ejemplo muestra la misma transformación en memoria del uso rápido. Una columna nueva se incorpora a todas las filas; solo la fila seleccionada recibe su valor.

## Antes

| name | age |
| --- | --- |
| Alice | 30 |
| Bob | 25 |

```python
table[0]["country"] = "MX"
```

## Después

| name | age | country |
| --- | --- | --- |
| Alice | 30 | MX |
| Bob | 25 | `None` |

Al guardar CSV, el valor vacío de la segunda fila se representa como una celda vacía. JSON utiliza null. Actualizar la tabla por sí solo no guarda un archivo.

[Ejemplo ejecutable completo](../getting-started/quickstart.md){ .md-button .md-button--primary }
