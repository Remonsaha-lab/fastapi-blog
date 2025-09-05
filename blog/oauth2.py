from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .token import verifyToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(raw_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        return verifyToken(raw_token)
    except HTTPException:
        raise
    except Exception:
        raise credentials_exception
