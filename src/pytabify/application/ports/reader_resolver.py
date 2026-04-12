from __future__ import annotations

from abc import ABC, abstractmethod

from pytabify.application.ports.table_reader import TableReader


class ReaderResolver(ABC):
    @abstractmethod
    def resolve(self, path: str) -> TableReader:
        """Resuelve el lector adecuado para un path dado."""
