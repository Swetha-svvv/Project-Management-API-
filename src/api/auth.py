from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.database.repository import UserRepository
from src.services.auth_service import AuthService
from src.schemas.auth import (
    UserRegister,
    UserLogin,
    TokenResponse,
    MessageResponse,
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=MessageResponse,
)
def register(
    request: UserRegister,
    db: Session = Depends(get_db),
):

    repository = UserRepository(db)

    service = AuthService(repository)

    service.register(
        request.email,
        request.password,
    )

    return {
        "message": "User registered successfully"
    }


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: UserLogin,
    db: Session = Depends(get_db),
):

    repository = UserRepository(db)

    service = AuthService(repository)

    token = service.login(
        request.email,
        request.password,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }