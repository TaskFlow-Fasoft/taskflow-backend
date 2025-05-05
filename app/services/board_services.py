from typing import Optional

from app.core.jwt_auth import UserJWTData
from app.interfaces.repository.board_repository_interface import IBoardRepository
from app.interfaces.services.board_services_interface import IBoardServices
from app.schemas.responses.board_responses import GetBoardsResponse, BoardDeletionResponse


class BoardServices(IBoardServices):

    def __init__(self, board_repository: IBoardRepository):
        self.board_repository = board_repository

    async def get_boards(self, user_data: UserJWTData) -> Optional[GetBoardsResponse]:
        boards = await self.board_repository.get_user_boards(user_data.user_id)

        return GetBoardsResponse(boards=boards) if boards else None

    async def delete_board(self, board_id: int, user_data: UserJWTData) -> BoardDeletionResponse:
        await self.board_repository.delete_board(board_id, user_data.user_id)

        return BoardDeletionResponse(
            success=True,
            board_id=board_id,
            message=f"Quadro deletado com sucesso."
        )
