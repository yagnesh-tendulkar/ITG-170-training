#usage of pydantic basemodel class
from pydantic import BaseModel,ValidationError


class User(BaseModel):
"""Creating a data model class with name User ,where this class represents the request data model/blueprint"""
  id :int
  name:str
  is_active:bool=True

#validation
valid_user={"id":"1","name":"balaji"}
user=User(**valid_user)
print(user.name)

#invalid user
invalid_user={"id":"invalid","name":"BALAA"}

try:
  invalid=User(**invalid_user)
except ValidationError as e:
  print(e.errors())
