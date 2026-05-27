from fastapi import FastAPI

pb=FastAPI(title="REnamed instance",version="0.0.1",docs_url="/interactive background")

@pb.get("/")
def read():
  return {"message":"Welcome to pb instance"}
