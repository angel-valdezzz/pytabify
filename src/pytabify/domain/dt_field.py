from typing import Any


class DTField:
    """Representa una celda dentro de una fila tabular."""

    def __init__(self, name: str, value: Any, index: int):
        self._name = str(name)
        self._value = value
        self._index = index

    def __str__(self):
        return "" if self._value is None else str(self._value)

    @property
    def is_none(self):
        return self._value is None

    @property
    def is_empty(self):
        return self._value == ""

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def index(self):
        return self._index

    def __len__(self):
        return self.length

    @property
    def length(self):
        return 0 if self._value is None else len(str(self._value))

    def set_value(self, value: Any):
        self._value = value

    def set_index(self, index: int):
        self._index = index
