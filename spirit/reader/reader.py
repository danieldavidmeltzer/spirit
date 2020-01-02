from spirit.protobuf_reprsentations import Snapshot
from spirit.protobuf_reprsentations import User
from .utils import read_item
import gzip


class Reader:
    """
    Reader for reading mind file
    """

    def __init__(self, file_name):
        """
        Initialize Reader to open gzip file in path file_name
        """
        self.file_name = file_name
        self.file_interactor = gzip.open(file_name, "rb")
        user = self._read_user()
        self.gender = user.gender
        self.username = user.username
        self.user_id = user.user_id
        self.birthday = user.birth_date

    def _read_user(self):
        """
        inner function to read the user from file
        """
        return read_item(self.file_interactor, User)

    def _read_next_snapshot(self):
        """
        inner function to read next snapshot from file
        """
        return read_item(self.file_interactor, Snapshot)

    def __iter__(self):
        return self

    def __next__(self):
        next_snapshot = self._read_next_snapshot()
        if next_snapshot is None:
            raise StopIteration()
        return next_snapshot

    def __del__(self):
        """
        close file upon de-init
        """
        self.file_interactor.close()
