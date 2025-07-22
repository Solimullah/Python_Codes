from sqlalchemy.orm import Session
from .. import db, schemas
from ..auth import jwt

def get_user_by_email(db: Session, email: str):
    return db.query(db.models.User).filter(db.models.User.email == email).first()

def create_user(db: Session, user: schemas.user.UserCreate):
    hashed_password = jwt.get_password_hash(user.password)
    db_user = db.models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
