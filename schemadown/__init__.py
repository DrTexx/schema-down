#!/usr/bin/env python -e

"""Tool for generating documentation for JSON schemas in Markdown."""

from .essentials import get_version
from .schemadown import SchemaDown
from .schema import SchemaVersion, JSONSchema2019_09

__version__ = get_version()
