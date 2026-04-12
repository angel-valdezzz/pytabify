from abc import ABC, abstractmethod
from pytabify.domain.data_table import DataTable

class SavingStrategy(ABC):
    """SavingStrategy"""
    @staticmethod
    @abstractmethod
    def save(datatable: DataTable, path: str, encoding: str):
        """save"""
