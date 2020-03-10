from spirit.utils.fetcher import find_driver
from . import drivers


class BlobStore:
    """
    class that helps mange saving and reading binaries through
    different services using different drivers
    """

    def __init__(self, url, keys=None):
        """
        initialise a blob store using a url, correct blob store and it's
        driver are identified through the url's scheme
        Args:
            url: the url of the blob store
            keys: optional keys for the blob center
        """
        self.driver = find_driver(url, drivers, keys=keys)

    def save_binary(self, binary):
        """
        save a binary to the blob store
        Args:
            binary:
                binary to save
        Returns:
            unique id for fetching the binary later
        """
        return self.driver.save_binary(binary)

    def get_binary(self, binary_id):
        """
        get binary using id given when saving
        Args:
            binary_id: the id given to the file upon saving

        Returns:
            bytes typed obj
        """
        return self.driver.get_binary(binary_id)
