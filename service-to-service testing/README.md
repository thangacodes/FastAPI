# FastAPI Service-to-Service
```
FastAPI = creates APIs
httpx   = calls APIs
```
## Install dependencies

```bash
pip install -r requirements.txt

Start Service B
uvicorn service_b:app --host 0.0.0.0 --port 8001

Start Service A
Open another terminal:
uvicorn service_a:app --host 0.0.0.0 --port 8000

Test Service A
Open:
http://127.0.0.1:8000/get-user
http://127.0.0.1:8000/get-corp
API documentation
- Service A: http://127.0.0.1:8000/docs
- Service B: http://127.0.0.1:8001/docs
```
