from typing import Any


class DTField:
    """Representa una celda dentro de una fila tabular."""

    def __init__(self, name: str, value: Any, index: int) -> None:
        self._name = str(name)
        self._value = value
        self._index = index

    def __str__(self) -> str:
        return "" if self._value is None else str(self._value)

    @property
    def is_none(self) -> bool:
        return self._value is None

    @property
    def is_empty(self) -> bool:
        return bool(self._value == "")

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> Any:
        return self._value

    @property
    def index(self) -> int:
        return self._index

    def __len__(self) -> int:
        return self.length

    @property
    def length(self) -> int:
        return 0 if self._value is None else len(str(self._value))

    def set_value(self, value: Any) -> None:
        self._value = value

    def set_index(self, index: int) -> None:
        self._index = index
