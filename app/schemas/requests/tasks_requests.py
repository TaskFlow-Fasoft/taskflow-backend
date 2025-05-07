from datetime import date

from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    board_id: int
    column_id: int
    title: str
    description: str
    due_date: date


class DeleteTaskRequest(BaseModel):
    board_id: int
    column_id: int
    task_id: int
