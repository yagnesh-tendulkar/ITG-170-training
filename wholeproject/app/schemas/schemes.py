from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator


class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=18)
    email: EmailStr
    age: int = Field(gt=18, lt=60)
    password: str

    @model_validator(mode="before")
    @classmethod
    def validate_method(cls, data):
        data["name"] = data["name"].strip()
        return data


class Test(BaseModel):
    id: int = Field(gt=0) 
    name: str = Field(min_length=3, max_length=18)
    email: EmailStr
    age: int = Field(gt=18, lt=60)


@field_validator("name")
@classmethod
def validate_name(cls, value):
    if not value.isalpha():
        raise ValueError("Name should be greater than three characters")
    return value


@field_validator("email")
@classmethod
def validate_email(cls, value):
    if not value.endswith("@gmail.com"):
        raise ValueError("Only gmails are allowed!")
    return value


@field_validator("age")
@classmethod
def validate_age(cls, value):
    if value < 18:
        raise ValueError("Age must be greater than 18")
    return value

 