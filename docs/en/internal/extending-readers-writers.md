# Extending formats

New formats must preserve the separation between domain, use cases and adapters.

## Where to change

| Area | Role |
| --- | --- |
| `src/pytabify/application/ports` | Reading/writing contracts |
| `src/pytabify/application/use_cases` | Loading and persistence flows |
| `src/pytabify/adapters/files/readers` | Concrete format readers |
| `src/pytabify/adapters/files/writers` | Concrete format writers |
| `src/pytabify/adapters/files/resolvers.py` | Extension-based resolution |

## Recommended flow

1. Implement the reader/writer under adapters/files.
2. Register its format in the corresponding resolver.
3. Preserve the domain contract.
4. Add adapter unit tests and at least one end-to-end flow.

Readers resolve by extension, convert external sources to `list[dict[str, Any]]` and leave tabular validation to the domain. New readers must keep this contract, avoid infrastructure-level business rules and raise consistent infrastructure errors.

!!! warning "Preserve the domain contract"
    Non-rectangular rows or inconsistent column names do not justify weakening domain validation. The adapter must provide a reasonable structure for validation.

Verify successful reading/writing, missing-file errors, invalid-content errors and integration through DataTableCreator/DataTableSaver and the resolvers.
