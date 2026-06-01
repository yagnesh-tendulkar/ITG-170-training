from pydantic import BaseModel, field_validator

class Task(BaseModel):
    title:str
    priority:str
    status:str
    user_id:int

    @field_validator("priority")
    def validate_priority(cls, value):

        if value.lower() not in ["high","medium","low"]:
            raise ValueError(
                "Priority must be high, medium or low"
            )

        return value