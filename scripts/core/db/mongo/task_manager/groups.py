from scripts.config.constants import DBMapping, CollectionMap
from scripts.utils.mongo_util import MongoCollectionBaseClass


class GroupMongo(MongoCollectionBaseClass):
    def __init__(self, mongo_client):
        super().__init__(
            mongo_client,
            database=DBMapping.task_manager,
            collection=CollectionMap.groups,
        )
