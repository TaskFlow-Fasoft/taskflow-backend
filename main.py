from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.routes.authentication_routes import authentication

app = FastAPI(
    title="API TaskFlow",
    description="API responsável pelas requisições do TaskFlow."
)

app.include_router(authentication)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
