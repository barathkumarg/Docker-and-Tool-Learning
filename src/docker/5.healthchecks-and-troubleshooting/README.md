# Health Checks and Troubleshooting

## Goal
Build a small Docker exercise where you add health checks to a container, inspect its health state, and troubleshoot a failing or broken startup.

This task is intended for an intermediate-level practice exercise.

## Task Overview

### Main Task
Create a simple service, define a health check for it, run it in Docker, and learn how to inspect and troubleshoot container health.

## Subtasks

### 1. Create the project structure
- [x] Create a folder for the practice app
- [x] Prepare a basic application or use a simple web server image
- [x] Keep the setup minimal so health checks are easy to observe


### 2. Create a simple application or service
- [x] Build a small web app or use an image such as Nginx
- [x] Make sure the service exposes a port that can be checked
- [x] Prepare the app so it can start successfully at first


### 3. Add a health check to the container
- [x] Define a `HEALTHCHECK` instruction in the Dockerfile or in Compose
- [x] Use a command such as `curl`, `wget`, or `CMD` to verify the service is healthy
- [x] Set reasonable intervals, retries, and timeout values

### 4. Run the container and inspect health status
- [x] Start the container with Docker or Compose
- [x] Check the health state with `docker ps`
- [x] Inspect container health details with `docker inspect`

- docker-compose.yml 
```docker-compose.yml
version: '3.8'
services:
    web:
        image: nginx:alpine
        ports:
            - "8080:80"
        healthcheck:
            test: ["CMD", "curl", "-f", "http://localhost/"]
            interval: 10s
            timeout: 5s
            retries: 3

```

- output the healthy tag added near the up time in the `docker ps` command
```bash
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                   PORTS                                     NAMES
3369706be1b4   nginx:alpine   "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes (healthy)   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   simple-nginx
```

### 5. Simulate a failing health check
- [x] Break the app temporarily by changing its startup behavior or configuration
- [x] Observe the container status change to unhealthy
- [x] Confirm that the health check is being executed

- Intentionally break the health check
```docker-compose.yml
version: '3.8'

services:
  web-app:
    image: nginx:alpine
    container_name: simple-nginx-service
    ports:
      - "8080:80"
    healthcheck:
      # ❌ Broken: Trying to check port 9999 instead of 80
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:9999/"]
      interval: 5s   # Sped up to 5s so you don't have to wait long!
      timeout: 3s
      retries: 2
```

- on docker inspect
```
  "Health": {
                "Status": "unhealthy",
                "FailingStreak": 3,
```

### 6. Troubleshoot the issue
- [x] Check container logs with `docker logs`
- [x] Inspect the health check definition and command
- [x] Verify the internal port and the command being tested
- [x] Fix the issue and restart the container

## Notes

- Health checks help Docker understand whether a container is ready to serve traffic.
- A health check should test a real service condition, not just whether the process exists.
- Use simple commands first before moving to more advanced setups.
