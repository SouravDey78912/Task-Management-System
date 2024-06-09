from scripts.config.constants import QueryConstants


class TaskAggregate:
    @staticmethod
    def fetch_tasks(user_ids, role):
        base_query = [{QueryConstants.match: {}}, {QueryConstants.project: {"_id": 0}}]
        if role == "admin":
            return base_query
        base_query[0][QueryConstants.match] = {
            "assigned_to": {QueryConstants.in_: user_ids}
        }
        return base_query
