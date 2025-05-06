from abc import ABC, abstractmethod

from app.schemas.requests.column_requests import CreateColumnRequest


class IColumnRepository(ABC):

    @abstractmethod
    async def create_column(self, column_request: CreateColumnRequest) -> dict:
        raise NotImplementedError()
