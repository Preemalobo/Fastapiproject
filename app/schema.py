#defines rules for how user data should look when sending or receiving data in our API.
#We use Pydantic (BaseModel) to validate user input , this prevents bad data from entering the database

from pydantic import BaseModel

#Form to create a new user
class UserCreate(BaseModel):
    name:str
    age:int
    email:str
    password:str

#Updating user details
class UserUpdate(BaseModel):
    name:str
    email:str
