from fastapi import FastAPI,HTTPException,Depends
import uvicorn
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import UserCreate,UserUpdate
from app.models import User


app=FastAPI()

@app.get("/")
def home():
    return {"msg":"Welcome to the FastAPI project"}

@app.get("/users/{user_id}")
def get_user_by_email(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404,detail="User Not Found")

@app.post("/users")
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    db_user=User(name=user.name,age=user.age,email=user.email,password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/users/{user_id}")
def update_user_by_email(user_id:int,user:UserUpdate,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name=user.name
    db_user.email=user.email
    # db.refresh(db_user)
    db.commit()
    return {"msg":"User updated Successfully"}

@app.delete("/users/{user_id}")
def delete_user_by_email(user_id:int,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

