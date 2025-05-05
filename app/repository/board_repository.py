from typing import Optional, List

from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.interfaces.repository.board_repository_interface import IBoardRepository
from app.schemas.responses.board_responses import Board


class BoardRepository(IBoardRepository):

    def __init__(self, connection: AsyncSession):
        self.connection = connection

    async def get_user_boards(self, user_id: int) -> Optional[List[Board]]:
        result = await self.connection.execute(
            statement=text(
                "SELECT * FROM BOARDS WHERE USER_ID = :user_id"
            ),
            params={"user_id": user_id}
        )

        boards = result.mappings().all()

        if boards:
            return [Board(**board) for board in boards]
        else:
            return None

    async def delete_board(self, board_id: int, user_id: int):
        check_existency = await self.connection.execute(
            statement=text(
                "SELECT * FROM BOARDS WHERE ID = :board_id AND USER_ID = :user_id"
            ),
            params={
                "board_id": board_id,
                "user_id": user_id
            }
        )

        if not check_existency.scalar():
            raise HTTPException(
                status_code=404,
                detail=f"Quadro não encontrado."
            )
        else:
            await self.connection.execute(
                statement=text("DELETE FROM BOARDS WHERE ID = :board_id AND USER_ID = :user_id"),
                params={
                    "board_id": board_id,
                    "user_id": user_id
                }
            )

            await self.connection.commit()
