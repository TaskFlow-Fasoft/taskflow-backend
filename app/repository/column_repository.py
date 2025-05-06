from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.interfaces.repository.column_repository_interface import  IColumnRepository
from app.schemas.requests.column_requests import CreateColumnRequest


class ColumnRepository(IColumnRepository):

    def __init__(self, connection: AsyncSession):
        self.connection = connection

    async def create_column(self, column_request: CreateColumnRequest) -> dict:
        result = await self.connection.execute(
            statement=text(
                """
                INSERT INTO BOARD_COLUMNS (
                    TITLE,
                    BOARD_ID,
                    CREATED_AT
                )
                VALUES (
                    :title,
                    :board_id,
                    CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo'
                ) RETURNING ID, CREATED_AT
                """
            ),
            params={
                "title": column_request.title,
                "board_id": column_request.board_id
            }
        )

        column_info = result.mappings().first()

        if column_info:
            await self.connection.commit()

            return dict(column_info)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ocorreu um erro ao tentar criar a coluna."
            )
