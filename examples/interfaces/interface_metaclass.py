"""
Example of an interface which uses a "metaclass" to enforce strict interface implementation.
"""
import logging

LOG = logging.getLogger("examples")


class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class ParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods
    as they are implicitly made available via .__subclasscheck__().

    However, to help my IDE (PyCharm), I declared the interface methods anyway.
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """ Load data source """
        pass

    def extract_text(self, data: str) -> dict:
        """ Extract the text from the data source """
        pass


class PdfParser:
    """
    Extract text from a PDF.

    Strict interface implementation.
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        LOG.info("PdfParser: Loading data from %s/%s", path, file_name)
        return "pdf data"

    def extract_text(self, data: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        LOG.info("PdfParser: Extract data from %s", data[:10])
        return {
            "body": "pdf data"
        }


class EmailParser:
    """
    Extract text from an email.

    *Not* a strict interface implementation.
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        LOG.info("EmailParser: Loading data from %s/%s", path, file_name)
        return "email data"

    def extract_text_from_email(self, data: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        LOG.info("EmailParser: Extract text from email %s", data[:10])
        return {
            "body": data
        }


def parse(parser: ParserInterface, path_name: str, file_name: str) -> dict:
    """
    Parse some data.
    :param parser: Parser passed as an interface.
    :param path_name: Data file's path name.
    :param file_name: Data file's file name.
    :return: Parsed data.
    """
    LOG.info("Parsing %s/%s", path_name, file_name)
    raw_data = parser.load_data_source(path_name, file_name)
    parsed_data = parser.extract_text(raw_data)
    return parsed_data


def interface_with_metaclass() -> None:
    """
    Example of interface implementation with a metaclass.
    :return: None
    """
    LOG.info("---------------------------------------------")
    LOG.info("Running the metaclass-based interface example")
    pdf_parser = PdfParser()
    assert issubclass(PdfParser, ParserInterface) is True
    parsed_pdf = parse(pdf_parser, ".", "data.pdf")
    assert isinstance(parsed_pdf, dict)
    assert parsed_pdf.get("body") is not None
    assert parsed_pdf.get("body") == "pdf data"
    LOG.info("Method resolution order (MRO): %s", str(PdfParser.__mro__))

    email_parser = EmailParser()
    # As expected: EmailParser does not strictly implement the interface.
    assert issubclass(EmailParser, ParserInterface) is False
    try:
        _ = parse(email_parser, ".", "email.txt")
    except AttributeError as e:
        # As expected, the parse function will not find extract_text():l
        LOG.error("Email-parser parse error: %s", e)
    LOG.info("Method resolution order (MRO): %s", str(EmailParser.__mro__))
