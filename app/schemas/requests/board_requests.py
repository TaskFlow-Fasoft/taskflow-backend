from typing import Optional

from pydantic import BaseModel


class CreateBoardRequest(BaseModel):
    title: str


class BoardUpdateRequest(BaseModel):
    title: Optional[str]
