from app.core.database import get_session
from app.interfaces.repository.register_repository_interface import IRegisterRepository
from app.interfaces.services.register_services_interface import IRegisterServices
from app.repository.register_repository import RegisterRepository
from app.services.register_services import RegisterServices


async def get_register_repository() -> IRegisterRepository:
    async for session in get_session():
        return RegisterRepository(session)


async def get_register_services() -> IRegisterServices:
    register_repository = await get_register_repository()
    return RegisterServices(register_repository)
