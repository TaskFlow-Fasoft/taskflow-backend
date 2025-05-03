from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserRegistrationResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
