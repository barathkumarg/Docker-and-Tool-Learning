
# Docker Compose Overview

Docker Compose is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure your application's services, networks, and volumes. With a single command, you can create and start all the services defined in the configuration.

---

## Building Images Before Compose

If your application uses custom images (for example, your own app code), you need to build these images before running `docker-compose up`. This is typically done using a `Dockerfile` for each service. You can build images manually with:

```sh
docker build -t voting-app ./src/docker-image
docker build -t result-app ./src/docker-image
docker build -t worker ./src/docker-image
```

Or, you can let Docker Compose build them automatically by specifying the `build` context in your `docker-compose.yml`:

```yaml
services:
  vote:
    build: ./src/docker-image
    ports:
      - "5000:80"
  result:
    build: ./src/docker-image
    ports:
      - "5001:80"
  worker:
    build: ./src/docker-image
```

When you use the `build` key, Compose will build the image from the specified directory (containing the Dockerfile) before starting the containers. If you use the `image` key, Compose will pull the image from a registry or use a locally available image.

---

## Basic docker-compose.yml Structure (Version 2)

```yaml
version: '2'
services:
  redis:
    image: redis
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: postgres
      POSTGRES_USER: postgres
  vote:
    image: voting-app
    ports:
      - "5000:80"
    depends_on:
      - redis
      - db
  result:
    image: result-app
    ports:
      - "5001:80"
  worker:
    image: worker
    depends_on:
      - redis
      - db
```

**Key points:**
- `version`: Specifies the Compose file format version.
- `services`: Defines the containers to run.
- `depends_on`: Controls start order (not health checks).
- `ports`: Maps host ports to container ports.

---

## Using Custom Networks (Version 2)

```yaml
version: '2'
services:
  redis:
    image: redis
    networks:
      - backend
  db:
    image: postgres
    networks:
      - backend
  vote:
    image: voting-app
    ports:
      - "5000:80"
    networks:
      - frontend
      - backend
  result:
    image: result-app
    ports:
      - "5001:80"
    networks:
      - frontend
      - backend
networks:
  frontend:
  backend:
```

**Explanation:**
- `frontend` and `backend` are user-defined networks for better isolation and control.
- Services can communicate using their service names as hostnames.

---

## Running the Application

To start the application:

```sh
docker-compose up -d
```

To stop and remove containers, networks, and volumes:

```sh
docker-compose down
```

---

## docker-compose.yml Structure (Version 3)

Version 3 is designed for Docker Swarm mode and introduces new features for orchestration. Some features from version 2 (like `links`) are removed, but `depends_on` is still supported for start order (not health).

```yaml
version: '3'
services:
  redis:
    image: redis
  db:
    image: postgres
  vote:
    image: voting-app
    ports:
      - "5000:80"
  result:
    image: result-app
    ports:
      - "5001:80"
  worker:
    image: worker
```

**Key differences in Version 3:**
- Focuses on Swarm services and orchestration.
- Adds `deploy` for scaling and resource constraints (only in Swarm mode).
- Not backward compatible with version 2.

---

## Notes

- Avoid using deprecated `links` and prefer user-defined networks.
- Use `depends_on` only for start order, not for waiting on service health.
- Always check the Docker Compose documentation for the version you are using.