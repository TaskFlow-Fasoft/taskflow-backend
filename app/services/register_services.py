from fastapi import HTTPException

from app.interfaces.repository.register_repository_interface import IRegisterRepository
from app.interfaces.services.register_services_interface import IRegisterServices
from app.schemas.requests.register_requests import UserRegistrationRequest
from app.schemas.responses.register_responses import UserRegistrationResponse


class RegisterServices(IRegisterServices):

    def __init__(self, registration_repository: IRegisterRepository):
        self.registration_repository = registration_repository

    async def user_register(self, registration_data: UserRegistrationRequest) -> UserRegistrationResponse:
        email_not_available = await self.registration_repository.email_already_registered(registration_data.email)

        if email_not_available:
            raise HTTPException(
                status_code=400,
                detail="Email já registrado. Faça seu login ou insira um novo e-mail."
            )

        user_registration = await self.registration_repository.save_registration(registration_data)

        return user_registration
