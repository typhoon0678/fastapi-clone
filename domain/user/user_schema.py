from pydantic import BaseModel, field_validator, EmailStr


class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str
    username: str


    @field_validator('username', 'password1', 'password2', 'email', check_fields=False)
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    @field_validator('password2', check_fields=False)
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v