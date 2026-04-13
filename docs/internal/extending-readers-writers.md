# Extender formatos

Si agregas un nuevo formato, el cambio debe respetar la separacion actual entre dominio, casos de uso y adaptadores.

## Donde tocar

| Area | Rol |
| --- | --- |
| `src/pytabify/application/ports` | contratos de lectura y escritura |
| `src/pytabify/application/use_cases` | flujos de carga y persistencia |
| `src/pytabify/adapters/files/readers` | readers concretos por formato |
| `src/pytabify/adapters/files/writers` | writers concretos por formato |
| `src/pytabify/adapters/files/resolvers.py` | resolucion por extension |

## Flujo recomendado

1. Implementa un reader o writer concreto en `adapters/files`.
2. Registra el formato en el resolver correspondiente.
3. Mantén intacto el contrato del dominio.
4. Agrega pruebas unitarias del adaptador y al menos un flujo end-to-end.

=== "Reader existente"

    - resuelve archivo por extension;
    - convierte origen externo a `list[dict[str, Any]]`;
    - deja al dominio validar el contrato tabular.

=== "Nuevo reader"

    - debe seguir el mismo contrato de salida;
    - no debe inyectar reglas de negocio en la infraestructura;
    - debe fallar con errores de infraestructura coherentes.

!!! warning "No rompas el contrato del dominio"
    Si tu adaptador produce filas no rectangulares o nombres de columnas inconsistentes, el problema no se arregla en la capa de dominio. El adaptador debe entregar una estructura razonable para que la validacion haga su trabajo.

??? info "Pruebas minimas recomendadas"
    - lectura o escritura exitosa del nuevo formato;
    - error consistente cuando el archivo no existe;
    - error consistente cuando el contenido es invalido;
    - compatibilidad con `DataTableCreator` o `DataTableSaver` a traves de los resolvers.
