from abc import ABC, abstractmethod

from app.schemas.requests.authentication_requests import UserJWTData
from app.schemas.requests.tasks_requests import CreateTaskRequest
from app.schemas.responses.tasks_responses import CreateTaskResponse, GetColumnTasksResponse


class ITasksServices(ABC):

    @abstractmethod
    async def create_task(self, tasks_request: CreateTaskRequest, user_data: UserJWTData) -> CreateTaskResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_column_tasks(self, column_id: int, board_id: int, user_data: UserJWTData) -> GetColumnTasksResponse:
        raise NotImplementedError()
