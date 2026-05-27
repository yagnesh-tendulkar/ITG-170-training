from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/save")
async def save_file(file: UploadFile = File(...)):

    contents = await file.read()

    with open(file.filename, "wb") as f:
        f.write(contents)

    return {"message": "File saved successfully"}
@app.get("/save")
def test():
    return {"message": "GET working"}