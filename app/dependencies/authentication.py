from typing import Optional

from app.core.database import get_session
from app.interfaces.repository.authentication_repository_interface import IAuthenticationRepository
from app.interfaces.services.authentication_services_interface import IAuthenticationServices
from app.repository.authentication_repository import AuthenticationRepository
from app.services.authentication_services import AuthenticationServices


async def get_auth_repository() -> Optional[IAuthenticationRepository]:
    async for session in get_session():
        return AuthenticationRepository(session)


async def get_auth_services() -> IAuthenticationServices:
    auth_repository = await get_auth_repository()
    return AuthenticationServices(auth_repository)
