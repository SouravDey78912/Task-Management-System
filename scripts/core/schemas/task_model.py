from typing import Optional

from pydantic import BaseModel


class MetaData(BaseModel):
    created_by: Optional[str] = ""
    created_at: Optional[int] = 0
    updated_at: Optional[int] = 0
    updated_by: Optional[str] = ""


class TaskModel(BaseModel):
    task_id: Optional[str] = ""
    title: str
    description: Optional[str] = ""
    assigned_to: str
    meta: Optional[MetaData]
    due_date: int
    comments: Optional[str] = ""
    status: Optional[str] = "Open"


class FilterModel(BaseModel):
    filterModel: Optional[dict] = {}
    sortModel: Optional[list] = []


class FetchTaskModel(BaseModel):
    user_id: str
    filters: Optional[FilterModel] = FilterModel()
