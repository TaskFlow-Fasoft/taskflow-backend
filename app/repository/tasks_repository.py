from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.interfaces.repository.tasks_repository_interface import ITasksRepository
from app.schemas.requests.tasks_requests import CreateTaskRequest


class TasksRepository(ITasksRepository):

    def __init__(self, connection: AsyncSession):
        self.connection = connection

    async def create_task(self, tasks_request: CreateTaskRequest) -> dict:
        result = await self.connection.execute(
            statement=text(
                """
                INSERT INTO TASKS(
                    TITLE,
                    DESCRIPTION,
                    COLUMN_ID,
                    DUE_DATE,
                    CREATED_AT
                )
                VALUES (
                    :title,
                    :description,
                    :column_id,
                    :due_date,
                    CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo'
                ) RETURNING ID, CREATED_AT
                """
            ),
            params={
                "title": tasks_request.title,
                "description": tasks_request.description,
                "column_id": tasks_request.column_id,
                "due_date": tasks_request.due_date
            }
        )

        task_info = result.mappings().first()

        if task_info:
            await self.connection.commit()

            return dict(task_info)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ocorreu um erro ao criar a task."
            )
