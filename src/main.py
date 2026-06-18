from src.database.repository import UserRepository
from src.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from src.core.exceptions import (
    bad_request,
    unauthorized,
)


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, email: str, password: str):

        existing_user = self.user_repository.get_user_by_email(email)

        if existing_user:
            bad_request("Email already registered")

        hashed_password = hash_password(password)

        return self.user_repository.create_user(
            email=email,
            hashed_password=hashed_password,
        )

    def login(self, email: str, password: str):

        user = self.user_repository.get_user_by_email(email)

        if not user:
            unauthorized()

        if not verify_password(
            password,
            user.hashed_password,
        ):
            unauthorized()

        token = create_access_token(
            {"sub": str(user.id)}
        )

        return token