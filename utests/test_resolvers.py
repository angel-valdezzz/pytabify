import pytest

from pytabify.adapters.files.errors import FileExtensionException
from pytabify.adapters.files.readers import (
    CSVFileReadingAdapter,
    JSONFileReadingAdapter,
    XLSXReadingAdapter,
)
from pytabify.adapters.files.resolvers import FileReaderResolver, FileWriterResolver
from pytabify.adapters.files.writers import (
    CsvFileWritingAdapter,
    JsonFileWritingAdapter,
    XlsxFileWritingAdapter,
)


@pytest.mark.parametrize(
    ("path", "reader_type"),
    [
        ("input.csv", CSVFileReadingAdapter),
        ("input.json", JSONFileReadingAdapter),
        ("input.xlsx", XLSXReadingAdapter),
    ],
)
def test_file_reader_resolver_returns_expected_adapter(path, reader_type):
    assert isinstance(FileReaderResolver().resolve(path), reader_type)


@pytest.mark.parametrize(
    ("path", "writer_type"),
    [
        ("output.csv", CsvFileWritingAdapter),
        ("output.json", JsonFileWritingAdapter),
        ("output.xlsx", XlsxFileWritingAdapter),
    ],
)
def test_file_writer_resolver_returns_expected_adapter(path, writer_type):
    assert isinstance(FileWriterResolver().resolve(path), writer_type)


@pytest.mark.parametrize("resolver", [FileReaderResolver(), FileWriterResolver()])
def test_file_resolvers_reject_unknown_extensions(resolver):
    with pytest.raises(FileExtensionException):
        resolver.resolve("unsupported.txt")
