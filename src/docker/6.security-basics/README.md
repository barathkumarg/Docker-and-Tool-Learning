# Security Basics

## Goal
Practice basic Docker security concepts by running a container in a safer way and reducing its attack surface.

This task is intended for an intermediate-level practice exercise.

## Task Overview

### Main Task
Create a simple containerized app and apply common security practices such as non-root execution, read-only filesystems, and minimal image contents.

## Subtasks

### 1. Create a simple containerized application
- [x] Create a small app or use a basic image for practice

`main.py`
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI App", version="1.0.0")


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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items")
def create_item(item: Item):
    return {"item": item, "created": True}
```

`dockerfile`
```dockerfile
FROM python:3.13-slim

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
```

- [x Make sure the app runs successfully before applying security changes
- [x] Keep the setup minimal and easy to debug

### 2. Run the container as a non-root user
- [x] Add a non-root user in the Dockerfile
- [x] Switch to that user with `USER`
```
FROM python:3.13-slim

RUN useradd -m appser
USER appuser
```
- [x] Run the container and confirm it does not run as root
```
appuser@b5fa7b221020:/app$ whoami
appuser
appuser@b5fa7b221020:/app$ 
```

### 3. Use a read-only filesystem
- [x] Start the container with a read-only root filesystem
```
    ports:
      - "5000:5000"
    read_only: true
    tmpfs:
      - /tmp
    volumes: # Best pratice to remove the mount if not used
      - ./python-app:/app:ro
```
- [x] Avoid writing to the container filesystem unless required
- [x] Test whether the app still runs as expected
```
docker exec -it python-app touch /app/test.txt

touch: cannot touch '/app/test.txt': Read-only file system
```

### 4. Drop unnecessary Linux capabilities
- [x] Run the container with reduced capabilities
```yaml
cap_drop:
  - ALL 
#cap_add:
#  - NET_ADMIN  -> Add if you need to add capabilities
volumes: # Best pratice to remove the mount if not used
```
- [x] Use options such as `--cap-drop ALL` where appropriate
- [x] Understand the difference between a normal container and a hardened one

Normal unhardened container on ping to 8.8.8.8:
```
python-app$docker exec -it python-app ping -c 2 8.8.8.8

PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=25.5 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=25.5 ms

```

When hardened with `--cap-drop ALL`:
```
python-app$docker exec -it python-app ping -c 2 8.8.8.8

Cannot be accessed: Operation not permitted
```

### 5. Minimize image contents
- [x] Remove unnecessary packages and files from the image
- [x] Use a smaller base image when possible
- [x] Keep only what the app really needs

```
Using the python:3.13-slim image, which is already a minimal image, and removing any unnecessary packages or files during the build process.

```

### 6. Inspect the running container
- [x] Use `docker inspect` to review security-related settings
- [x] Check the user, capabilities, and filesystem options
- [x] Compare the container before and after hardening


### 7. Manage secrets safely
- [x] Practice passing secrets into a container using environment variables
- [x] Learn how to use Docker secrets in Swarm-style setups
- [x] Create a simple Docker Compose example that uses secrets without hardcoding them
- [x] Document how secrets differ from regular environment variables

- Used the file - secrets mount, which is considered to be a better practice than using environment variables for sensitive data.

```docker-compose.yml
 volumes:
      - ./python-app:/app:ro
      - ./python-app/secrets/api_key.txt:/run/secrets/api_key:ro
```

```python
def read_secret(name: str) -> str:
    path = f"/run/secrets/{name}"
    try:
        with open(path) as f:
            return f.read().strip()
    except FileNotFoundError:
        raise RuntimeError(f"Required secret '{name}' not found at {path}")
```

