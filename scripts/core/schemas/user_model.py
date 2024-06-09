from pydantic import BaseModel


class UserUpdateModel(BaseModel):
    username: str
    user_role: str
    user_id: str
    group_ids: list


class CreateGroupModel(BaseModel):
    group_name: str
    description: str
    group_id: str
