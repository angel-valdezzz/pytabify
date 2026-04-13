class FileError(Exception):
    """Base error for file infrastructure failures."""


class FileNotFoundException(FileError):
    """The requested file does not exist."""


class FileReadingException(FileError):
    """An error occurred while reading a file."""


class FileWritingException(FileError):
    """An error occurred while writing a file."""


class FileExtensionException(FileError):
    """The file extension is not supported."""


class SheetNameHasNotEmptyException(FileError):
    """A sheet name is required to read an XLSX file."""


class SheetNameDoesNotExistException(FileError):
    """The requested sheet does not exist in the XLSX file."""
