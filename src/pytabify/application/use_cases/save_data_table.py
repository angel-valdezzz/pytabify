from pytabify.application.ports.writer_resolver import WriterResolver
from pytabify.domain.data_table import DataTable


class SaveDataTable:
    """Caso de uso para persistir una tabla hacia una salida externa."""

    def __init__(self, writer_resolver: WriterResolver):
        self._writer_resolver = writer_resolver

    def execute(self, datatable: DataTable, path: str, encoding: str = "utf-8"):
        writer = self._writer_resolver.resolve(path)
        writer.write(datatable, path, encoding=encoding)
