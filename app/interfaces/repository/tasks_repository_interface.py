from abc import ABC, abstractmethod
from typing import List

from app.schemas.requests.tasks_requests import CreateTaskRequest


class ITasksRepository(ABC):

    @abstractmethod
    async def create_task(self, tasks_request: CreateTaskRequest) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def get_column_tasks(self, column_id: int) -> List:
        raise NotImplementedError()
