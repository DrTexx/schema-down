"""Defines SchemaVersion class."""

from datetime import datetime


class SchemaVersion:
    """Base class for schema versions."""

    def __init__(self, name: str, published: datetime) -> None:
        """See class docstring."""
        self.name = name
        self.published = published
