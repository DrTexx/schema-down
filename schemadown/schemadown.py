"""Abstraction class for using schemadown."""

# builtins
import os
from typing import List, Dict, Any

# package
from .schema import SchemaVersion
from .generate import SchemaDownDocument
from .types import DocList, JSONSchema


class SchemaDown:
    """Abstracted class for using schemadown."""

    def __init__(self, schema_version: SchemaVersion):
        """See class docstring."""
        self.schema = schema_version

    def generate_docs(self, schema: JSONSchema) -> List[SchemaDownDocument]:
        """Generate docs with data provided."""
        docs = []

        # print(schema)
        # print(type(schema))

        # TODO: in future should be result of a func/method, this is for tesing
        docs.append(
            SchemaDownDocument(
                schema=schema,
                title=self.schema.getTitle(schema),
                id=self.schema.getId(schema),
            )
        )

        # for key in schema:
        #     val = schema[key]

        #     if isinstance(val, dict):
        #         print("it's a dict")

        # create documents
        # doc = SchemaDownDocument(
        #     title=schema["id"],
        #     rootKeys=[if isinstance(schema[key])]
        # )

        # docs = [SchemaDownDocument(schema)]

        # # return DocList in requested format
        # docs = []
        # if format == "markdown":
        #     docs = [sd_doc.asMarkdown() for sd_doc in sd_docs]

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
