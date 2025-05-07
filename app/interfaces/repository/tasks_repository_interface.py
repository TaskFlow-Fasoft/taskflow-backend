from abc import ABC, abstractmethod

from app.schemas.requests.tasks_requests import CreateTaskRequest


class ITasksRepository(ABC):

    @abstractmethod
    async def create_task(self, tasks_request: CreateTaskRequest) -> dict:
        raise NotImplementedError()
