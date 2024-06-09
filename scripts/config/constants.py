class DBMapping:
    task_manager = "task_manager"


class CollectionMap:
    user = "user"
    tasks = "tasks"
    groups = "groups"


class Secrets:
    LEEWAY_IN_MINS: int = 10
    ALG = "HS256"
    LOCK_OUT_TIME_MINS: int = 30
    REFRESH_TIME_IN_MINS: int = 60
    KEY = "9-kTElQo1KpR0dlhX0ihY-fBHjf1VcxoindVn7isKo8"
    access_token = "access-token"


class QueryConstants:
    project = "$project"
    match = "$match"
    in_ = "$in"
    key_mongo_mapping = {"created_at": "meta.created_at"}
    options = "$options"
    regex = "$regex"
