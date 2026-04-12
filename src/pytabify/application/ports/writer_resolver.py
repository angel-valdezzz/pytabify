from __future__ import annotations

from abc import ABC, abstractmethod

from pytabify.application.ports.table_writer import TableWriter


class WriterResolver(ABC):
    @abstractmethod
    def resolve(self, path: str) -> TableWriter:
        """Resuelve el escritor adecuado para un path dado."""
