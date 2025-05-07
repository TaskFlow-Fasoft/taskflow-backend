from abc import ABC, abstractmethod
from typing import List

from app.schemas.requests.tasks_requests import CreateTaskRequest, DeleteTaskRequest


class ITasksRepository(ABC):

    @abstractmethod
    async def create_task(self, tasks_request: CreateTaskRequest) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def get_column_tasks(self, column_id: int) -> List:
        raise NotImplementedError()

    @abstractmethod
    async def check_task_existency(self, task_id: int, column_id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete_task(self, column_request: DeleteTaskRequest):
        raise NotImplementedError()
