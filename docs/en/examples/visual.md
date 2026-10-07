---
tags:
  - Usage
---

# Visual examples

This example shows the same in-memory transformation as the quick start. A new column is added to every row; only the selected row receives its value.

## Before

| name | age |
| --- | --- |
| Alice | 30 |
| Bob | 25 |

```python
table[0]["country"] = "MX"
```

## After

| name | age | country |
| --- | --- | --- |
| Alice | 30 | MX |
| Bob | 25 | `None` |

Saving as CSV represents the second row's empty value as an empty cell. JSON uses null. Updating the table alone does not save a file.

[Complete executable example](../getting-started/quickstart.md){ .md-button .md-button--primary }
