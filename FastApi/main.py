from fastapi import FastAPI, Depends, HTTPException
from models import User, get_db_session
from schemas import UserSchema, UserUpdateSchema
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

@app.post('/', response_model = UserSchema)
def add_user(user_payload:UserSchema, db:Session = Depends(get_db_session)):
    user = User(**user_payload.model_dump())
    db.add(user)
    db.commit()
    return user

@app.post('/user')
def add_multiple_user(db: Session = Depends(get_db_session)):
    user_data = [{"name": "Kaustubh"}, {'name': 'Niraj'}, {'name': 'Tejas'}, {'name': 'Ayesha'}]
    users = [User(**user_data_val) for user_data_val in user_data]
    db.add_all(users)
    db.commit()

@app.get('/user', response_model = List[UserSchema])
def get_all_users(db: Session = Depends(get_db_session)):
    users = db.query(User).all()
    return users

@app.get('/user/{userid}', response_model = List[UserSchema])
def get_user(userid: int, db:Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == userid).first()
    if not user:
        raise HTTPException(status_cod = 404, details = "User id not matched")
    return user

@app.get('/user/by-name/{username}', response_model=UserSchema)
def get_user_by_username(username: str, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.name == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put('/user/{userid}', response_model = UserSchema)
def update_user(userid: int, user_update: UserUpdateSchema, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == userid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

@app.delete('/user/{userid}', response_model = UserSchema)
def delete_user(userid: int, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == userid).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    
    db.delete(user)
    db.commit
    return user
