from datetime import datetime, timedelta

from pydantic import EmailStr
from pytz import timezone
from fastapi import Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.core.jwt_auth import create_access_token
from app.interfaces.repository.authentication_repository_interface import IAuthenticationRepository
from app.schemas.requests.authentication_requests import UserRegistrationRequest, UserLoginRequest
from app.schemas.responses.authentication_responses import UserRegistrationResponse, UserLoginResponse


class AuthenticationRepository(IAuthenticationRepository):

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
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Não foi possível realizar o cadastro. Tente novamente mais tarde."
            )

    async def verify_user_credentials(self, login_data: UserLoginRequest) -> UserLoginResponse:
        result = await self.connection.execute(
            text(
                """
                SELECT 
                    EMAIL,
                    PASSWORD
                FROM USERS
                WHERE EMAIL = :email
                AND PASSWORD = :password
                """
            ),
            params={"email": login_data.email, "password": login_data.password}
        )

        credentials = result.mappings().first()

        if credentials:
            return UserLoginResponse(
                access_token=create_access_token(credentials.get("email")),
                expires_at=datetime.now(tz=timezone("America/Sao_Paulo")) + timedelta(days=1)
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Falha ao autenticar. E-mail ou senha incorretos."
            )
