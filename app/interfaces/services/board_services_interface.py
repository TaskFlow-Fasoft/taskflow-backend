from abc import ABC, abstractmethod

from app.core.jwt_auth import UserJWTData
from app.schemas.responses.board_responses import GetBoardsResponse


class IBoardServices(ABC):

    @abstractmethod
    async def get_boards(self, user_data: UserJWTData) -> GetBoardsResponse:
        raise NotImplementedError()
