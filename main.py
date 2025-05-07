from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.authentication_routes import authentication
from app.routes.board_routes import boards
from app.routes.column_routes import column
from app.routes.tasks_routes import tasks

app = FastAPI(
    title="API TaskFlow",
    description="API responsável pelas requisições do TaskFlow."
)

app.include_router(authentication)
app.include_router(boards)
app.include_router(column)
app.include_router(tasks)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="25.59.132.184", port=8000, reload=True, log_level="info")
