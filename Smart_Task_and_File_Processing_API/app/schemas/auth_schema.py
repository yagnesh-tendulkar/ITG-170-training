from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator
)


class UserRegister(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="User Full Name"
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=6,
        max_length=100,
        description="User Password"
    )

    @field_validator("password")
    @classmethod
    def validate_password(
        cls,
        value: str
    ):

        if not any(
            char.isupper()
            for char in value
        ):
            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not any(
            char.isdigit()
            for char in value
        ):
            raise ValueError(
                "Password must contain at least one number"
            )

        return value


class UserLogin(BaseModel):

    email: EmailStr

    password: str


class TokenResponse(BaseModel):

    access_token: str

    token_type: str


class UserResponse(BaseModel):

    id: int

    name: str

    email: EmailStr


class ChangePasswordRequest(BaseModel):

    old_password: str

    new_password: str = Field(
        ...,
        min_length=6
    )

    @field_validator("new_password")
    @classmethod
    def validate_new_password(
        cls,
        value: str
    ):

        if not any(
            char.isupper()
            for char in value
        ):
            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not any(
            char.isdigit()
            for char in value
        ):
            raise ValueError(
                "Password must contain at least one number"
            )

        return value


class ForgotPasswordRequest(BaseModel):

    email: EmailStr