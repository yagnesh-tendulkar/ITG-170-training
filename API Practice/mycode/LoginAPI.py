from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel,EmailStr

app=FastAPI()

class UserRequest(BaseModel):
    email:EmailStr
    mobileNo:str
    country:str

COUNTRY_CODES={
    "India":"+91",
    "USA":"+1",
    "UK":"+44"
}

def format_mobile_no(user:UserRequest)->UserRequest:
    code=COUNTRY_CODES.get(user.country)
    if not code:
        raise HTTPException(status_code=400,detail="Invalid country")
    if not user.mobileNo.startswith(code):
        clear_number=user.mobileNo.lstrip("0")
        user.mobileNo=code+clear_number
    return user

@app.post("/user/save")
def save_to_db(user:UserRequest=Depends(format_mobile_no)):
    print(f"Saving user: {user.email}, {user.mobileNo}, {user.country}")
    # Save the user to the database
    return {"message":"User saved successfully","user":user}