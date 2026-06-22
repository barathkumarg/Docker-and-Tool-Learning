# Docker Compose - Flask with Redis

## Overview
This directory contains a multi-container Docker application using Docker Compose. It runs a Flask web application with Redis as a cache/data store.

## Files
- `docker-compose.yml` — Compose configuration with services and networks
- `dockerfile` — Dockerfile for building the Flask application image
- `app.py` — Flask application with Redis integration
- `requirements.txt` — Python dependencies

## Building and Running

### Start the application:
```sh
docker-compose up -d
```

### View logs:
```sh
docker-compose logs -f web
```

### Stop the application:
```sh
docker-compose down
```

### Access the application:
- Web app: `http://localhost:5000`
- Health check: `http://localhost:5000/health`
- Redis: `localhost:6379`

## Key Features
- **Network Bridge**: Services communicate via `app-network`
- **Volumes**: Redis data persisted via `redis-data` volume
- **Entrypoint & CMD**: Flask app configured with entrypoint and command
- **Environment Variables**: FLASK_ENV and REDIS_HOST configured
- **Restart Policy**: Both services restart automatically on failure
