from datetime import date
from typing import Optional

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


class UpdateTaskRequest(BaseModel):
    board_id: int
    column_id: int
    task_id: int
    title: Optional[str]
    description: Optional[str]
    column_id: Optional[int]
    due_date: Optional[date]
