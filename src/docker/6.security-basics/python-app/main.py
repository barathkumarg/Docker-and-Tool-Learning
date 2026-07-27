from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI App", version="1.0.0")


def read_secret(name: str) -> str:
    path = f"/run/secrets/{name}"
    try:
        with open(path) as f:
            return f.read().strip()
    except FileNotFoundError:
        raise RuntimeError(f"Required secret '{name}' not found at {path}")


API_KEY = read_secret("api_key")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/secret-status")
def secret_status():
    # Never return the raw secret in a response - mask it instead
    masked = API_KEY[:4] + "..." + API_KEY[-2:] if len(API_KEY) > 6 else "***"
    return {"api_key_loaded": True, "api_key_preview": masked}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items")
def create_item(item: Item):
    return {"item": item, "created": True}