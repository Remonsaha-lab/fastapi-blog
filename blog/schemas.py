from typing import List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str
class Blog(BlogBase):
    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):      
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        from_attributes = True

from typing import Optional

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser] = None
    class Config():
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None  # stores user email