from pytabify.adapters.files.resolvers import FileReaderResolver, FileWriterResolver
from pytabify.application.use_cases.create_data_table_from_file import CreateDataTableFromFile
from pytabify.application.use_cases.create_data_table_from_records import CreateDataTableFromRecords
from pytabify.application.use_cases.save_data_table import SaveDataTable


def build_create_table_from_file_use_case() -> CreateDataTableFromFile:
    return CreateDataTableFromFile(reader_resolver=FileReaderResolver())


def build_create_table_from_records_use_case() -> CreateDataTableFromRecords:
    return CreateDataTableFromRecords()


def build_save_table_use_case() -> SaveDataTable:
    return SaveDataTable(writer_resolver=FileWriterResolver())
