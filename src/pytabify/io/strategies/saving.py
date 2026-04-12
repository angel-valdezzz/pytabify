from openpyxl import Workbook

from pytabify.adapters.files.writers import xlsx_file_writing_adapter
from pytabify.adapters.files.writers import (
    CsvFileWritingAdapter,
    JsonFileWritingAdapter,
    XlsxFileWritingAdapter,
)
from pytabify.domain.data_table import DataTable
from pytabify.io.interfaces.save import SavingStrategy

class JsonFileSavingStrategy(SavingStrategy):
    """JsonFileSavingStrategy"""
    @staticmethod
    def save(datatable: DataTable, path: str, encoding: str):
        JsonFileWritingAdapter().write(datatable, path, encoding=encoding)

class CsvFileSavingStrategy(SavingStrategy):
    """CsvFileSavingStrategy"""
    @staticmethod
    def save(datatable: DataTable, path: str, encoding: str):
        CsvFileWritingAdapter().write(datatable, path, encoding=encoding)

class XlsxFileSavingStrategy(SavingStrategy):
    """XlsxFileSavingStrategy"""
    @staticmethod
    def save(datatable: DataTable, path: str, encoding: str):
        xlsx_file_writing_adapter.Workbook = Workbook
        XlsxFileWritingAdapter().write(datatable, path, encoding=encoding)
