from fastapi import APIRouter, Depends

from app.dependencies.register import get_register_services
from app.interfaces.services.register_services_interface import IRegisterServices
from app.schemas.requests.register_requests import UserRegistrationRequest
from app.schemas.responses.register_responses import UserRegistrationResponse

register = APIRouter(
    prefix="/register",
    tags=["Register"]
)

@register.post("", response_model=UserRegistrationResponse)
async def register_user(
        registration_data: UserRegistrationRequest,
        registration_service: IRegisterServices = Depends(get_register_services)
) -> UserRegistrationResponse:
    registration = await registration_service.user_register(registration_data)

    return registration
