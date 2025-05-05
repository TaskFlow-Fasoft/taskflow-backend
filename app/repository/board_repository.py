from typing import Optional, List

from fastapi import HTTPException, status
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
                status_code=status.HTTP_400_BAD_REQUEST,
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

    async def create_board(self, title: str, user_id: int) -> dict:
        result = await self.connection.execute(
            statement=text(
                """
                INSERT INTO BOARDS (
                    TITLE,
                    USER_ID,
                    CREATED_AT
                )
                VALUES (
                    :title,
                    :user_id,
                    CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo'
                ) RETURNING ID, CREATED_AT
                """
            ),
            params={
                "title": title,
                "user_id": user_id
            }
        )

        board_info = result.mappings().first()

        if board_info:
            await self.connection.commit()

            return dict(board_info)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ocorreu um erro ao criar o quadro. Tente novamente mais tarde."
            )
