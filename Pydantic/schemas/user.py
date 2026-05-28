from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator
)


# -----------------------------------
# CREATE USER REQUEST BODY
# -----------------------------------

class UserCreate(BaseModel):

    full_name: str

    email: EmailStr

    password: str

    @field_validator("password")
    @classmethod
    def validate_password(
        cls,
        value: str
    ):

        if len(value) < 8:
            raise ValueError(
                "Password must be at least 8 characters"
            )

        return value


# -----------------------------------
# UPDATE USER REQUEST BODY
# -----------------------------------

class UserUpdate(BaseModel):

    full_name: str

    email: EmailStr


# -----------------------------------
# RESPONSE MODEL
# -----------------------------------

class UserResponse(BaseModel):

    id: int

    full_name: str

    email: EmailStr

    model_config = {
        "from_attributes": True
    }


# -----------------------------------
# PATH PARAMETERS
# -----------------------------------

class UserPathParams(BaseModel):

    user_id: int = Field(
        gt=0,
        description="User ID must be greater than 0"
    )


# -----------------------------------
# QUERY PARAMETERS
# -----------------------------------

class UserQueryParams(BaseModel):

    skip: int = Field(
        default=0,
        ge=0
    )

    limit: int = Field(
        default=10,
        ge=1,
        le=100
    )