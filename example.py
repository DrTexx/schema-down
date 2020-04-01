"""Example using schemadown."""

# builtin
import json

# package
from schemadown import SchemaDown, JSONSchema2019_09

SCHEMA_FILE_PATH = "/home/denver/github/schema-down/example.schema.json"


def main() -> None:
    """Body of example."""
    # instantiate schema down object
    schemadown = SchemaDown(JSONSchema2019_09())

    # load schema into memory
    schema = {}
    with open(SCHEMA_FILE_PATH) as f:
        schema = json.load(f)

    # generate docs and store in memory
    docs = schemadown.generate_docs(schema)

    # convert docs to markdown
    markdown_docs = [doc.asMarkdown() for doc in docs]

    # print generated docs to stdout
    schemadown.print_docs(markdown_docs)

    # write generated docs to files
    # schemadown.write_docs(
    #     markdown_docs, "/home/denver/github/schema-down/output"
    # )


main()
