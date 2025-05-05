from abc import ABC, abstractmethod
from typing import List, Optional

from app.schemas.responses.board_responses import Board


class IBoardRepository(ABC):

    @abstractmethod
    async def get_user_boards(self, user_id: int) -> Optional[List[Board]]:
        raise NotImplementedError()
