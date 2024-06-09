from fastapi import APIRouter

from scripts.api import Endpoints
from scripts.core.handlers.task_handler import TaskHandler
from scripts.core.schemas import DefaultResponseSchema, DefaultFailureSchema
from scripts.core.schemas.task_model import TaskModel, FetchTaskModel
from scripts.utils.authorisation import MetaInfoSchema

task_router = APIRouter(prefix=Endpoints.api_task)


@task_router.post(Endpoints.api_create)
async def create_task(request_data: TaskModel, meta: MetaInfoSchema):
    try:
        task_handler = TaskHandler()
        return DefaultResponseSchema(
            data=task_handler.create_task(request_data, user_id=meta.user_id)
        )
    except Exception as e:
        return DefaultFailureSchema(message="Failed to create task", error=str(e))


@task_router.post(Endpoints.api_update)
async def update_task(request_data: TaskModel, meta: MetaInfoSchema):
    try:
        task_handler = TaskHandler()
        return DefaultResponseSchema(
            data=task_handler.update_task(request_data, user_id=meta.user_id)
        )
    except Exception as e:
        return DefaultFailureSchema(message="Failed to update task", error=str(e))


@task_router.post(Endpoints.api_fetch)
async def fetch_task(request_data: FetchTaskModel, meta: MetaInfoSchema):
    try:
        task_handler = TaskHandler()
        return DefaultResponseSchema(data=task_handler.fetch_task(request_data))
    except Exception as e:
        return DefaultFailureSchema(message="Failed to fetch task", error=str(e))
