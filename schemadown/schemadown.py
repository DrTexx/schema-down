"""Abstraction class for using schemadown."""

# builtins
import os
from typing import List, Dict, Any

# package
from .schema import SchemaVersion
from .generate import DocGeneratorData
from .types import DocList


class SchemaDown:
    """Abstracted class for using schemadown."""

    def __init__(self, schema_version: SchemaVersion):
        """See class docstring."""
        self.schema_version = schema_version

    def generate_docs(
        self, schema: Dict[Any, Any], format: str = "markdown"
    ) -> DocList:
        """Generate docs with data provided."""
        docs: DocList = []

        if format == "markdown":
            # TODO: example, needs to be dynamic
            docs = [
                {"filename": "file1.md", "content": "# Header\n\ntext1"},
                {"filename": "file2.md", "content": "# Header2\n\ntext2"},
            ]

        return docs

    def print_docs(self, docs: DocList) -> None:
        """Print all the documents in a DocList to stdout."""
        for doc in docs:
            print(f"----[{doc['filename']}]----")
            print(doc["content"])

    def write_docs(self, docs: DocList, output_path: str) -> None:
        """Write all documents in a DocList to files."""
        for doc in docs:
            # create filepath for document being written
            filepath = os.path.join(output_path, doc["filename"])
            # if it doesn't already exist, create and open file
            with open(filepath, "x") as f:
                # write docs content to file
                f.write(doc["content"])
