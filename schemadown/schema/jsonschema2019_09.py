"""Defines class for json schema version 2019-09."""

# builtin
from datetime import datetime

# package
from .version import SchemaVersion
from ..types import JSONSchema


class JSONSchema2019_09(SchemaVersion):
    """Class representing JSON schema version 2019-09."""

    def __init__(self) -> None:
        """See class docstring."""
        super().__init__(
            name="2019-09",
            published=datetime(2019, 9, 16),
            getSchemaVersion=self._getSchemaVersion,
            getId=self._getId,
            getTitle=self._getTitle,
            getDescription=self._getDescription,
        )

    def _getSchemaVersion(self, schema: JSONSchema) -> str:
        ver: str = schema["$schema"]
        return ver

    def _getId(self, schema: JSONSchema) -> str:
        id: str = schema["$id"]
        return id

    def _getTitle(self, schema: JSONSchema) -> str:
        title: str = schema["title"]
        return title

    def _getDescription(self, schema: JSONSchema) -> str:
        desc: str = schema["description"]
        return desc
