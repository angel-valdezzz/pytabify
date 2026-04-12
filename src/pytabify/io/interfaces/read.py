from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ReadingStrategy(ABC):
    """Contrato legacy para estrategias de lectura."""

    def __init__(self, path: str, **kwargs):
        self._path = path
        self._kwargs = kwargs

    @abstractmethod
    def read(self) -> list[dict[str, Any]]:
        """read"""
