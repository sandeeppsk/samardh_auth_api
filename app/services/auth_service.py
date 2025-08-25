from datetime import timedelta
from typing import Optional
from sqlalchemy.orm import Session
from app.core.security import create_access_token, create_refresh_token, verify_token
from app.services.user_service import user_service
from app.schemas.auth import Token
from app.core.config import settings

class AuthService:
    def authenticate_user(self, db: Session, username: str, password: str):
        return user_service.authenticate(db, username, password)

    def create_tokens(self, user_id: int) -> Token:
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        
        access_token = create_access_token(
            subject=user_id, expires_delta=access_token_expires
        )
        refresh_token = create_refresh_token(
            subject=user_id, expires_delta=refresh_token_expires
        )
        
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )

    def refresh_access_token(self, db: Session, refresh_token: str) -> Optional[Token]:
        user_id = verify_token(refresh_token)
        if not user_id:
            return None
        
        user = user_service.get_user(db, int(user_id))
        if not user or not user.is_active:
            return None
        
        return self.create_tokens(user.id)

auth_service = AuthService()