# SAMPLE WEB APPLICATION 

## Overview
- Building the Flask with redis application using Docker and Docker Compose.
-A sample counter application 

### Using the Pre built Image on flask app

```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### app.py 

```python
from flask import Flask
from redis import Redis

app = Flask(__name__)
# "redis" is the hostname defined in docker-compose.yml
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increment the counter in Redis
    count = redis.incr('hits')
    
    # Simple HTML UI
    return f"""
    <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
        <h1>🚀 Flask + Redis Counter</h1>
        <p style="font-size: 24px;">This page has been viewed <b>{count}</b> times.</p>
        <button onclick="location.reload()">Refresh to Count</button>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### docker-compose.yml (Version 3)

```yaml
version: '2'
services:
  redis:
    image: redis
    networks:
      - flask-app
  web:
    build: .
    container_name: flask-counter-app
    ports:
      - "5001:5000"
    environment:
      - REDIS_HOST=redis
    networks:
      - flask-app
networks:
  flask-app:

```

### requirements.txt

``` 
Flask==2.0.1
redis==4.0.2
```
### Running the Application 
To start the application:

```sh
docker-compose up -d
```