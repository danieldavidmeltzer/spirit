import os


class Context:
    def __init__(self):
        self.data_dir = None

    @classmethod
    def build_context(cls, data_dir):
        context = cls()
        context.data_dir = data_dir
        return context

    def path(self, path_dir):
        return os.path.join(self.data_dir, path_dir)
