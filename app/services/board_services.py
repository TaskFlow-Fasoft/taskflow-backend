from typing import Optional

from app.core.jwt_auth import UserJWTData
from app.interfaces.repository.board_repository_interface import IBoardRepository
from app.interfaces.services.board_services_interface import IBoardServices
from app.schemas.responses.board_responses import GetBoardsResponse


class BoardServices(IBoardServices):

    def __init__(self, board_repositoy: IBoardRepository):
        self.board_repositoy = board_repositoy

    async def get_boards(self, user_data: UserJWTData) -> Optional[GetBoardsResponse]:
        boards = await self.board_repositoy.get_user_boards(user_data.user_id)

        return GetBoardsResponse(boards=boards) if boards else None
