from datetime import timezone, datetime

import shortuuid

from scripts.core.db.mongo import mongo_client
from scripts.core.db.mongo.task_manager.tasks import TaskMongo
from scripts.core.db.mongo.task_manager.user import UserMongo
from scripts.core.schemas.task_model import TaskModel, MetaData, FetchTaskModel
from scripts.exceptions.module_exception import CustomError
from scripts.logging import logger
from scripts.core.db.mongo.aggregate.tasks_aggregate import TaskAggregate
from scripts.utils.mongo_util import MongoQueryBuilder


class TaskHandler(MongoQueryBuilder):
    def __init__(self):
        self.task_mongo = TaskMongo(mongo_client=mongo_client)
        self.user_mongo = UserMongo(mongo_client=mongo_client)

    def create_task(self, request_data: TaskModel, user_id: str) -> str:
        """
        Creates a task using the provided request data and user ID.
        Args:
            request_data: TaskModel object containing task details.
            user_id: User ID associated with the task creation.
        Returns:
            str: ID of the created task.
        Raises:
            Any Exception raised during the task creation process.
        """
        try:
            request_data.task_id = shortuuid.uuid()
            request_data.meta = MetaData(
                created_by=user_id,
                created_at=int(datetime.now(timezone.utc).timestamp()),
            )
            self.task_mongo.insert_one(request_data.model_dump())
            return request_data.task_id
        except Exception as e:
            logger.info(f"Error while creating task : {str(e)}")
            raise

    def update_task(self, request_data: TaskModel, user_id):
        """
        Updates a task with the provided data.
        Args:
            request_data (TaskModel): The data to update the task with.
            user_id: The ID of the user performing the update.
        Returns:
            None
        Raises:
            CustomError: If the task_id provided in the request_data is invalid.
        """
        try:
            if self.task_mongo.find_one(query={"task_id": request_data.task_id}):
                request_data.meta = MetaData(
                    updated_by=user_id,
                    updated_at=int(datetime.now(timezone.utc).timestamp()),
                )
                self.task_mongo.update_one(
                    query={"task_id": request_data.task_id},
                    data=request_data.model_dump(),
                )
            else:
                raise CustomError("Invalid task_id !!")
        except Exception as e:
            logger.info(f"Error while creating task : {str(e)}")
            raise

    def fetch_task(self, request_data: FetchTaskModel) -> list:
        """
        Fetches tasks based on the provided request data.
        Args:
            request_data: Data containing the user ID for fetching tasks.
        Returns:
            List: List of tasks fetched based on the request data.
        Raises:
            Any Exception raised during the task fetching process.
        """
        try:
            user_data = (
                self.user_mongo.find_one(
                    query={"user_id": request_data.user_id},
                    filter_dict={"group_ids": 1, "user_role": 1},
                )
                or {}
            )
            user_ids = user_data.get("group_ids", []) or []
            user_ids.append(request_data.user_id)
            query = TaskAggregate.fetch_tasks(
                user_ids=user_ids, role=user_data.get("user_role", "").lower()
            )
            pipeline = self.add_filters(query=query, input_data=request_data)
            if task_data := list(self.task_mongo.aggregate(pipelines=pipeline)):
                return task_data
            logger.debug("No data found")
            return []
        except Exception as e:
            logger.info(f"Error while creating task : {str(e)}")
            raise
