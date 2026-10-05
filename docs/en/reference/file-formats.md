# Supported formats

pytabify moves tabular data between memory and files using one stable contract.

| Format | Read | Write | Types | Main consideration |
| --- | --- | --- | --- | --- |
| CSV | Yes | Yes | Limited | Reading returns text |
| JSON | Yes | Yes | Supported simple types | Useful for API fixtures and round-trips |
| XLSX | Yes | Yes | Based on cell content | Reading requires sheet_name |

## When to choose each format

- **CSV:** fast interoperability and flat files.
- **JSON:** supported native types and simple fixtures.
- **XLSX:** users whose natural input/output is Excel.

## Practical rules

=== "CSV"

    - Values are strings: 01000 remains `"01000"`; empty cells are `""`.
    - Empty/duplicate headers and inconsistent row lengths are rejected.
    - Use encoding="utf-8" unless a specific source requires otherwise.
    - It is less expressive for None and booleans.

=== "JSON"

    - Useful for tests, fixtures and simple round-trips.
    - Preserves numbers, booleans and null better than CSV.

=== "XLSX"

    - Reading requires sheet_name.
    - The first row contains headers.
    - Useful when source data already lives in Excel.

!!! warning "Correct extension"
    Infrastructure resolvers use file extensions. Renaming to an unsupported extension makes reading/writing fail.
