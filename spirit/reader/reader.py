import gzip

from spirit.sample_protobuf import Snapshot
from spirit.sample_protobuf import User
from .protobuf_read import read_item


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
        self.user = self._read_user()
        self.gender = self.user.gender
        self.username = self.user.username
        self.user_id = self.user.user_id
        self.birthday = self.user.birth_date

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
