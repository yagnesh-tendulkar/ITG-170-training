from pydantic import(BaseModel,EmailStr,field_validator)

class UserCreate(BaseModel):
    full_name:str
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod

    def validate_password(cls, value: str):

        if len(value) < 8:
            raise ValueError("password should be greater than 8 characters")
        return value

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    model_config = {"from_attributes":True}

class Update(BaseModel):
    full_name: str
    email: EmailStr

