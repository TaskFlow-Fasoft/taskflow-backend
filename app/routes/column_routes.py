from fastapi import APIRouter, Depends

from app.core.jwt_auth import decode_access_token
from app.dependencies.column import get_column_services
from app.interfaces.services.column_services_interface import IColumnServices
from app.schemas.requests.authentication_requests import UserJWTData
from app.schemas.requests.column_requests import CreateColumnRequest, DeleteColumnRequest
from app.schemas.responses.column_responses import CreateColumnResponse, DeleteColumnResponse

column = APIRouter(
    prefix="/column",
    tags=["Column"]
)


@column.post("", response_model=CreateColumnResponse)
async def create_column(
        column_request: CreateColumnRequest,
        user_data: UserJWTData = Depends(decode_access_token),
        column_services: IColumnServices = Depends(get_column_services)
) -> CreateColumnResponse:
    return await column_services.create_column(column_request, user_data)


@column.delete("", response_model=DeleteColumnResponse)
async def delete_column(
        column_request: DeleteColumnRequest,
        user_data: UserJWTData = Depends(decode_access_token),
        column_services: IColumnServices = Depends(get_column_services)
) -> DeleteColumnResponse:
    return await column_services.delete_column(column_request, user_data)
