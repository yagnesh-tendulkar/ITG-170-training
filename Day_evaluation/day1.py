from datetime import datetime
from pydantic import BaseModel
class user(BaseModel):
    id:int
    name:str
    signup_ts:datetime|None=None
    friends:list[str]
external_data={"id":"123",
               "name":"Alice",
               "signup_ts":"2026-06-12 12:22",
               "friends":["a","b","c"]
               }
user=user(**external_data)
print(user)
print(user.id)