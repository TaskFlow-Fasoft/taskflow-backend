from pydantic import BaseModel, EmailStr


class UserRegistrationRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str
