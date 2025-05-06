from pydantic import BaseModel


class CreateColumnRequest(BaseModel):
    title: str
    board_id: int
