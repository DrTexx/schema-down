"""Defines class for json schema version 2019-09."""

from .version import SchemaVersion
from datetime import datetime


class JSONSchema2019_09(SchemaVersion):
    """Class representing JSON schema version 2019-09."""

    def __init__(self) -> None:
        """See class docstring."""
        super().__init__(name="2019-09", published=datetime(2019, 9, 16))
