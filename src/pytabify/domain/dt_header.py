from dataclasses import dataclass


@dataclass(frozen=True)
class DTHeader:
    """Representa un encabezado de columna dentro del esquema de la tabla."""

    name: str
    index: int
