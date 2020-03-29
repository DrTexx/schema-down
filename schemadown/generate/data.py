class DocGeneratorData:
    def __init__(self, *args):
        self.document = {}
        self.examples = self._create_examples()
