"""Defines SchemaVersion class."""

# builtin
from datetime import datetime
from typing import Callable

# package
from ..types import JSONSchema


class SchemaVersion:
    """Base class for schema versions."""

    def __init__(
        self,
        name: str,
        published: datetime,
        getSchemaVersion: Callable[[JSONSchema], str],
        getId: Callable[[JSONSchema], str],
        getTitle: Callable[[JSONSchema], str],
    ) -> None:
        """See class docstring."""
        self.name = name
        self.published = published
        self.getSchemaVersion = getSchemaVersion
        self.getId = getId
        self.getTitle = getTitle
