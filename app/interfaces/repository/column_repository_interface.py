from abc import ABC, abstractmethod

from app.schemas.requests.column_requests import CreateColumnRequest, DeleteColumnRequest


class IColumnRepository(ABC):

    @abstractmethod
    async def create_column(self, column_request: CreateColumnRequest) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def check_column_existency(self, column_id: int, board_id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete_column(self, column_request: DeleteColumnRequest):
        raise NotImplementedError()
