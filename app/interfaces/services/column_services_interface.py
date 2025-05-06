from abc import ABC, abstractmethod

from app.schemas.requests.authentication_requests import UserJWTData
from app.schemas.requests.column_requests import CreateColumnRequest, DeleteColumnRequest
from app.schemas.responses.column_responses import CreateColumnResponse, DeleteColumnResponse, GetColumnsResponse


class IColumnServices(ABC):

    @abstractmethod
    async def create_column(self, column_request: CreateColumnRequest, user_data: UserJWTData) -> CreateColumnResponse:
        raise NotImplementedError()

    @abstractmethod
    async def delete_column(self, column_request: DeleteColumnRequest, user_data: UserJWTData) -> DeleteColumnResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_board_columns(self, board_id: int, user_data: UserJWTData) -> GetColumnsResponse:
        raise NotImplementedError()
