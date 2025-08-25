from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password

class UserService:
    def get_user(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create_user(self, db: Session, user: UserCreate) -> User:
        hashed_password = get_password_hash(user.password)
        db_user = User(
            email=user.email,
            username=user.username,
            hashed_password=hashed_password,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user(self, db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
        db_user = self.get_user(db, user_id)
        if db_user:
            update_data = user_update.dict(exclude_unset=True)
            if "password" in update_data:
                update_data["hashed_password"] = get_password_hash(update_data["password"])
                del update_data["password"]
            
            for field, value in update_data.items():
                setattr(db_user, field, value)
            
            db.commit()
            db.refresh(db_user)
        return db_user

    def delete_user(self, db: Session, user_id: int) -> bool:
        db_user = self.get_user(db, user_id)
        if db_user:
            db.delete(db_user)
            db.commit()
            return True
        return False

    def authenticate(self, db: Session, username: str, password: str) -> Optional[User]:
        user = self.get_user_by_username(db, username)
        if not user:
            user = self.get_user_by_email(db, username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

user_service = UserService()