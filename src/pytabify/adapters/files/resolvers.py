from __future__ import annotations

from pathlib import Path

from pytabify.adapters.files.errors import FileExtensionException
from pytabify.adapters.files.formats import FileFormats
from pytabify.adapters.files.readers import (
    CSVFileReadingAdapter,
    JSONFileReadingAdapter,
    XLSXReadingAdapter,
)
from pytabify.adapters.files.writers import (
    CsvFileWritingAdapter,
    JsonFileWritingAdapter,
    XlsxFileWritingAdapter,
)
from pytabify.application.ports import ReaderResolver, TableReader, TableWriter, WriterResolver


class FileReaderResolver(ReaderResolver):
    def resolve(self, path: str) -> TableReader:
        extension = Path(path).suffix
        try:
            file_format = FileFormats(extension)
        except ValueError as exc:
            raise FileExtensionException(f"La extension {extension} no es valida.") from exc

        mapping = {
            FileFormats.CSV: CSVFileReadingAdapter(),
            FileFormats.JSON: JSONFileReadingAdapter(),
            FileFormats.XLSX: XLSXReadingAdapter(),
        }
        return mapping[file_format]


class FileWriterResolver(WriterResolver):
    def resolve(self, path: str) -> TableWriter:
        extension = Path(path).suffix
        try:
            file_format = FileFormats(extension)
        except ValueError as exc:
            raise FileExtensionException(f"La extension {extension} no es valida.") from exc

        mapping = {
            FileFormats.CSV: CsvFileWritingAdapter(),
            FileFormats.JSON: JsonFileWritingAdapter(),
            FileFormats.XLSX: XlsxFileWritingAdapter(),
        }
        return mapping[file_format]
