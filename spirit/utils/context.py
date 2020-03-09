import os


class Context:
    def __init__(self):
        self.publish = None

    @classmethod
    def build_context(cls, publish):
        context = cls()
        context.publish = publish
        return context

