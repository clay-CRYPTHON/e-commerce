from fastapi import Depends, FastAPI, HTTPException, APIRouter
from fastapi_jwt_auth import AuthJWT
from starlette import status

auth_router = APIRouter(
    prefix="/auth",
)


@auth_router.get('', status_code=status.HTTP_200_OK)
async def welcome():
    # try:
    #     Authorize.jwt_required()
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    #                         detail='Enter valid access token')
    return {"message": "Bu Auth route sahifasi"}

