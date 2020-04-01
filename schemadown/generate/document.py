"""Defines schema down document class."""

# site
from mdutils.mdutils import MdUtils

# package
from ..types import JSONSchema, DocList, MarkdownDocument


def resolve_ref(v) -> None:
    print("(wip) RESOLVING:", v)


def resolve_all(entry, parent) -> dict:
    # for every item in the entry
    for k, v in entry.items():
        # if the items value is a dict
        if isinstance(v, dict):
            # resolve the dict
            resolve_all(v, entry)
        # if the items value isn't a dict
        else:
            # if items value is a ref
            if k == "$ref":
                # resolve ref
                resolve_ref(v)
            # if items value is NOT a ref
            else:
                # print items value
                print(f"{k} : {v}")
    return entry


# TODO: removable, reference code for dict recursion
def myprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            if k == "$ref":
                myprint()
            print("{0} : {1}".format(k, v))


class SchemaDownDocument:
    """Standard format for schema documents despite output format. Has methods to output in specific formats."""

    def __init__(
        self, schema: JSONSchema, title: str, id: str, description: str
    ) -> None:
        """See class docstring."""
        self.schema = schema
        self.id = id
        self.title = title
        self.description = description

        # self.schema_items = {}
        # self.examples = self._create_examples()

    # def __repr__(self):
    #     return

    def asMarkdown(self) -> MarkdownDocument:
        """Return document as markdown."""
        # TODO: example, needs to be dynamic

        mdFile = MdUtils(file_name="file1.md", title="Schema")
        mdFile.new_header(level=1, title=self.title)

        # document meta headings
        documentMeta = ["Information", "Value"]
        # document meta rows
        documentMeta.extend(["Schema Id", self.id])
        documentMeta.extend(["Title", self.title])

        mdFile.new_table(columns=2, rows=3, text=documentMeta)

        # TODO: generate code snippet sections like those in the gantree docs as of 2020/03/29
        mdFile.new_paragraph('```jsonc\n{\n  "example": "text"\n}\n```')

        props = self.schema["properties"]

        resolved = resolve_all(props, None)

        print("resolved:", resolved)

        # style is set 'atx' format by default.

        # list_of_strings = ["Name", "Value"]
        # for x in range(5):
        #     list_of_strings.extend(["Schema ID", schema_id])
        # mdFile.new_line()
        # mdFile.new_table(
        #     columns=2, rows=6, text=list_of_strings, text_align="center"
        # )

        filename = mdFile.file_name
        content = mdFile.file_data_text

        return {"filename": filename, "content": content}

        # mdFile.create_md_file()
        #
        #
        #
        # contentLines = [f"# {self.title}", "", f"{self.id}", "", "Some text"]

        # contentStr = "\n".join(contentLines)

        # markdown_doc: MarkdownDocument = {
        #     "filename": "file1.md",
        #     "content": contentStr,
        # }
        # return markdown_doc
