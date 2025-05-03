from pydantic import BaseModel, EmailStr


class UserRegistrationRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
