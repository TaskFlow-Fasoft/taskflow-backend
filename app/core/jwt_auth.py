import os
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from pytz import timezone
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


def create_access_token(email: str, algorithm: str = "HS256") -> str:
    now = datetime.now(tz=timezone("America/Sao_Paulo"))

    payload = {
        "type": "access_token",
        "exp": now + timedelta(hours=24),
        "iat": now,
        "sub": email
    }

    return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm=algorithm)


def decode_access_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        return payload["sub"]
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado.")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido.")
