from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    password: str
    salario: float

class UserLogin(BaseModel):
    email: EmailStr
    password: str
