from datetime import datetime, date

from pydantic import BaseModel


class CreateTaskResponse(BaseModel):
    id: int
    title: str
    description: str
    column_id: int
    due_date: date
    created_at: datetime
