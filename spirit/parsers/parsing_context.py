class ParsingContext:
    def __init__(self):
        self.blob_url = None

    @classmethod
    def build_context(cls, blob_url):
        context = cls()
        context.blob_url = blob_url
        return context
