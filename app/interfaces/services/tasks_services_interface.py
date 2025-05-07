from abc import ABC, abstractmethod

from app.schemas.requests.authentication_requests import UserJWTData
from app.schemas.requests.tasks_requests import CreateTaskRequest
from app.schemas.responses.tasks_responses import CreateTaskResponse


class ITasksServices(ABC):

    @abstractmethod
    async def create_task(self, tasks_request: CreateTaskRequest, user_data: UserJWTData) -> CreateTaskResponse:
        raise NotImplementedError()
