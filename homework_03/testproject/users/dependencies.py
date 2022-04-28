from fastapi import Header, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from . import crud


def get_user_by_auth_token(token: str = Header(..., description='user auth token')):
    user = crud.get_user_to_token(token)
    if user:
        return user
    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={'message':'Invalid token'}
    )
