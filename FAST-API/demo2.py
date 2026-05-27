from fastapi import FastAPI
app =FastAPI()
@app.get("/")
def home():
    return "hiii alll"

@app.get("/about")
def about():
    return {"aboput" :"hiiiiii"}