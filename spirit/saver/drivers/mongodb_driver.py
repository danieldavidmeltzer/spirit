from pymongo import MongoClient

from spirit.saver.drivers.mongodb import saver


class MongoDBDriver:
    scheme = "mongodb"

    def __init__(self, url):
        self.mongo_client = MongoClient(url)

    def save_parsing_result(self, parsing_result):
        """
        save parsing result to db in mongo client
        Args:
            parsing_result:
            the result from the parser
        Returns:

        """
        saver.save_item(parsing_result, mongo_db=self.mongo_client.spirit)
