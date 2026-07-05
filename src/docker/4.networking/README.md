# Docker Networking Practice

## Status
This exercise has been implemented and the basic container-to-container communication flow is working.

## Tasks
### Flask app creation
- [x] Created a Flask application that can connect to Redis

```python
from flask import Flask, request 
import redis

app = Flask(__name__)

# redis connection
connect = redis.Redis(host="redis-app", port=6379, db=0)


# Create a route with basic html to get a key-value and post a key value from the redis
@app.route("/get", methods=["GET"])
def get_value():
    """
    Get the value of a key from Redis and display it in HTML format.
    """
    key = request.args.get("key")
    value = connect.get(key)
    return f"<h1>Value for key '{key}': {value}</h1>"

@app.route("/set", methods=["POST", "GET"])
def set_value():
    """
    Set the value of a key in Redis and display it in HTML format.
    """
    if request.method == "POST":
        key = request.form.get("key")
        value = request.form.get("value")
    else:
        # render the html form for GET request
        return '''
        <form method="post">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br><br>
            <label for="value">Value:</label>
            <input type="text" id="value" name="value"><br><br>
            <input type="submit" value="Set Value">
        </form>
        '''

    connect.set(key, value)
    return f"<h1>Value set for key '{key}': {value}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

### Docker file and compose construction
- [x] Created a `docker-compose.yml` file to define the Flask and Redis services
- [x] Added a Dockerfile for the Flask app

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY app.py .
RUN pip install flask redis
EXPOSE 5000 

ENTRYPOINT ["python"]
CMD ["app.py"]
```
- [x] Set up a Redis container
- [x] Created a Docker network for both services
- [x] Connected both containers to the same network
```docker-compose.yml
version: '3'

services:
  flask-app:
    build: ./flask-app
    container_name: flask-app
    ports:
      - "5000:5000"
    networks:
      - flask-app
  
  redis-app:
    image: redis:latest
    container_name: redis-app
    ports:
      - "6379:6379"
    networks:
      - flask-app

  
networks:
  flask-app:
    driver: bridge

```

- [x] Used Docker Compose to start the services together
- [x] Verified that the Flask app communicates with Redis using the service name rather than localhost

```bash
docker-compose up -d --build
```

### Practice Docker network commands
- [x] Create a custom network manually
- [x] List all networks with `docker network ls`
```bash
docker network create flask-app-network
docker network ls
```

- [x] Inspect a network with `docker network inspect`
- [x] Connect and disconnect containers from a network
```bash
docker network inspect flask-app-network

docker network connect flask-app-network flask-app-container

docker network connect flask-app-network redis-app
```

### Compare network drivers
- [x] Practice with the `bridge` network
- [x] Try the `host` network
- [x] Understand when `none` is useful
- [x] Learn the difference between container and host networking

```bash
docker network create --driver host host-network # command will not work, since there is one host network per host
docker network ls

# Attach the network with the container
docker run -d -p 6379 --name redis-app --network host redis:latest

docker run -d -p 6379 --name redis-app --network host redis:latest
```

### 3. Understand DNS and service discovery
- [x] Check how containers resolve each other by name
- [x] Practice using service names in Compose instead of `localhost`
- [x] Observe how container IP addresses change and why DNS is preferred

```bash
# When connected in the network we can able to ping the container by its name, for example:

docker exec -it flask-app ping redis-app
```

```python
# Usage of the dns in the applicatio n code:
# Used when the network `bridge` 
connect = redis.Redis(host="redis-app", port=6379, db=0)
```

### 4. Troubleshoot communication issues
- [x] Test connectivity with `ping` or `curl`
- [x] Inspect container logs
- [x] Verify exposed ports and internal ports
- [x] Fix issues caused by wrong hostnames or missing network attachments

```bash
# Inspect the logs
docker logs flask-app

# Verification of the exposed ports and internal ports
docker port flask-app-container

# Check the network attachments
docker network inspect flask-app-network

#Issues on wrong hostnames or missing network attachments
# - > Verify the application logs, issues will be listed

docker network disconnect flask-app-network flask-app-container
docker network connect flask-app-network flask-app-container

```

### 5. Advance the exercise
- [x] Add a third service such as a database or cache
```docker-compose.yml
   # Additional service for nginx reverse proxy
   nginx-proxy:
    image: nginx:latest
    container_name: nginx-proxy-container
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
    networks:
      - frontend # Bridges the 2 networks together
      - flask-app
```
- [x] Connect multiple services to the same custom network
```docker-compose.yml
networks:
  flask-app:
    driver: bridge
  frontend:
    driver: bridge
```
- [x] Practice separating internal and external traffic
```docker-compose.yml
    # Restrict the python port to behave internally.
    #ports:  -> used for exposing to host:
    # - "5000:5000"
    expose:
      - "5000"  # Exposes the port to other containers in the same network

```
