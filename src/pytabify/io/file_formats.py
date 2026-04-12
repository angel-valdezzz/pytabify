from enum import Enum

from pytabify.io.interfaces.read import ReadingStrategy
from pytabify.io.strategies.reading import CSVFileReadingStrategy, JSONFileReadingStrategy, XLSXReadingStrategy


class FileFormats(Enum):
    """Compatibilidad legacy para resolución de estrategias de lectura."""

    CSV = ".csv"
    JSON = ".json"
    XLSX = ".xlsx"

    def get_strategy(self) -> type[ReadingStrategy]:
        mapping = {
            FileFormats.CSV: CSVFileReadingStrategy,
            FileFormats.JSON: JSONFileReadingStrategy,
            FileFormats.XLSX: XLSXReadingStrategy,
        }
        return mapping[self]
