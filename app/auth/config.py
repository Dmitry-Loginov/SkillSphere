from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from app.core.config import settings

# Транспорт - Bearer токены
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# Стратегия - JWT
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY,
        lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

# Бэкенд аутентификации
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)