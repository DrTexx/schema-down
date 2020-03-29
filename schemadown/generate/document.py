"""Defines schema down document class."""

from ..types import JSONSchema, DocList, MarkdownDocument


class SchemaDownDocument:
    """Standard format for schema documents despite output format. Has methods to output in specific formats."""

    def __init__(self, schema: JSONSchema, title: str, id: str) -> None:
        """See class docstring."""
        self.schema = schema
        self.title = title
        self.id = id
        # self.title = {}
        # self.schema_items = {}
        # self.examples = self._create_examples()

    # def __repr__(self):
    #     return

    def asMarkdown(self) -> MarkdownDocument:
        """Return document as markdown."""
        # TODO: example, needs to be dynamic

        contentLines = [f"# {self.title} ({self.id})", "", "Some text"]
        contentStr = "\n".join(contentLines)

        markdown_doc: MarkdownDocument = {
            "filename": "file1.md",
            "content": contentStr,
        }
        return markdown_doc
