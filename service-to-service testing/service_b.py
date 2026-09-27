from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user():
    return {
        "id": 101,
        "name": "john",
        "place": "Bangalore",
        "job": "IT-Employee"
    }
@app.get("/corp")
def get_corp():
    return{
            "name": "Samsung",
            "domain": "Electronics-chip",
            "designation": "principal"
            }
