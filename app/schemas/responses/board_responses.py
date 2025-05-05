from datetime import datetime
from typing import List

from pydantic import BaseModel


class Board(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: datetime


class GetBoardsResponse(BaseModel):
    boards: List[Board]
