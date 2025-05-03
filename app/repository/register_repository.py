from pydantic import EmailStr
from pytz import timezone
from fastapi import Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.interfaces.repository.register_repository_interface import IRegisterRepository
from app.schemas.requests.register_requests import UserRegistrationRequest
from app.schemas.responses.register_responses import UserRegistrationResponse


class RegisterRepository(IRegisterRepository):

    def __init__(self, connection: AsyncSession = Depends(get_session)):
        self.connection = connection

    async def email_already_registered(self, email: EmailStr) -> bool:
        result = await self.connection.execute(
            statement=text(
                "SELECT EMAIL FROM USERS WHERE EMAIL = :email"
            ),
            params={"email": email}
        )

        return True if result.scalar() else False

    async def save_registration(self, registration_data: UserRegistrationRequest) -> UserRegistrationResponse:
        result = await self.connection.execute(
            text(
                """
                INSERT INTO USERS (
                    USERNAME,
                    EMAIL,
                    PASSWORD,
                    CREATED_AT
                )
                VALUES (
                    :username,
                    :email,
                    :password,
                    CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo'
                )
                RETURNING ID, CREATED_AT
                """
            ),
            params={
                "username": registration_data.username,
                "email": registration_data.email,
                "password": registration_data.password
            }
        )

        user_info = result.mappings().first()

        if user_info:
            current_time = user_info.get("created_at").astimezone(timezone("America/Sao_Paulo"))

            await self.connection.commit()

            return UserRegistrationResponse(
                id=user_info.get("id"),
                username=registration_data.username,
                email=registration_data.email,
                created_at=current_time
            )
        else:
            raise HTTPException(
                status_code=400,
                detail="Não foi possível realizar o cadastro. Tente novamente mais tarde."
            )
