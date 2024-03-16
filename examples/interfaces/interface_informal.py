"""
Example of an "informal" interface
"""
import logging

LOG = logging.getLogger("examples")


class InformalParserInterface:
    """
    Interface to load and parse data.
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        LOG.warning("load_data_source: Not implemented; path=%s, file_name=%s", path, file_name)
        raise NotImplementedError

    def extract_text(self, data: str) -> dict:
        """Extract text from the currently loaded file."""
        LOG.warning("extract_text: Not implemented; data=%s", data[:10])
        raise NotImplementedError


class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        return "pdf data"

    def extract_text(self, data: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        return {
            "body": data
        }


class EmailParser(InformalParserInterface):
    """Extract text from an email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        return "email data"

    def extract_text_from_email(self, data: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        return {
            "body": data
        }


def parse(parser: InformalParserInterface, path_name: str, file_name: str) -> dict:
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


def interface_informal() -> None:
    """
    Example of an informal interface.
    :return: None.
    """
    LOG.info("--------------------------------------")
    LOG.info("Running the informal interface example")
    pdf_parser = PdfParser()
    assert issubclass(PdfParser, InformalParserInterface) is True
    parsed_pdf = parse(pdf_parser, ".", "data.pdf")
    assert isinstance(parsed_pdf, dict)
    assert parsed_pdf.get("body") is not None
    assert parsed_pdf.get("body") == "pdf data"
    LOG.info("Method resolution order (MRO): %s", str(PdfParser.__mro__))

    email_parser = EmailParser()
    # Well, this is disappointing that issubclass returns true
    # as EmailParser does *not* fully implement InformalParserInterface
    assert issubclass(EmailParser, InformalParserInterface) is True
    # Parse errors out b/c it does not implement extract_text().
    try:
        _ = parse(email_parser, ".", "email.txt")
        assert False
    except NotImplementedError as e:
        LOG.error("Email parser parse error: %s, %s", e.__class__, e)
    LOG.info("Method resolution order (MRO): %s", str(EmailParser.__mro__))
