from abc import ABC, abstractmethod

from pydantic import EmailStr

from app.schemas.requests.register_requests import UserRegistrationRequest
from app.schemas.responses.register_responses import UserRegistrationResponse


class IRegisterRepository(ABC):

    @abstractmethod
    async def email_already_registered(self, email: EmailStr) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def save_registration(self, registration_data: UserRegistrationRequest) -> UserRegistrationResponse:
        raise NotImplementedError()
