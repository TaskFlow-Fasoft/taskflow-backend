from abc import ABC, abstractmethod

from app.schemas.requests.register_requests import UserRegistrationRequest
from app.schemas.responses.register_responses import UserRegistrationResponse


class IRegisterServices(ABC):

    @abstractmethod
    async def user_register(self, registration_data: UserRegistrationRequest) -> UserRegistrationResponse:
        raise NotImplementedError()
