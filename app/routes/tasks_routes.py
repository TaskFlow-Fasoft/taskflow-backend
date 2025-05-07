from fastapi import APIRouter, Depends, Query

from app.core.jwt_auth import decode_access_token
from app.dependencies.tasks import get_tasks_services
from app.interfaces.services.tasks_services_interface import ITasksServices
from app.schemas.requests.authentication_requests import UserJWTData
from app.schemas.requests.tasks_requests import CreateTaskRequest
from app.schemas.responses.tasks_responses import CreateTaskResponse, GetColumnTasksResponse

tasks = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@tasks.post("", response_model=CreateTaskResponse)
async def create_task(
        tasks_request: CreateTaskRequest,
        user_data: UserJWTData = Depends(decode_access_token),
        tasks_services: ITasksServices = Depends(get_tasks_services)
) -> CreateTaskResponse:
    return await tasks_services.create_task(tasks_request, user_data)


@tasks.get("/{column_id]/{board_id}", response_model=GetColumnTasksResponse)
async def get_column_tasks(
        column_id: int = Query(title="ID da coluna.", description="ID da coluna que terá as tasks retornada."),
        board_id: int = Query(title="ID do quadro.", description="ID do quadro vinculado à coluna."),
        user_data: UserJWTData = Depends(decode_access_token),
        tasks_services: ITasksServices = Depends(get_tasks_services)
) -> GetColumnTasksResponse:
    return await tasks_services.get_column_tasks(column_id, board_id, user_data)
