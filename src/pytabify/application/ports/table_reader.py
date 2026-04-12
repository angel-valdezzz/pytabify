from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class TableReader(ABC):
    @abstractmethod
    def read(self, path: str, **kwargs) -> list[dict[str, Any]]:
        """Lee registros tabulares desde una fuente externa."""
