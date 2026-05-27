from fastapi import FastAPI, WebSocket
from routes.employee_routes import router

app = FastAPI()

app.include_router(router)

clients = []


@app.get("/")
async def home():

    return {
        "message": "Employee Backend Running"
    }


# WEBSOCKET
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    clients.append(websocket)

    while True:

        data = await websocket.receive_text()

        for client in clients:

            await client.send_text(
                f"Real Time Message : {data}"
            )