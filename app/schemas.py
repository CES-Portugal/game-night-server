from typing import List, Optional

from pydantic import BaseModel

###### TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

###### USER
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    signin_token: str

class User(UserBase):
    id: int
    is_active: bool
    points: int

    class Config:
        orm_mode = True



###### GAMEs
class Game(BaseModel):
    id: int
    name: str
    owner_id: int
    is_active: bool
    class Config:
        orm_mode = True

class Gaming(BaseModel):
    id: int
    game_id: int 
    player_id: int

    class Config:
        orm_mode = True

