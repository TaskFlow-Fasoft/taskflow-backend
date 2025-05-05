from fastapi import APIRouter, Depends

from app.core.jwt_auth import decode_access_token, UserJWTData
from app.dependencies.board import get_board_services
from app.interfaces.services.board_services_interface import IBoardServices
from app.schemas.responses.board_responses import GetBoardsResponse

boards = APIRouter(
    prefix="/boards",
    tags=["Boards"]
)


@boards.get("", response_model=GetBoardsResponse)
async def get_boards(
        user_data: UserJWTData = Depends(decode_access_token),
        board_services: IBoardServices = Depends(get_board_services)
) -> GetBoardsResponse:
    return await board_services.get_boards(user_data)
