from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/get-user")
async def get_user_from_service_b():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8001/user")
        response.raise_for_status()

    return {
        "message": "Data received from Service B app",
        "called": "Calling Service B API from Service A API",
        "service_b_response": response.json()
    }

@app.get("/get-corp")
async def get_corp_from_service_b():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8001/corp")
        response.raise_for_status()

    return {
        "message": "Data received from Service B app corp",
        "called": "Calling Service B API from Service A API",
        "service_b_response": response.json()
    }
