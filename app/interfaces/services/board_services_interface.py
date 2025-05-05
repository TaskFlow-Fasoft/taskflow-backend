from abc import ABC, abstractmethod

from app.core.jwt_auth import UserJWTData
from app.schemas.responses.board_responses import GetBoardsResponse, BoardDeletionResponse


class IBoardServices(ABC):

    @abstractmethod
    async def get_boards(self, user_data: UserJWTData) -> GetBoardsResponse:
        raise NotImplementedError()

    @abstractmethod
    async def delete_board(self, board_id: int, user_data: UserJWTData) -> BoardDeletionResponse:
        raise NotImplementedError()
