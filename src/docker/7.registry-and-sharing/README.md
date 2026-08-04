# Registry and Image Sharing

## Goal
Practice building, tagging, pushing, and pulling Docker images so they can be shared across machines or teams.

This task is intended for an intermediate-level practice exercise.

## Task Overview

### Main Task
Create a simple Docker image, push it to a registry, and pull it back to verify that it can be shared and reused.

## Subtasks

### 1. Create a simple application image
- [x] Create a small app or use a basic example for practice
- [x] Write a Dockerfile for the app
- [x] Build the image locally

```python
# main.py

# create a sample fat api application , endpoint /health and it returns the healthy on response
# create a enpoint where it checks the given number is prime endpoint /isprime?number=n
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_health():
    return {"status": "healthy"}


@app.get("/isprime")
def check_prime(number: int):
    if number < 2:
        return {"number": number, "is_prime": False}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}

```

```dockerfile
FROM --platform=amd64 python:3.11-slim

WORKDIR /app
EXPOSE 5000
COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
```

```bash
docker build -t python-prime-app .
```

```bash
docker run -d -p 5000:5000 python-prime-app --name python-prime-container
```

### 2. Tag the image properly
- [x] Add a meaningful image tag
- [x] Use a repository name and version tag
- [x] Practice tagging with a personal or local registry name

```bash
docker login 

docker tag python-prime-app barathkumargn/python-prime-app:v1.0
```

### 3. Push the image to a registry
- [x] Use Docker Hub or a local registry for practice
- [x] Authenticate if required
- [x] Push the image and verify that it is available remotely

```bash
docker push barathkumargn/python-prime-app:1.0
```

### 4. Pull the image from the registry
- [x] Remove the local image if needed
- [x] Pull the image again from the registry
- [x] Confirm that the image can be reused on another machine or environment

```bash
docker rmi python-prime-app:1.0
```


### 5. Run the pulled image
- [x] Start a container from the pulled image
- [x] Verify that the application works after pulling
- [x] Confirm that the image behaves the same way as the original local build

```bash 
docker pull barathkumargn/python-prime-app:v0.0.1

docker run -d -p 5000:5000 barathkumargn/python-prime-app:v0.0.1 --name python-prime-container
```

### 6. Practice image versioning and reuse
- [x] Tag the same image with multiple versions
- [x] Compare the behavior of different tags
- [x] Understand how tags help with rollout and rollback

### 7. Clean up and document results
- [x] Remove temporary containers and images if needed
- [x] Record the push and pull commands used
- [x] Note the final results and learning points
